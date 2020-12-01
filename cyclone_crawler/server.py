import time
from http.server import HTTPServer
from api import GetHandler
from config import HOST_NAME, HOST_PORT

#if __name__=='__main__':
server_class = HTTPServer
httpd = server_class((HOST_NAME, HOST_PORT), GetHandler)
print(f"{time.asctime()}, Starting server @{HOST_NAME}:{HOST_PORT}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print(f"{time.asctime()}, Stopping server")

