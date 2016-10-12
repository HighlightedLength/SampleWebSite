from app_server.access.data_contexts.data_context_factory import DataContextFactory
from web_server.views.view_factory import ViewFactory
from web_server.models import model1
import json

class CoffeeController:
    def index(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'json; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        #view = ViewFactory()
        #model1 = model1()

        response = {}
        response['method_name'] = "index"
        response['comment'] = comment
        response['model'] = "app_server index"

        jsonResponse = json.dumps(response)
        print(jsonResponse)
        #ret = view.build(r"web\views\form1.html", model1)
        #ret = [("You GET a free coffee in index" + "\n" + comment).encode("utf-8")]
        #return ret
        return [jsonResponse.encode("utf-8")]

    def create(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'json; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(2)

        #view = ViewFactory()
        #model1 = model1()

        response = {}
        response['method_name'] = "create"
        response['comment'] = comment
        response['model'] = "app_server index"

        jsonResponse = json.dumps(response)
        #ret = view.build(r"web\views\form1.html", model1)
        ret = [("You GET a free coffee in index" + "\n" + comment).encode("utf-8")]
        return [ret.encode("utf-8")]
        #return jsonResponse.encode("utf-8")

    def new(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'json; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        ret = [("You GET a free coffee in new" + "\n" + comment).encode("utf-8")]
        return ret
    def update(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee in update").encode("utf-8")]
        return ret

    def delete(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee").encode("utf-8")]
        return ret
    def show(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee").encode("utf-8")]
        return ret
    def edit(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee").encode("utf-8")]
        return ret
