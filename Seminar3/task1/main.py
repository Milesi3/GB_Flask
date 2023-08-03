import random

from flask import Flask, request, render_template, abort, redirect, url_for, flash, session
from task1.model import db, Student, Faculty


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    for i in range(5):
        faculty = Faculty(name=f"faculty_{i}")
    for i in range(20):
        student = Student(firstname=f"name_{i}", lastname="Иванов", age=random.randint(18,30))


@app.route('/students/')
def all_students():
    students = Student.query.all()
    facultys = Faculty.query.all()
    context = {'students': students,
               'facultys': facultys}
    return render_template('students.html', **context)
