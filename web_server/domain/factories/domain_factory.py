class DomainFactory:
    def build_model:
        values = (environ["REQUEST_METHOD"], environ["sample_website.controller"], environ["sample_website.query_value"])

        return values
