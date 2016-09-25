import re
from app_server.app.controllers.coffee_controller import CoffeeController
from app_server.app.controllers.tea_controller import TeaController
from pprint import pprint
from routes import Mapper

class Router:
    def serve(self, environ, start_response):

        map = Mapper(controller_scan = ["coffee", "tea"])

        map.connect(None, "/", controller = "coffee")
        map.connect(None, "/{controller}/{id}")
        map.connect(None, "/{controller}/{acion}/{id}")

        result  = map.match(environ["PATH_INFO"])

        print(environ["PATH_INFO"])
        print(result)

        if(result['controller'] == "coffee"):
            controller = CoffeeController()
        elif(result['controller'] == "tea"):
            controller = TeaController()
        else:
            controller = TeaController()

        pprint(dir(controller))

        if environ["REQUEST_METHOD"] == 'GET':
            return controller.view(environ, start_response)
        elif environ["REQUEST_METHOD"] == 'POST':
            return controller.post_edit(environ, start_response)
