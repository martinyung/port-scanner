from os import *

def scanner(setting, host, results):
	command = 'nmap ' + setting + ' ' + host
	process = popen(command)
	report = str(process.read())
	results[setting] = (report)