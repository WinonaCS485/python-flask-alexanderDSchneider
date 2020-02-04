from flask import Flask, render_template
import pymysql.cursors

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/db')
def display_db():
    connection = pymysql.connect(host='mrbartucz.com',
                             user='eb1391ck',
                             password='putty1562',
                             db='eb1391ck_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    

    try:
        with connection.cursor() as cursor:
            # Select all Students
            sql = "SELECT * from Student"
        
           # execute the SQL command
            cursor.execute(sql)
            
            #for result in cursor:
                #print(result)
            # get the results
            data = cursor.fetchall()
            
            return render_template('db.html', output_data = data)
      
            # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
            # So you must commit to save your changes. 
            # connection.commit()
        

    finally:
        connection.close()
           

if __name__ == '__main__':
    app.run(debug=True, port=1391)
