from flask import Flask, render_template, redirect, request, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)

app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    is_valid = True
    if len(request.form['email']) == 0:
        flash("Email is required")
        is_valid = False

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Not valid email")
        is_valid = False

    if len(request.form['fname']) < 0:
        flash("Your first name is required.")
        is_valid = False
    elif not request.form['fname'].isalpha():
        flash("Incorrect please enter first name, no numerics")
        is_valid = False

    if len(request.form['lname']) < 0:
        flash("Your last name is required.")
        is_valid = False
    elif not request.form['lname'].isalpha():
        flash("Incorrect please enter last name, no numerics")
        is_valid = False

    if len(request.form['pw']) < 8:
        flash("Invalid password, please make atleast 8 characters")
        is_valid = False

    elif len(request.form['pw']) != len(request.form['confpw']):
        flash("Passwords do not match")
        is_valid = False

    if is_valid:
        flash("Thank you for submitting your information.")

    return redirect('/')

app.run(debug=True)