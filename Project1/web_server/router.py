import re
from web_server.controllers.coffee_controller import CoffeeController
from web_server.controllers.tea_controller import TeaController
from routes import Mapper

class Router:
    def serve(self, environ, start_response):

        map = Mapper()

        map.connect(None, "/{controller}/{id}")
        map.connect(None, "/{controller}/{acion}/{id}")

        result  = map.match(environ["PATH_INFO"])
        if(result['controller'] == "coffee"):
            controller = CoffeeController()
        elif(result['controller'] == "tea"):
            controller = TeaController()
        else:
            contoller = TeaController()

        if environ["REQUEST_METHOD"] == 'GET':
            return controller.get(environ, start_response)
        elif environ["REQUEST_METHOD"] == 'POST':
            return controller.post(environ, start_response)
