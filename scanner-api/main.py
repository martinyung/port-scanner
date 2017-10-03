from flask import Flask
from os import *

app = Flask(__name__)

@app.route('/')
def index():
	command = 'nmap -F vulnweb.com'
	process = popen(command)
	results = str(process.read())
	return results

if __name__ == '__main__':
	app.run(debug=True)