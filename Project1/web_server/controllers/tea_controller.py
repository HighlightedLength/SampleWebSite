from app_server.access.data_contexts.data_context_factory import DataContextFactory

class TeaController:
        def get(self, environ, start_response):
            status = '200 OK'
            headers = [('Content-type', 'text/plain; charset=utf-8')]

            start_response(status, headers)

            factoryObject  = DataContextFactory()
            comment = factoryObject.factory(2)

            ret = [("You get iced tea" + "\n" + comment).encode("utf-8")]

            return ret
        def post(self, environ, start_response):
            status = '999 NOT OK'
            headers = [('Content-type', 'text/plain; charset=utf-8')]

            start_response(status, headers)

            ret = [("Sorry! Get out").encode("utf-8")]
            return ret
