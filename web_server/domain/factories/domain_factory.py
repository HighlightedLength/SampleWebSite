class DomainFactory:
    def buildModel(self, environ, start_response):
        values = (environ["REQUEST_METHOD"], environ["sample_website.controller"], environ["sample_website.query_value"])

        return values
