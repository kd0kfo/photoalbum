#!/usr/bin/env python


from sys import argv
import yaml
from jinja2 import Environment, FileSystemLoader

yaml_data = yaml.load(open("info.yaml", "r"))

env = Environment(loader=FileSystemLoader("/Users/david/research/software/"
                                          "photoalbum/templates"))
template = env.get_template("category_index.html")

title = ""
category = None
parent = None
if 'title' in yaml_data:
    title = yaml_data['title']
if 'category' in yaml_data:
    category = yaml_data['category']

with open("index.html", "w") as output:
    output.write(template.render({"title": title,
                                  "categories": yaml_data["categories"],
                                  "category": category}))
