# Python_SQL
AceAcademy

create Virtual environment using #venv module - `python -m venv backend`
 --- now the installed packages will be store in virtual env
activate virtual environment  - `backend\Scripts\activate` || `backend/Scripts/activate`

after that i wll install my module - `pip install flask` etc

// so now the flask will be install in my backend folder (virtual environment) inside project

// if i'll install without activating virtual environment than the module will be install in my system folder (c folder of window)

* To run Python program - `python main.py`

* to open vscode in virtual environment , first activate v-env on CMD , then write code . (to open vscode in that folder)

# API
 * If want to rander/display html file than we have to import function rander_template from flask module `from flask import render_template`
 * Have to create templates folder on root folder and save all the html files insite templates folder
 * now return html file as an argument of render_template function - `return render_template(index.html)`

 >> is ths comment
 - markdown

 * Reload server automatically when any changes applied - `app.run(debug=True)`
   debug = true , statement can display error on webpage
 * if want to serve application in my network - `app.run(debug=True, host='0.0.0.0')`

 
