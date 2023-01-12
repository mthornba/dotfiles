#!/usr/bin/make -f

SHELL=/bin/bash

.PHONY: clean stow nerd

nerd: src/starship.base stow
	rm -f $@
	echo -e "\n# Nerd Font Symbols\n" > $@
	/usr/local/bin/starship preset nerd-font-symbols >> $@
	cat src/starship.base $@ > .config/starship.toml
	rm -f $@

stow:
	mkdir -p .config

clean:
	rm -rf .config
