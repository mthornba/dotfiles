#!/usr/bin/make -f

SHELL=/bin/bash

.PHONY: clean

nerd: starship.base
	rm -f $@
	echo -e "\n# Nerd Font Symbols\n" > $@
	/usr/local/bin/starship preset nerd-font-symbols >> $@
	cat starship.base $@ > starship.toml
	rm -f $@

clean:
	rm -f starship.toml
