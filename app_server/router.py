import re
from app_server.app.controllers.coffee_controller import CoffeeController
from app_server.app.controllers.tea_controller import TeaController
from routes import Mapper

class Router:
    def serve(self, environ, start_response):

        map = Mapper(controller_scan = ["coffees", "teas"])

        #map = Mapper()

        map.resource("coffee","coffees")
        map.resource("tea","teas")

        result = map.match(environ["PATH_INFO"])
        print(result)
        if(result):
            print(result['controller'])

        if(result['controller'] == "coffee"):
            controller = CoffeeController()
        elif(result['controller'] == "tea"):
            controller = TeaController()
        else:
            controller = TeaController()

        print(environ["QUERY_STRING"])

        #environ["sample_website.query_value"] = result['id']

        methodToCall = getattr(controller,result['action'])
        return methodToCall(environ,start_response)
        # map.connect(None, "/", controller = "coffee")
        # map.connect(None, "/{controller}/{id}")
        # map.connect(None, "/{controller}/{acion}/{id}")

        # result  = map.match(environ["PATH_INFO"])
        #
        # print(environ["PATH_INFO"])
        # print(result)
        #
        # if(result['controller'] == "coffee"):
        #     controller = CoffeeController()
        # elif(result['controller'] == "tea"):
        #     controller = TeaController()
        # else:
        #     controller = TeaController()
        #
        # if environ["REQUEST_METHOD"] == 'GET':
        #     return controller.get_view(environ, start_response)
        # elif environ["REQUEST_METHOD"] == 'POST':
        #     return controller.post_edit(environ, start_response)
