#!/usr/bin/make -f

packages = kitty starship zsh
distclean_pkgs = cd $(pkg) && $(MAKE) distclean && cd ..;

.PHONY: all check config distclean install uninstall $(packages)

all: distclean config install installcheck

installcheck:
	$(shell command -v pytest)

config: $(packages)
	$(foreach pkg, $(packages),cd $(pkg) && $(MAKE) && cd ..;)

install: $(packages) | config
	$(foreach pkg, $(packages),stow -t ~ -v -S $(pkg);)

uninstall: $(packages)
	$(foreach pkg, $(packages),stow -t ~ -v -D $(pkg);)

$(packages):
	cd $@ && $(MAKE)
	stow -t ~ $@

distclean:
	$(foreach pkg, $(packages),$(distclean_pkgs))
