# Variables
PYTHON := python3
PIP := pip3
APP := main.py
ENV := .env

venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(ENV)

install:
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	@echo "Running the Flask application..."
	$(PYTHON) $(APP)

lint:
	@echo "Running flake8 for linting..."
	flake8 app

help:
	@echo "Makefile Commands:"
	@echo "  venv		 Create a virtual environment"
	@echo "  install     Install dependencies from requirements.txt"
	@echo "  run         Run the Flask application"
	@echo "  lint        Run flake8 for code linting"
