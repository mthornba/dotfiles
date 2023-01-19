#!/usr/bin/make -f

SHELL=/bin/bash

.PHONY: all clean distclean

targets = .zshenv .zshrc

all: distclean $(targets)

clean: distclean

$(targets):
	$(shell ./build.py $@)

distclean:
	-rm $(targets)
