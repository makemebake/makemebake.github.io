from flask import Flask 
from flask import render_template 
from flask import request 

app = Flask ("MyApp")


@app.route("/")
def signup():
	return render_template("enterdetails.html")

@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form
	print form_data['name']
	print form_data['email']
	return render_template("done.html")

app.run()