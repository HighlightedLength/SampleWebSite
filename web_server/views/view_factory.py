import pyRazor
from pyRazor import pyrazor

class ViewFactory:
    def __init__(self):
        self.cache = {}

    def build(self, template_path, model):
        if not(template_path in self.cache):
            with open(template_path) as newFile:
                doc = newFile.read()
            #print(doc)
            self.cache[template_path] = pyrazor.Parse(doc)

        template = self.cache.get(template_path)

        return template.Render(model)
