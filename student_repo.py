import os
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        #password="",
        password=os.getenv("MYSQL_PASSWORD"),
        database="student_db",

    )
    return connection

def get_student():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "select * from student"

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "Success" : True,
        "message" : "stdents Fetched successfully",
        "data" : students
    }


def insert_student(student):
    connection = get_connection()
    cursor = connection.cursor()
    query = "insert into student(name, course, fee) values (%s, %s, %s)"

    cursor.execute(query, (student.name, student.course, student.fee))

    connection.commit() #required for insert
    cursor.close()
    connection.close()
    return {
        "Success": True,
        "message": "stdents Inserted successfully",
        "data": student
    }