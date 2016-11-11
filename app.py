# -*- coding: utf-8 -*-
import web
import json

data = []

render = web.template.render("views/")

urls = (
    "/index(.*)", "index"
)

class index:
    def GET(self, data_list):
        with open('200datos.json', 'r') as file:
            data = json.load(file)
        return render.index(data["results"])
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
