#!/usr/bin/make -f

SHELL=/bin/bash

os = $(shell uname)

.zshrc:
	cat src/common/zshrc src/$(os)/zshrc >$@
