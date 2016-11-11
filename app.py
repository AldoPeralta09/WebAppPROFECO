# -*- coding: utf-8 -*-
import web
import json

render = web.template.render("views/")

urls = (
    "/index(.*)", "index"
)

class index:
    def GET(self, data_list):
        with open('200datos.json', 'r') as file:
            data_list = json.load(file)
        return render.index(data_list["results"])
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
