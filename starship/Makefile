#!/usr/bin/make -f

SHELL=/bin/bash

targets = .config/starship.toml
style = nerd

.PHONY: clean distclean

all: $(targets) clean

$(targets): src/starship.toml $(style) | .config
	cat src/starship.toml $(style) > $@

nerd:
	echo -e "\n# Nerd Font Symbols\n" > $@
	$(shell command -v starship) preset nerd-font-symbols >> $@

.config:
	mkdir -p $@

clean:
	-rm $(style)

distclean: clean
	-rm -r .config
