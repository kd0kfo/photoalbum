#!/usr/bin/env python


def get_size(filename):
    from PIL import Image
    image = Image.open(filename)
    return image.size


def resize(newfilename, filename, newsize):
    from PIL import Image
    image = Image.open(filename)
    image = image.resize(newsize)
    image.save(newfilename)


def create_thumbnail(thumbnail_name, filename, factor=6):
    orig_size = get_size(filename)
    newsize = (orig_size[0]/factor, orig_size[1]/factor)
    resize(thumbnail_name, filename, newsize)


def get_name_and_orientation(filename):
    resized_filename = "reduced_{0}".format(filename)

    size = get_size(filename)
    if size[0] > size[1]:
        newsize = (600, 450)
        orientation = "horizontal"
    else:
        newsize = (450, 600)
        orientation = "vertical"

    return (resized_filename, orientation)


def resize_without_thumbnail(filename):

    resized_filename = "reduced_{0}".format(filename)

    size = get_size(filename)
    if size[0] > size[1]:
        newsize = (600, 450)
        orientation = "horizontal"
    else:
        newsize = (450, 600)
        orientation = "vertical"
    resize(resized_filename, filename, newsize)

    return (resized_filename, orientation)


def resize_and_thumbnail(filename):
    thumbnail_filename = "thumb_{0}".format(filename)
    (resized_filename, orientation) = resize_without_thumbnail(filename)
    create_thumbnail(thumbnail_filename, resized_filename)

if __name__ == "__main__":
    from sys import argv

    filename = argv[1]
    resize_and_thumbnail(filename)
