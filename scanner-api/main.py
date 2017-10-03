from flask import Flask
from os import *

app = Flask(__name__)

@app.route('/')
def index():
	target = 'vulnweb.com'
	scanner1 = scanner('-PS -F', target)
	scanner2 = scanner('-PA -F', target)
	return scanner1 + '--------\n' + scanner2

def scanner(setting, target):
	command = 'nmap ' + setting + ' ' + target
	process = popen(command)
	results = str(process.read())
	return results

if __name__ == '__main__':
	app.run(debug=True)