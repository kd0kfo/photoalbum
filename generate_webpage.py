#!/usr/bin/env python


from sys import argv
from os.path import isfile
from jinja2 import Environment, FileSystemLoader
import resize
import yaml
from glob import glob

def get_photo_a(photo):
    a_tag = '<a tabindex="1" class="{0}">'.format(photo['orientation'])
    img_tag = '<img src="{0}"'.format(photo['src'])
    if 'text' in photo:
        img_tag += ' alt="{0}"'.format(photo['text'])
    img_tag += "/>"
    return "{0}{1}</a>".format(a_tag, img_tag)


env = Environment(loader=FileSystemLoader("/Users/david/research/software/photoalbum/templates"))
env.filters['get_photo_a'] = get_photo_a
template = env.get_template("index.html")

photos = []
yaml_data = {}
if isfile("info.yaml"):
    yaml_data = yaml.load(open("info.yaml", "r"))


if "title" in yaml_data:
    title = yaml_data['title']
else:
    title = ""

if "category" in yaml_data:
    category = yaml_data["category"]
else:
    category = {"url": "http://photos.davecoss.com", "label": "Main page"}

for file in glob("*.[jJ][pP][gG]") + glob("*.png"):
    (filename, orientation) = resize.resize_without_thumbnail(file)
    if file in yaml_data:
        photo_data = yaml_data[file]
    else:
        photo_data = {}
    photo_data["src"] = filename
    photo_data["orientation"] = orientation
    photos.append(photo_data)

print(template.render({"title": title, "photos": photos, "category": category}))

