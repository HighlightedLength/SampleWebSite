from app_server.access.data_contexts.data_context_factory import DataContextFactory
from web.views.view_factory import ViewFactory
from web.models import model

class CoffeeController:
    def get_view(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        view = ViewFactory()
        model1 = model()

        ret = view.build(r"web\views\form1.html", model1)
        #ret = [("You GET a free coffee" + "\n" + comment).encode("utf-8")]
        return [ret.encode("utf-8")]

    def get_edit(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        ret = [("You GET a free coffee" + "\n" + comment).encode("utf-8")]
        return ret

    def view(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        ret = [("You GET a free coffee" + "\n" + comment).encode("utf-8")]
        return ret
    def post_edit(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee").encode("utf-8")]
        return ret

    def post_form(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee").encode("utf-8")]
        return ret
