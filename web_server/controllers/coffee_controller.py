from app_server.access.data_contexts.data_context_factory import DataContextFactory
from web_server.views.view_factory import ViewFactory
from web_server.models.model1 import model
from web_server.domain.factories.domain_factory import DomainFactory
from web_server.domain.services.domain_service import DomainService

class CoffeeController:
    def index(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]

        start_response(status, headers)

        domain = DomainFactory()
        domain_model  = domain.buildModel(environ,start_response)
        domainService1 = DomainService()
        result = domainService1.action(domain_model)
        print (result)

        #factoryObject  = DataContextFactory()
        #comment = factoryObject.factory(1)
        comment = "data from database"

        view = ViewFactory()
        model1 = model()

        # response = {}
        # response['method_name'] = ("index").encode("utf-8")
        # response['comment'] = comment
        # response['model'] = model1

        #ret = view.build(r"web\views\form1.html", model1)
        ret = [("You GET a free coffee in index" + "\n" + comment).encode("utf-8")]
        #return [ret.encode("utf-8")]
        #return response
        return ret

    def create(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]

        start_response(status, headers)

        domain = DomainFactory()
        domain_model  = domain.buildModel(environ,start_response)
        domainService1 = DomainService()
        result = domainService1.action(domain_model)
        print (result)

        #factoryObject  = DataContextFactory()
        #comment = factoryObject.factory(1)
        comment = "data from database"

        view = ViewFactory()
        model1 = model()

        # response = {}
        # response['method_name'] = ("index").encode("utf-8")
        # response['comment'] = comment
        # response['model'] = model1

        #ret = view.build(r"web\views\form1.html", model1)
        ret = [("You GET a free coffee in create" + "\n" + comment).encode("utf-8")]
        #return [ret.encode("utf-8")]
        #return response
        return ret

    def new(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]

        start_response(status, headers)

        domain = DomainFactory()
        domain_model  = domain.buildModel(environ,start_response)
        domainService1 = DomainService()
        result = domainService1.action(domain_model)
        print (result)

        #factoryObject  = DataContextFactory()
        #comment = factoryObject.factory(1)
        comment = "data from database"

        view = ViewFactory()
        model1 = model()

        # response = {}
        # response['method_name'] = ("index").encode("utf-8")
        # response['comment'] = comment
        # response['model'] = model1

        #ret = view.build(r"web\views\form1.html", model1)
        ret = [("You GET a free coffee in new" + "\n" + comment).encode("utf-8")]
        #return [ret.encode("utf-8")]
        #return response
        return ret

    def update(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]

        start_response(status, headers)

        domain = DomainFactory()
        domain_model  = domain.buildModel(environ,start_response)
        domainService1 = DomainService()
        result = domainService1.action(domain_model)
        print (result)

        #factoryObject  = DataContextFactory()
        #comment = factoryObject.factory(1)
        comment = "data from database"

        view = ViewFactory()
        model1 = model()

        # response = {}
        # response['method_name'] = ("index").encode("utf-8")
        # response['comment'] = comment
        # response['model'] = model1

        #ret = view.build(r"web\views\form1.html", model1)
        ret = [("You GET a free coffee in update" + "\n" + comment).encode("utf-8")]
        #return [ret.encode("utf-8")]
        #return response
        return ret
    def delete(self, environ, start_response):
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]

        start_response(status, headers)

        domain = DomainFactory()
        domain_model  = domain.buildModel(environ,start_response)
        domainService1 = DomainService()
        result = domainService1.action(domain_model)
        print (result)

        #factoryObject  = DataContextFactory()
        #comment = factoryObject.factory(1)
        comment = "data from database"

        view = ViewFactory()
        model1 = model()

        # response = {}
        # response['method_name'] = ("index").encode("utf-8")
        # response['comment'] = comment
        # response['model'] = model1

        #ret = view.build(r"web\views\form1.html", model1)
        ret = [("You GET a free coffee in delete" + "\n" + comment).encode("utf-8")]
        #return [ret.encode("utf-8")]
        #return response
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
