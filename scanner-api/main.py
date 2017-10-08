from flask import Flask, jsonify
from flask_cors import CORS
from scanner import *
import threading

app = Flask(__name__)
CORS(app)

@app.route('/scan')
def scan():
	host = 'vulnweb.com'
	results = {}

	# creating thread for different scan settings

	ack_scan = threading.Thread(target=scanner('-sA -F', host, results))
	syn_scan = threading.Thread(target=scanner('-sS -F', host, results))
	xmass_scan = threading.Thread(target=scanner('-sX -F', host, results))
	null_scan = threading.Thread(target=scanner('-sN -F', host, results))

	ack_scan.start()
	syn_scan.start()
	xmass_scan.start()
	null_scan.start()

	return jsonify(results)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='80')