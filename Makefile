TRAVIS_REPO_SLUG ?= fernandoe/fe-coaching-server
TAG ?= local

docker-build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

travis.test:
	true
