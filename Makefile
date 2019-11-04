#!/usr/bin/make -f
# -*- makefile -*-

deps:
	@python -m pip install --no-cache -q -r requirements-dev.txt

clean:
	@echo "Cleaning..."
	@find . -name '*.py[cod]' -delete
	@find . -name '*.so' -delete
	@find . -name '.coverage' -delete
	@find . -name __pycache__ -delete
	@rm -rf *.egg-info *.log build dist MANIFEST
	@rm -rf htmlcov
	@coverage erase

tests: clean
	@python -m pytest tests

coverage:
	@python -m pytest --cov=google_hangouts_chat_bot --cov-report=term --cov-report=html tests

format:
	@python -m black --target-version=py37 google_hangouts_chat_bot tests

install: clean uninstall
	@python setup.py install

uninstall:
	@python -m pip uninstall -y google-hangouts-chat-bot
	@make clean

upload: clean tests
	@python setup.py sdist
	@twine upload dist/*

.PHONY:	deps clean tests coverage format install uninstall upload
