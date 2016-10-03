import re
from web_server.controllers.coffee_controller import CoffeeController
from web_server.controllers.tea_controller import TeaController
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

        if(results.get(id)):
            environ["sample_website.query_value"] = results['id']

        environ["sample_website.controller"] = results['controller']

        methodToCall = getattr(controller,result['action'])
        return methodToCall(environ,start_response)
