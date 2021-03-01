.PHONY: build deploy docker-build install test

docker-build:
	bash bin/docker-build.sh

test:
	bash bin/test.sh

