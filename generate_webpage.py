#!/usr/bin/env python


from sys import argv
from os.path import isfile
from jinja2 import Environment, FileSystemLoader
import resize
import yaml
from glob import glob
from getopt import getopt, GetoptError


def get_photo_a(photo):
    a_tag = '<a tabindex="1" class="{0}">'.format(photo['orientation'])
    img_tag = '<img src="{0}"'.format(photo['src'])
    if 'text' in photo:
        img_tag += ' alt="{0}"'.format(photo['text'])
    img_tag += "/>"
    return "{0}{1}</a>".format(a_tag, img_tag)


should_resize = True
manifest_version = "1.0"
try:
    (opts, args) = getopt(argv[1:], "hm:", ["help", "manifest=", "no-resize"])
except GetoptError as ge:
    from sys import stderr
    stderr.write("Invalid argument")
    raise ge

for (opt, optarg) in opts:
    while opt[0] == "-":
        opt = opt[1:]
    if opt in ["h", "help"]:
        print("Options:")
        print("-h, --help\t\tThis help Dialog")
        print("-m, --manifest STRING\tUse STRING as version in manifest file.")
        print("    --no-resize\t\tDo not resize images. Only generate"
              " index page.")
        exit(0)
    elif opt in ["m", "manifest"]:
        manifest_version = optarg
    elif opt == "no-resize":
        should_resize = False


env = Environment(loader=FileSystemLoader("/Users/david/research/software"
                                          "/photoalbum/templates"))
env.filters['get_photo_a'] = get_photo_a
template = env.get_template("index.html")

photos = []
yaml_data = {}
ignore_list = []
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

if "ignore" in yaml_data:
    ignore_list = yaml_data["ignore"]

for infilename in glob("*.[jJ][pP][gG]") + glob("*.png"):
    if infilename in ignore_list:
        continue
    if should_resize:
        (filename, orientation) = resize.resize_without_thumbnail(infilename)
    else:
        (filename, orientation) = resize.get_name_and_orientation(infilename)
    if infilename in yaml_data:
        photo_data = yaml_data[infilename]
    else:
        photo_data = {}
    photo_data["src"] = filename
    photo_data["orientation"] = orientation
    photos.append(photo_data)

with open("index.html", "w") as output:
    output.write(template.render({"title": title, "photos": photos,
                                  "category": category}))

with open("manifest.appcache", "w") as output:
    output.write("CACHE MANIFEST\n")
    output.write("\n# Version: {0}\n\n".format(manifest_version))
    output.write("CACHE:\n")
    for photo in photos:
        output.write("{0}\n".format(photo["src"]))

    output.write("NETWORK:\n")
    for input in ["http://ajax.googleapis.com/ajax/libs/"
                  "jquery/1.10.2/jquery.min.js",
                  "http://photos.davecoss.com/main.css",
                  "http://photos.davecoss.com/photos.js"]:
        output.write("{0}\n".format(input))
