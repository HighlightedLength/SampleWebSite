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

        if(result):
            if(result['controller'] == "coffees"):
                controller = CoffeeController()
            elif(result['controller'] == "teas"):
                controller = TeaController()
        else:
            controller = CoffeeController()

        if(result.get('id')):
            environ["sample_website.query_value"] = result['id']
            print("query value", environ["sample_website.query_value"])


        environ["sample_website.controller"] = result['controller']

        methodToCall = getattr(controller,result['action'])
        return methodToCall(environ,start_response)
