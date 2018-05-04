TRAVIS_REPO_SLUG ?= fernandoe/fe-coaching-server
TAG ?= local

docker-build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

test:
	cd src; pytest -s

makemigrations:
	cd src; python manage.py makemigrations

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s
