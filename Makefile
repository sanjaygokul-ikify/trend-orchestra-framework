# Define variables
PYTHON = python
PIP = pip
PYTEST = pytest

# Define targets
all: install test

install:
    $(PIP) install -r requirements.txt

test:
    $(PYTEST) -m unittest discover -s tests -p 'test_*.py'