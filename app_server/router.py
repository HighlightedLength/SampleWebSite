import re
from app_server.app.controllers.coffee_controller import CoffeeController
from app_server.app.controllers.tea_controller import TeaController
from routes import Mapper
from urllib.parse import parse_qsl

def matchString(environ):

    controllerList = []
    reString1 = r"/coffee"
    reString2 = r"/tea"

    p1 = re.compile(reString1, re.IGNORECASE)
    p2 = re.compile(reString2, re.IGNORECASE)

    m1 = p1.match(environ["QUERY_STRING"])
    m2 = p2.match(environ["QUERY_STRING"])

    #if m1:
    controllerList.append(m1)
    #else:
    controllerList.append(m2)

    return controllerList

class Router:
    def serve(self, environ, start_response):

        query = parse_qsl(environ["QUERY_STRING"])  #Parse a query string given as a string argument. Data are returned as a list of name, value pairs.
        print(query)                                # this prints in command prompt

        environData = matchString(environ)

        if(environData[0]):
            controller = CoffeeController()
        elif(environData[1]):
            controller = TeaController()
        else:
            controller = CoffeeController()

        if environ["REQUEST_METHOD"] == 'GET':
            return controller.index(environ, start_response)
        elif environ["REQUEST_METHOD"] == 'POST':
            return controller.create(environ, start_response)




        # status = '200 OK'
        # headers = [('Content-type', 'text/plain; charset=utf-8')]
        #
        # start_response(status, headers)
        #
        # comment = "my comment in app server router"
        #
        # ret = [("You GET a free coffee in create" + "\n" + comment).encode("utf-8")]
        # return ret



        # if environ["REQUEST_METHOD"] == 'GET':
        #     return controller.get_view(environ, start_response)
        # elif environ["REQUEST_METHOD"] == 'POST':
        #     return controller.post_edit(environ, start_response)

        # map = Mapper(controller_scan = ["coffees", "teas"])
        #
        # #map = Mapper()
        #
        # map.resource("coffee","coffees")
        # map.resource("tea","teas")
        #
        # result = map.match(environ["PATH_INFO"])
        # print(result)
        # if(result):
        #     print(result['controller'])
        #
        # if(result['controller'] == "coffee"):
        #     controller = CoffeeController()
        # elif(result['controller'] == "tea"):
        #     controller = TeaController()
        # else:
        #     controller = TeaController()
        #
        # print(environ["QUERY_STRING"])
        #
        # #environ["sample_website.query_value"] = result['id']
        #
        # methodToCall = getattr(controller,result['action'])
        # return methodToCall(environ,start_response)
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
