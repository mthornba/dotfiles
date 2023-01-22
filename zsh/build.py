#!/usr/bin/env python3

import sys, platform
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./src")
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)
os = platform.system()
template_vars = { "os": os }

for file in sys.argv[1:]:
  TEMPLATE_FILE = file.lstrip(".") + ".j2"
  template = templateEnv.get_template(TEMPLATE_FILE)
  outputText = template.render(template_vars)

  f = open(file, "w")
  f.write(outputText)
  f.close()
