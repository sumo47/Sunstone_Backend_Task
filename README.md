# Student Management App

A simple web application for managing students, library, and bank accounts using Flask and SQLAlchemy.

## Features

* Add, update, and delete student records.
* Add, update, and delete library book records.
* Add, update, and delete bank account records.

## Requirements

* Python 3.x
* Flask
* SQLAlchemy

## Installation

1. Clone the repository:
   ```bash
   https://github.com/sumo47/Sunstone_Backend_Task.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Sunstone_Backend_Task
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Set up the database:
   * Ensure you have a database (e.g., SQLite, PostgreSQL) set up.
   * Configure the database URI in your Flask app configuration:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sumit.db'
     ```

2. Create the database tables:
   ```python
   from app import db
   db.create_all()
   ```
>>> create new python file and run this code there
## Usage

1. Run the Flask application:
   ```bash
   flask run
   ```
   >>> or use command `python app.py`
2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Code Explanation

### Main Application

```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sumit.db'
db = SQLAlchemy(app)
```

### Models

#### Student Model

```python
class student(db.Model):
    roll_No = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)
```

#### Library Model

```python
class library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(20), nullable=False)
```

#### Bank Model

```python
class bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_no = db.Column(db.Integer, nullable=False)
    ifsc = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    bank_Name = db.Column(db.String(20), nullable=False)
```

### Routes

#### Student Routes

```python
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
```

```python
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
```

```python
@app.route('/delete')
def delete():
    roll_No = request.args.get('sno')
    data = student.query.filter_by(roll_No=roll_No).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/')
```

#### Library Routes

```python
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
```

```python
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
```

```python
@app.route('/library/delete')
def bookDelete():
    book_id = request.args.get('book_id')
    data = library.query.filter_by(id=book_id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/library')
```

#### Bank Routes

```python
@app.route('/bank', methods=['GET', 'POST'])
def bankHome():
    if request.method == 'POST':
        account_no = request.form.get('account_no')
        ifsc = request.form.get('ifsc')
        name = request.form.get('name')
        bank_Name = request.form.get('bank_Name')
        newAcount = bank(name=name, ifsc=ifsc, account_no=account_no, bank_Name=bank_Name)
        db.session.add(newAcount)
        db.session.commit()
        return redirect('/bank')
    else:
        listOfAccount = bank.query.all()
        return render_template('bank.html', accounts=listOfAccount)
```

```python
@app.route('/bank/update', methods = ['GET', 'POST'])
def bankUpdate():
    account_id = request.args.get('id')
    accountData = bank.query.filter_by(id=account_id).first()
    if request.method == 'POST':
        account_no = request.form.get('account_no')
        ifsc = request.form.get('ifsc')
        name = request.form.get('name')
        bank_Name = request.form.get('bank_Name')
        accountData.account_no = account_no
        accountData.ifsc = ifsc
        accountData.name = name
        accountData.bank_Name = bank_Name
        db.session.add(accountData)
        db.session.commit()
        return redirect('/bank')
    else:
        return render_template('bankUpdate.html', account=accountData)
```

```python
@app.route('/bank/delete')
def accountDelete():
    account_id = request.args.get('id')
    data = bank.query.filter_by(id=account_id).first()
    db.session.delete(data)
    db.session.commit()
    return redirect('/bank')
```

## Contributing

Contributions are welcome! Please create a pull request or submit an issue for any improvements or bugs.

---
