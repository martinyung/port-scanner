from flask import Flask, jsonify
from flask_cors import CORS
from scanner import *
import threading

app = Flask(__name__)
CORS(app)

@app.route('/scan')
def scan():
	host = 'vulnweb.com'
	results = []

	# creating thread for different scans setting
	scanner1 = threading.Thread(target=scanner('-PS -F', host, results))
	scanner2 = threading.Thread(target=scanner('-PA -F', host, results))

	scanner1.start()
	scanner2.start()

	return jsonify(results)

if __name__ == '__main__':
	app.run(debug=True)