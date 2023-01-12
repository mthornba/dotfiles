#!/usr/bin/make -f

SHELL=/bin/bash

.PHONY: clean stow

stow:
	mkdir -p .config

nerd: starship.base stow
	rm -f $@
	echo -e "\n# Nerd Font Symbols\n" > $@
	/usr/local/bin/starship preset nerd-font-symbols >> $@
	cat starship.base $@ > .config/starship.toml
	rm -f $@

clean:
	rm -rf .config
