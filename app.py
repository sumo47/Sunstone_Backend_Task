from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sumit.db'

db = SQLAlchemy(app)


class student(db.Model):
    roll_No = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)


class library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(20), nullable=False)


class bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)


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

# Library-------------------------------------------------------------------------------------


@app.route('/library', methods=['GET', 'POST'])
def LibraryHome():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        description = request.form.get('description')

        newBook = library(title=title, author=author, description=description)
        db.session.add(newBook)
        db.session.commit()

        return redirect('/library')
    else:
        books = library.query.all()
        return render_template('/library.html', books=books)


@app.route('/library/update', methods=['GET', 'POST'])
def LibraryUpdate():
    book_id = request.args.get('book_id')
    bookData = library.query.filter_by(id=book_id).first()

    if request.method == 'POST':

        title = request.form.get('title')
        description = request.form.get('description')
        author = request.form.get('author')

        bookData.title = title
        bookData.description = description
        bookData.author = author

        db.session.add(bookData)
        db.session.commit()

        return redirect('/library')
    else:

        return render_template('libraryUpdate.html', book=bookData)


@app.route('/library/delete')
def bookDelete():
    book_id = request.args.get('book_id')
    data = library.query.filter_by(id=book_id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/library')


app.run(debug=True)
