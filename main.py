from http.server import HTTPServer, SimpleHTTPRequestHandler 

PORT = 8000
server_address = ('', PORT)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f'Server is running on http://127.0.0.1:{PORT}')

httpd.serve_forever()
