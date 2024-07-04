from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sumit.db'

db = SQLAlchemy(app)


class student(db.Model):
    roll_No = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('Name')
        department = request.form.get('Department')

        newStudent = student(name=name, department=department)
        db.session.add(newStudent)
        db.session.commit()

        return redirect('/')

    else:
        students = student.query.all()
        return render_template('home.html', students=students)


@app.route('/update', methods=['GET', 'POST'])
def update():

    roll_No = request.args.get('sno')
    data = student.query.filter_by(roll_No=roll_No).first()

    if request.method == 'POST':

        name = request.form.get('Name')
        department = request.form.get('Department')

        data.name = name
        data.department = department

        db.session.add(data)
        db.session.commit()

        return redirect('/')
    else:

        return render_template('update.html', student=data)

@app.route('/delete')
def delete():
    roll_No = request.args.get('sno')
    data = student.query.filter_by(roll_No=roll_No).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')


# app.run(debug=True)
