import requests
import json
import logging
import time
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from config import HOST_NAME, HOST_PORT
from api import get_response

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



class GetHandler(BaseHTTPRequestHandler):

      def do_HEAD(self):
            self.send_response(200)
            self.send_header("Content-type", "applications/json")
            self.end_headers()

      def do_GET(self):
            '''GET REQUEST'''
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = get_response(self.path)
            self.wfile.write(json.dumps(data).encode())


server_class = HTTPServer
httpd = server_class((HOST_NAME, HOST_PORT), GetHandler)
print(f"{time.asctime()}, Starting server @{HOST_NAME}:{HOST_PORT}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
    print(f"{time.asctime()}, Stopping server")

httpd.server_close()
print(f"{time.asctime()}, Stopping server")

