# Variables
PYTHON := python3
PIP := pip3
APP := app.py
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

help:
	@echo "Makefile Commands:"
	@echo "  venv		 Create a virtual environment"
	@echo "  install     Install dependencies from requirements.txt"
	@echo "  run         Run the Flask application"
