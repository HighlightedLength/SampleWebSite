from wsgiref.simple_server import make_server
from app_server.router import Router

router = Router()

httpd = make_server('', 8000, router.serve)
print("Server started on port 8000...")
httpd.serve_forever()
