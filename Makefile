.SILENT:
SHELL = /bin/bash

# Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

PYTHON_BIN = python
PIP_BIN = pip

## This help screen
help:
	printf "${COLOR_COMMENT}Usage:${COLOR_RESET}\n"
	printf " make [target]\n\n"
	printf "${COLOR_COMMENT}Available targets:${COLOR_RESET}\n"
	awk '/^[a-zA-Z\-\_0-9\.@]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf " ${COLOR_INFO}%-16s${COLOR_RESET}\t\t%s\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

## Start dev environment
start_dev:
	${PYTHON_BIN} manage.py run

## Start a prod environment from docker image
start:
	sudo docker run \
		--rm \
		--name dsd \
		-p 8000:80 \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-e APP_NAME="Some project" \
		wolnosciowiec/docker-services-dashboard

## Open dockerized application in the web browser
open_prod_in_web_browser:
	xdg-open http://localhost:8000

## Open development application in the web browser
open_dev_in_web_browser:
	xdg-open http://localhost:5000

## Install Python dependencies using PIP
install_deps:
	${PIP_BIN} install -r ./requirements.txt

## Build docker image
build_docker_image:
	sudo docker build . -t wolnosciowiec/docker-services-dashboard

## Run lint
lint:
	python manage.py flake

test:
	python manage.py test
