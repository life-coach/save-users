
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def hello_world():
	with open("emails.txt", "a") as myfile:
		myfile.write(request.form['email'] + "\n")
	return "thank you"

