# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:24:20 2020
Task Master Application.
@author: Deepesh W
"""
import os
from flask import Flask, url_for, redirect, render_template,request
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_mail import Mail,Message

os.environ["APP_SETTINGS"] = "Config.DevelopmentConfig"
#print(os.environ["APP_SETTINGS"])
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
mail = Mail(app)

# '''app.config['MYSQL_DATABASE_HOST']= 'localhost'
# app.config['MYSQL_DATABASE_PORT']=3306
# app.config['MYSQL_DATABASE_USER']='root'
# app.config['MYSQL_DATABASE_PASSWORD']='romamw*9'
# app.config['MYSQL_DATABASE_DB']= 'customers'
# '''

mysql = MySQL(cursorclass=DictCursor,autocommit=True)
mysql.init_app(app)

@app.route('/',methods=['POST', 'GET'])

def index():
    cursor = mysql.get_db().cursor()
    if request.method == "POST":
        tasks_content = request.form['content']  #call of User input from database for view.
        End_on = request.form['End_on']
        Status = request.form['Status']
        qry = "INSERT INTO customers.task_master(content, end_on,proj_status) \
                VALUES(%s,%s,%s)"  # values is given in string input.
        #print('tasks_content is: ', tasks_content)
        
        try:
            cursor.execute(qry,(tasks_content,End_on, Status))
            #msg = Message("new task added.", sender="wadhwani.deep52@gmail.com", recipients = ["wadhwani.deep52@gmail.com","wadhwani.suman@gmail.com"])
            # for multiple recipients add recipients email ids in a list as above
            #msg.body = tasks_content
            #mail.send(msg)
            return redirect('/')
          #  cursor.commit() # flask-MySQL library doesn't support commit like this, it autocommits as above(line20)
        except:
           # mysql.rollback() # flask-MySQL library doesn't support rollback.
            cursor.close() #closing db.
            print('There was an issue adding your task.')
    else:
         cursor.execute('SELECT * FROM customers.task_master')  # sql query to fetch all the data from db.
         tasks = cursor.fetchall() # it feteches all the data present in db in onego.
         cursor.close()
         return render_template('try.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    cursor = mysql.get_db().cursor()
    qry_del = "DELETE FROM customers.task_master where id=%s"

    try:
        cursor.execute(qry_del,(id))
        return redirect('/')
    except:
        return 'There was problem deleting that task.'

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    cursor = mysql.get_db().cursor()
    qry_update = "UPDATE customers.task_master SET CONTENT = %s, end_on = %s, proj_status = %s where id = %s;"

    if request.method == "POST":
        tasks_content = request.form['content']
        End_on = request.form['End_on']
        Status = request.form['Status']
        try:
            cursor.execute(qry_update, (tasks_content,End_on,Status,id))
            return redirect('/')
        except:
            return 'There was issue updating your task.'
    else:
        cursor.execute('SELECT * FROM customers.task_master where id = %s', (id))
        task = cursor.fetchone()
        return render_template('update.html', task=task)

    
if __name__ == '__main__':
    app.run(debug=True)
    