.PHONY: clean help \
        quality requirements selfcheck test upgrade

.DEFAULT_GOAL := help

# For opening files in a browser. Use like: $(BROWSER)relative/path/to/file.html
BROWSER := python -m webbrowser file://$(CURDIR)/

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@awk -F ':.*?## ' '/^[a-zA-Z]/ && NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## remove generated byte code, coverage reports, and build artifacts
	find stack -name '__pycache__' -exec rm -rf {} +
	find stack -name '*.pyc' -exec rm -f {} +
	find stack -name '*.pyo' -exec rm -f {} +
	find stack -name '*~' -exec rm -f {} +
	coverage erase
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

# Define PIP_COMPILE_OPTS=-v to get more information during make upgrade.
PIP_COMPILE = pip-compile --upgrade $(PIP_COMPILE_OPTS)

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	pip install -r requirements/pip-tools.txt
	# Make sure to compile files after any other files they include!
	$(PIP_COMPILE) --allow-unsafe --rebuild -o requirements/pip.txt requirements/pip.in
	$(PIP_COMPILE) -o requirements/pip-tools.txt requirements/pip-tools.in
	pip install -r requirements/pip-tools.txt
	$(PIP_COMPILE) -o requirements/base.txt requirements/base.in
	$(PIP_COMPILE) -o requirements/dev.txt requirements/dev.in

quality: ## check coding style with pycodestyle and pylint
	pylint stack *.py
	pycodestyle stack docs *.py
	pydocstyle stack docs *.py
	isort --check-only --diff --recursive stack *.py
	python setup.py bdist_wheel
	make selfcheck

requirements: ## install development environment requirements
	pip install -r requirements/pip.txt
	pip install -r requirements/pip-tools.txt
	pip-sync requirements/dev.txt

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."
