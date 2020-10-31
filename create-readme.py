#!/usr/bin/python3
import os
import sys
from functools import reduce

def join(a, b):
  return a + b

def template(title, files, ext, depth):
  def make_link(f):
    title = os.path.basename(f).replace(ext, "")
    return """1. [{}]({})""".format(title, f)

  title = "#" * depth + " " + title + "\n"
  links = list(map(make_link, files))
  links = str(reduce(lambda a, b: a + b + "\n", links, ""))

  return title + links

def rec_search(dir, ext, depth, ignored):
  def ffilter(path):
    _, f_ext = os.path.splitext(path)
    return f_ext == ext

  elems = list(map(lambda p: os.path.join(dir, p), os.listdir(dir)))
  dirs  = list(filter(os.path.isdir, elems))
  dirs  = list(filter(lambda p: ignored.count(os.path.basename(p)) == 0, dirs))
  files = list(filter(os.path.isfile, elems))
  files = list(filter(ffilter, files))
  files = sorted(files)
  
  nxt = list(map(lambda p: rec_search(p, ext, depth + 1, ignored), dirs))
  out = template(os.path.basename(dir), files, ext, depth)

  return reduce(join, nxt, out)


print(rec_search(sys.argv[1], ".html", 0, ["OneDrive_1_28-8-2020", ".vscode", "recursos", ".git"]))
