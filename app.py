# -*- coding: utf-8 -*-
import web
import json
import csv

data = []

with open('200datos.json', 'r') as file:
    data = json.load(file)

file = open("datos.csv","w")

for row in data["results"]:
    file.write("{},{},{},{},{}\n".format(row["nombreComercial"],row["producto"],row["precio"],row["latitud"],row["longitud"]))

file.close()

render = web.template.render("views/")

urls = (
    "/index(.*)", "index"
)

class index:
    def GET(self, data_list):
        data_list = []
        with open("datos.csv","r") as filename:
            datos = csv.reader(filename, delimiter = ",")
            for row in datos:
                data_list.append(row)
        return render.index(data_list)
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
