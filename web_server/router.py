import re
from web_server.controllers.coffee_controller import CoffeeController
from web_server.controllers.tea_controller import TeaController
from routes import Mapper
from pprint import pprint
from http import cookies

def make_map():
    """Create configure and return the routes mapper"""
    #map = Mapper(directory="C:\Users\sushr\Documents\GitHub\SampleWebSite\web_server\controllers")
    #map.minimization = False
    map = Mapper(controller_scan = ["coffee", "tea"])
    map.connect("/{controller}/{id}")
    map.connect("/{controller}/{id}/")
    #map.resource("coffee","coffees")
    #map.resource("tea","teas")

    return map

class Router:
    #def __init__(self):
    #    self.session = session

    def serve(self, environ, start_response):

        #print("environ: ")
        #pprint(environ)        //print the entire environ variable neatly

        map = make_map()

        if(environ.get('HTTP_COOKIE')):
            myCookie = cookies.SimpleCookie()
            myCookie.load(environ['HTTP_COOKIE'])
            print("Got a cookie in request: ")
            pprint(myCookie)
        else:
            print("Cookie not present in request")


        result = map.match(environ["PATH_INFO"])
        print(result)


        if(result):
            print(result['controller'])

        if(result):
            if(result['controller'] == "coffee"):
                controller = CoffeeController()
            elif(result['controller'] == "tea"):
                controller = TeaController(session)
        else:
            controller = CoffeeController()

        if(result.get('id')):
            environ["sample_website.query_value"] = result['id']
            print("query value", environ["sample_website.query_value"])


        environ["sample_website.controller"] = result['controller']

        #methodToCall = getattr(controller,result['action'])
        methodToCall = getattr(controller,environ['REQUEST_METHOD'].lower()) # .lower() to make it case insensitive
        return methodToCall(environ,start_response)
