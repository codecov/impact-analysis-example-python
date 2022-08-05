from gevent import monkey
monkey.patch_all()

import os
from gevent.pywsgi import WSGIServer
from app import app

http_server = WSGIServer(('127.0.0.1', 8080), app)
http_server.serve_forever()