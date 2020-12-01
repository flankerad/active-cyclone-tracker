from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

import requests
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)




class GetHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        import ipdb; ipdb.set_trace()
        SimpleHTTPRequestHandler.do_GET(self)

Handler=GetHandler

httpd=HTTPServer(("localhost", 8080), Handler)
print("Running server @8080")
httpd.serve_forever()


