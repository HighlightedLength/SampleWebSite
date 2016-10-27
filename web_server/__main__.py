from wsgiref.simple_server import make_server
from web_server.router import Router

session = {}

router = Router()

httpd = make_server('', 8080, router.serve)
print("Server started on port 8080...")
httpd.serve_forever()
