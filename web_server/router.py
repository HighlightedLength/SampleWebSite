import re
from web_server.controllers.coffee_controller import CoffeeController
from web_server.controllers.tea_controller import TeaController
from routes import Mapper

def make_map():
    """Create configure and return the routes mapper"""
    #map = Mapper(directory="C:\Users\sushr\Documents\GitHub\SampleWebSite\web_server\controllers")
    #map.minimization = False
    map = Mapper(controller_scan = ["coffees", "teas"])
    map.resource("coffee","coffees")
    map.resource("tea","teas")

    return map

class Router:
    def serve(self, environ, start_response):

        map = make_map()

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
