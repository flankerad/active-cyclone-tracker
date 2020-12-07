import requests
import json
import logging
import time
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from config import HOST_NAME, HOST_PORT
from app.api import get_response
from app.db import close_connection
from connection import create_connection

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class GetHandler(BaseHTTPRequestHandler):

      """Handles Server requests for API"""

      def do_HEAD(self):
            self.send_response(200)
            self.send_header("Content-type", "applications/json")
            self.end_headers()

      def do_GET(self):
            '''GET REQUEST'''
            conn = create_connection()

            try:
                  data = get_response(conn, self.path)
                  self.send_response(200)

            except Exception as e:
                  logger.error(e)
                  self.send_error(400)
                  data = str(e)
                  close_connection(conn)

            finally:
                  self.send_header("Content-type", "application/json")
                  self.end_headers()
                  self.wfile.write(json.dumps(data).encode())


httpd = HTTPServer((HOST_NAME, int(HOST_PORT)), GetHandler)
logger.info(f"{time.asctime()}, Starting server @{HOST_NAME}:{HOST_PORT}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
    print(f"{time.asctime()}, Stopping server")

httpd.server_close()
print(f"{time.asctime()}, Stopping server")

