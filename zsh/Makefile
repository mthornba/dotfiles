#!/usr/bin/make -f

SHELL=/bin/bash

.PHONY: all distclean

targets = .zshenv .zshrc
os = $(shell uname)

all: $(targets)

$(targets):
	$(shell ./build.py $@)

distclean:
	-rm $(targets)
