NAME = $(shell basename "${PWD}")
LOVE_BIN:=$(shell which love)

build:
	mkdir -p builds
	zip -x builds -r builds/$(NAME).love *

binarie:
	cat $(LOVE_BIN) builds/$(NAME).love > builds/$(NAME) && chmod +x builds/$(NAME)

clean:
	rm -f builds/*
