from app_server.access.data_contexts.data_context_factory import DataContextFactory

class TeaController:
    def get_view(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        ret = [("You GET a free tea in get_view" + "\n" + comment).encode("utf-8")]
        return ret

    def get_edit(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        ret = [("You GET a free tea in get_edit" + "\n" + comment).encode("utf-8")]
        return ret

    def view(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        factoryObject  = DataContextFactory()

        comment = factoryObject.factory(1)

        ret = [("You GET a free tea in view" + "\n" + comment).encode("utf-8")]
        return ret
    def post_edit(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of tea in post_edit").encode("utf-8")]
        return ret

    def post_form(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of stuff").encode("utf-8")]
        return ret
