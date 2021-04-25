import pymysql
from app import app
import mysql.connector
from flask import jsonify
from flask import flash, request
import json

# create user
@app.route('/createuser', methods=['POST'])
def create_user():
	try:
		_json = request.json
		_username = _json['username']
		_password = _json['password']
		_role = _json['role']
		# insert record in database
		sqlQuery = "INSERT INTO users(username, password, role) VALUES(%s, %s, %s)"
		data = (_username, _password, _role,)
		conn = mysql.connector.connect(  host="35.178.122.25",  user="root",  password="password",  database="demo")
		cursor = conn.cursor()
		cursor.execute(sqlQuery, data)
		conn.commit()
		res = jsonify('User created successfully.')
		res.status_code = 200
		return res
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/users')
def users():
	try:
		conn = mysql.connector.connect(  host="35.178.122.25",  user="root",  password="password",  database="demo")
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT username,password,role FROM users")
		rows = cursor.fetchall()
		result = {"users": rows}
		return result
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/users/<sqlusername>')
def user(sqlusername):
	try:
		conn = mysql.connector.connect(  host="35.178.122.25",  user="root",  password="password",  database="demo")
		cursor = conn.cursor(dictionary=True)
		sqlquery = "select username,password,role from users where username=%s"
		cursor.execute(sqlquery, (sqlusername,))
		row = cursor.fetchone()
		return row
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/courses')
def courses():
	try:
		conn = mysql.connector.connect(  host="35.178.122.25",  user="root",  password="password",  database="demo")
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT courseid,coursename,duration FROM courses")
		rows = cursor.fetchall()
		result = {"courses": rows}
		return result
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/enrollments')
def enrollments():
	try:
		conn = mysql.connector.connect(  host="35.178.122.25",  user="root",  password="password",  database="demo")
		cursor = conn.cursor(dictionary=True)
		cursor.execute("SELECT enrollmentid,username,courseid FROM enrollments")
		rows = cursor.fetchall()
		result = {"enrollments": rows}
		return result
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/enrollments/<sqlusername>')
def userenrollment(sqlusername):
	try:
		conn = mysql.connector.connect(  host="35.178.122.25",  user="root",  password="password",  database="demo")
		cursor = conn.cursor(dictionary=True)
		sqlquery = "SELECT enrollmentid,username,courseid FROM enrollments where username=%s"
		cursor.execute(sqlquery, (sqlusername,))
		row = cursor.fetchone()
		return row
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404

    return res

if __name__ == "__main__":
    app.run()
