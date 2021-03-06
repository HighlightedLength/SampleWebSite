from app_server.access.data_contexts.data_context_factory import DataContextFactory
from web_server.views.view_factory import ViewFactory
from web_server.models.model1 import model
from web_server.domain.factories.domain_factory import DomainFactory
from web_server.domain.services.domain_service import DomainService
from urllib.parse import parse_qsl

def tempMethod(environ, start_response, myString):
    status = '200 OK'

    s1 = ('Set-Cookie', 'theme=light')
    s2 = ('Set-Cookie', 'sessionToken=session123')
    headers = [('Content-type', 'text/html; charset=utf-8'), s1, s2]



    start_response(status, headers)

    domain = DomainFactory()
    domain_model  = domain.buildModel(environ,start_response)
    domainService1 = DomainService()
    result = domainService1.action(domain_model)
    print ("results: text", result.text)
    print ("results:json", result.json)
    print ("results - encoding ", result.encoding)

    #factoryObject  = DataContextFactory()
    #comment = factoryObject.factory(1)
    comment = "data from database"

    view = ViewFactory()
    viewModel = model()

    print("viewModel: ",viewModel.textData, viewModel.tableData,viewModel.method)

    viewModel.buildModel(result.text)


    # response = {}
    # response['method_name'] = ("index").encode("utf-8")
    # response['comment'] = comment
    # response['model'] = model1

    ret = view.build(r"web_server\views\form1.html", viewModel)
    #ret = [("You GET a free coffee in "+myString + "\n" + comment).encode("utf-8")]
    return [ret.encode("utf-8")]
    #return response
    #return ret

class CoffeeController:
    def get(self, environ, start_response):

        ret = tempMethod(environ, start_response,"get1")
        return ret

    def post(self, environ, start_response):

        try:
            length = int(environ.get('CONTENT_LENGTH','0'))
        except ValueError:
            length = 0

        if length != 0:
            bodyBytes = environ['wsgi.input'].read(length)
            print(bodyBytes)
        else:
            print("some error in body")

        body = parse_qsl(bodyBytes.decode(), True)  # keep blank values = True
        print("body decoded: ", body)

        ret = tempMethod(environ, start_response,"post1")
        return ret

    def index(self, environ, start_response):

        ret = tempMethod(environ, start_response,"index1")
        return ret

    def create(self, environ, start_response):
        ret = tempMethod(environ, start_response,"create1")
        return ret

    def new(self, environ, start_response):
        ret = tempMethod(environ, start_response,"new1")
        return ret

    def update(self, environ, start_response):
        ret = tempMethod(environ, start_response,"update1")
        return ret
    def delete(self, environ, start_response):
        ret = tempMethod(environ, start_response,"delete1")
        return ret

    def show(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee in show").encode("utf-8")]
        return ret
    def edit(self, environ, start_response):
        status = '999 NOT OK'
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        start_response(status, headers)

        ret = [("Sorry! We are out of coffee in edit").encode("utf-8")]
        return ret
