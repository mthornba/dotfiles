#!/usr/bin/make -f

SHELL=/bin/bash

style = nerd
starship = $(shell command -v starship)

.PHONY: clean distclean

.config/starship.toml: src/starship.toml tmp/$(style) | .config
	cat src/starship.toml tmp/$(style) > $@

tmp/nerd: src/starship.toml | tmp
	echo -e "\n# Nerd Font Symbols\n" > $@
	/usr/local/bin/starship preset nerd-font-symbols >> $@

.config:
	mkdir -p .config

tmp:
	mkdir -p tmp

clean:
	-rm -r tmp

distclean: clean
	-rm -r .config
