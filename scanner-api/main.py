from flask import Flask
from flask_cors import CORS
from os import *
import queue
import threading

queue = queue.Queue(maxsize=0)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
	target = 'vulnweb.com'

	scanner1 = threading.Thread(scanner('-PS -F', target, queue))
	scanner2 = threading.Thread(scanner('-PA -F', target, queue))

	scanner1.start()
	scanner2.start()

	return queue.get_nowait()

def scanner(setting, target, queue):
	command = 'nmap ' + setting + ' ' + target
	process = popen(command)
	results = str(process.read())
	queue.put(results)

if __name__ == '__main__':
	app.run(debug=True)