#!/usr/bin/env python3

import sys, jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./src")
templateEnv = jinja2.Environment(loader=templateLoader)

for file in sys.argv[1:]:
  TEMPLATE_FILE = file.lstrip(".") + ".j2"
  template = templateEnv.get_template(TEMPLATE_FILE)
  outputText = template.render()

  f = open(file, "w")
  f.write(outputText)
  f.close()
