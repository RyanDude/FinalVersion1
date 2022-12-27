from flask import Flask, render_template, request, redirect, url_for
from utils import sql_util, KM
from config import config
import pymysql
import math

app = Flask(__name__)
db = pymysql.connect(host='localhost', user='root', passwd=config['MYSQL_PASSWORD'], database=config['DATABASE_NAME'],
                     charset='utf8')


# main page, admin login, student register, mentor register
@app.route('/')
def home():
    return render_template('home.html')


# student register function
@app.route('/student_register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'GET':
        # check if the admin open the portal
        sql = "select status from system_info where name = 'register_info'"
        result = sql_util.query(sql, db)
        # based on fields(controlled by admin), to generate fields for student to select
        sql_field = "select name from field"
        all_field = sql_util.query(sql_field, db)
        if result[0][0]:
            return render_template('student_register.html', all_field=all_field)
        else:
            return "The administrator closed the registration channel"
    else:
        # get submitted form to finish the register
        name = request.form.get('std_name')
        password = request.form.get('std_password')
        email = request.form.get('std_email')
        panther_id = request.form.get('panther_id')
        gender = request.form.get('gender')
        race = request.form.get('race')
        field = request.form.get('field')
        field = field[2:-3]
        p_gender = request.form.get('p_gender')
        p_race = request.form.get('p_race')
        p_position = request.form.get('p_position')
        sql = "insert into student(name,email,panther_id,race,gender,p_gender,p_race,p_position,field,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = [name, email, panther_id, race, gender, p_gender, p_race, p_position, field, password]
        sql_util.insert(sql, data, db)
        return render_template("register_success.html")


# mentor register function, it is same as student register
@app.route('/mentor_register', methods=['GET', 'POST'])
def mentor_register():
    if request.method == 'GET':
        sql = "select status from system_info where name = 'register_info'"
        result = sql_util.query(sql, db)
        sql_field = "select name from field"
        all_field = sql_util.query(sql_field, db)
        if result[0][0]:
            return render_template('mentor_register.html', all_field=all_field)
        else:
            return "The administrator closed the registration channel"
    else:
        name = request.form.get('mt_name')
        password = request.form.get('mt_password')
        email = request.form.get('mt_email')
        position = request.form.get('position')
        gender = request.form.get('gender')
        race = request.form.get('race')
        field = request.form.get('field')
        field = field[2:-3]
        number = request.form.get('number')
        sql = "insert into mentor(name,email,position,gender,race,field,number,password) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data = [name, email, position, gender, race, field, number, password]
        sql_util.insert(sql, data, db)
        return render_template("register_success.html")


# admin login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # compare id and password
        id = request.form.get('id')
        password = request.form.get('password')
        sql = "select * from admin where name = '%s' and password = '%s'" % (id, password)
        result = sql_util.query(sql, db)
        print(result)
        if len(result) != 0:
            return redirect(url_for('manager'))
        else:
            return u'User Not Found'


@app.route('/mentor_login', methods=['GET', 'POST'])
def mentor_login():
    if request.method == 'GET':
        return render_template('mentor_login.html')
    else:
        # compare username and password
        name = request.form.get('name')
        password = request.form.get('password')
        sql = "select * from mentor where name = '%s' and password = '%s'" % (name, password)
        result = sql_util.query(sql, db)
        if len(result) != 0:
            # get mentor information
            sql2 = "select  s.name from relationship rs,mentor m,student s where m.name='%s' and m.id=rs.mentor_id and rs.student_id=s.id" % name
            students = sql_util.query(sql2, db)
            if len(students) > 0:
                return render_template('mentor_homepage.html', students=students)
            else:
                return render_template("no_match.html")
        else:
            return u'User Not Found'


@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'GET':
        return render_template('student_login.html')
    else:
        # compare username and password
        name = request.form.get('name')
        password = request.form.get('password')
        sql = "select * from student where name = '%s' and password = '%s'" % (name, password)
        result = sql_util.query(sql, db)
        if len(result) != 0:
            sql2 = "select m.name from relationship rs,mentor m,student s where s.name='%s' and s.id=rs.student_id and rs.mentor_id=m.id"
            mentor = sql_util.query(sql2, db)
            if len(mentor) > 0:
                return render_template('student_homepage.html', mentor=mentor)
            else:
                return render_template("no_match.html")
        else:
            return u'User Not Found'


# open/close register portal
@app.route('/change_status', methods=['GET'])
def change_status():
    sql_query = "select status from system_info where name='register_info'"
    result = sql_util.query(sql_query, db)
    if result[0][0]:
        result = 0
    else:
        result = 1
    sql_update = "update system_info set status=%d where name='register_info'" % result
    sql_util.update(sql_update, db)
    return "Registration status changed successfully"


@app.route('/relationship_matching', methods=['GET', 'POST'])
def relationship_matching():
    if request.method == 'GET':
        # sql, clean previous relationship
        sql_truncate_relationship = "truncate relationship"
        sql_query_student = "select id,name,p_gender,p_race,field FROM student"
        sql_query_mentor = "SELECT id,name,gender,race,FIELD,number FROM mentor"
        sql_insert_relationship = "insert into relationship(student_id,mentor_id) value (%s,%s)"
        # clean the relationship
        sql_util.delete(sql_truncate_relationship, db)
        # get student/mentor info
        result_student = sql_util.query(sql_query_student, db)
        result_mentor = sql_util.query(sql_query_mentor, db)
        student = list(result_student)
        mentor = list(result_mentor)

        all_match_id = []
        all_match_name = []
        score = 0
        cycle_number = 1
        # use KM to match students and mentors
        while (len(student) > 0 and len(mentor) > 0):

            student, id, name, sum = KM.match(student, mentor)
            # iterate mentor set，remove the mentors(number of students >= cycle_number)
            new_mentor = []
            for i in range(len(mentor)):
                if int(mentor[i][5]) >= cycle_number:
                    new_mentor.append(mentor[i])
            mentor = new_mentor
            #
            all_match_name.extend(name)
            all_match_id.extend(id)
            #
            score += sum
            #
            cycle_number += 1
        # insert into database
        sql_util.insert_many(sql_insert_relationship, all_match_id, db)
        return render_template('admin.html', all_match_name=all_match_name, score=score)
    else:
        return "test2"


# admin add field
@app.route('/add_field', methods=['GET', 'POST'])
def add_field():
    if request.method == 'GET':
        return render_template('add_field.html')
    else:
        field = request.form.get("add_field")
        sql = "insert into field(name) value (%s)"
        sql_util.insert(sql, field, db)
        return redirect(url_for('manager'))


# admin delete field
@app.route('/delete_field', methods=['GET', 'POST'])
def delete_field():
    if request.method == 'GET':
        return render_template('delete_field.html')
    else:
        field = request.form.get("field_delete")
        sql = "delete from field where name = '%s'" % field
        sql_util.delete(sql, db)
        return redirect(url_for('manager'))


# admin page
@app.route('/manager', methods=['GET', 'POST'])
def manager():
    if request.method == 'GET':
        sql_field = "select name from field"
        all_field = sql_util.query(sql_field, db)
        return render_template('manager.html', all_field=all_field)
    else:
        print("test")


if __name__ == '__main__':
    # app.run()
    app.run(host="127.0.0.1", port="8089")
