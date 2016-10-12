import json
import pprint

class model:
    method = ""
    textData = ""
    tableData = ""
    def buildModel(self, response):
        obj = json.loads(response)
        self.method = obj["method_name"]
        self.textData = obj["model"]
        self.tableData = obj["comment"]
        return
        #pprint.pprint(obj)
