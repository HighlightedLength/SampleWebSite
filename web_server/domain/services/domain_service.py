import requests

class DomainService:
    def action(self, domain_model):
        payload = {'controller': domain_model[1], 'id': domain_model[2]}
        if(domain_model[0] == "GET"):
            r = requests.get('http://localhost:8000/', params = payload)
            print(r.url)
            return r
        elif(domain_model[0] == "POST"):
            r = requests.post('http://localhost:8000/', params = payload)
            print(r.url)
            return r
