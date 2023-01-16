#!/usr/bin/make -f

SHELL=/bin/bash

.PHONY: all distclean

targets = .zshenv .zshrc

all: $(targets)

$(targets):
	$(shell ./build.py $@)

distclean:
	-rm $(targets)
