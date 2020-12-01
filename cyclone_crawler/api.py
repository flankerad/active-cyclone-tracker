from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

import requests
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



class GetHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_resonse(200)
        self.send_header("Content-type", "applications/json")
        self.end_headers()

    def do_GET(self):
        '''GET REQUEST'''
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"recieved":"ok"}).encode())

