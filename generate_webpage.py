#!/usr/bin/env python


from sys import argv
from os.path import isfile
from jinja2 import Environment, FileSystemLoader
import resize
import yaml
from glob import glob

def get_photo_a(photo):
    a_tag = '<a tabindex="1" class="horizontal">'
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

for file in glob("IMG*.jpg"):
    filename = resize.resize_without_thumbnail(file)
    if file in yaml_data:
        photo_data = yaml_data[file]
    else:
        photo_data = {}
    photo_data["src"] = filename
    photos.append(photo_data)

print(template.render({"title": title, "photos": photos, "category": {"url": "http://davecoss.com", "label": "Main page"}}))

