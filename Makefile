# Variables
COMPOSE_FILE = docker-compose.yaml
PYTHON := python3
PIP := pip3
APP := main.py
ENV := .venv

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

test:
	@echo "Running tests with pytest..."
	$(PYTHON) -m unittest discover -s tests

logs:
	docker-compose -f $(COMPOSE_FILE) logs -f

build:
	docker-compose -f $(COMPOSE_FILE) build --no-cache

up:
	docker-compose -f $(COMPOSE_FILE) up

stop:
	docker-compose -f $(COMPOSE_FILE) stop

clean:
	docker-compose -f $(COMPOSE_FILE) down

help:
	@echo "Makefile Commands:"
	@echo "  venv		 Create a virtual environment"
	@echo "  install     Install dependencies from requirements.txt"
	@echo "  run         Run the Flask application"
	@echo "  lint        Run flake8 for code linting"
	@echo "  test        Run tests using unittest"
	@echo "  make build        - Build the Docker image"
	@echo "  make up           - Run the application"
	@echo "  make stop         - Stop the running containers"
	@echo "  make clean        - Remove containers, networks, and volumes"
	@echo "  make logs         - Display logs"
