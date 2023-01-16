#!/usr/bin/env python

import jinja2

# environment = jinja2.Environment()
# template = environment.from_string("Hello, {{ name }}!")
# print(template.render(name="World"))

templateLoader = jinja2.FileSystemLoader(searchpath="./src")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "zshrc.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render()  # this is where to put args to the template renderer

print(outputText)
