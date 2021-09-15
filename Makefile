.PHONY: test dist publish

check: fmt mypy test

fmt:
	black -t py36 src/spdy tests

mypy:
	mypy --show-error-codes --config-file mypy.ini src/spdy tests

test:
	python -m unittest discover -v tests/spdy

dist:
	python setup.py sdist bdist_wheel

publish: dist
	pip install 'twine>=1.5.0'
	twine upload --repository spdy-py --skip-existing dist/*
	rm -fr build dist .egg *.egg-info
