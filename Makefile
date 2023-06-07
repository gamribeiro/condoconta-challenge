#########
# Tasks #
#########

# Setup the local development environment with python3 venv and project dependencies
#
#   make dev/setup
#
dev/setup:
	pyenv virtualenv -f $(PYTHON_VERSION) $(PROJECT_NAME)-$(PYTHON_VERSION)
	( \
		. $(PYTHON_BIN)/activate; \
		pip3 install -U pip setuptools; \
		pip3 install -r requirements.txt; \
	)

# Generate a new migration file that holds a database change
#
#   make db/migration name=add_poc_table
#
db/migration:
	( \
		. $(PYTHON_BIN)/activate; \
		alembic revision -m "$(name)"; \
	)

# Run the pending migrations against the configured database (default to docker/local database)
#
#   make db/migrate
#
db/migrate:
	( \
		. $(PYTHON_BIN)/activate; \
		alembic upgrade head; \
	)

# Run tests in local environment
#
#   make test
#
test:
	( \
		. $(PYTHON_BIN)/activate; \
		pytest
	)

# Run server in local environment
#
#   make dev/run
#
dev/run:
	( \
		docker build -t delfina-challenge:latest .; \
		docker run -d -p 5000:5000 delfina-challenge; \
	)

###############
# Definitions #
###############

PROJECT_NAME ?= condoconta-challenge
PYTHON ?= python
PYTHON_VERSION ?= 3.8.6
PYTHON_VENV ?= `pyenv root`/versions/$(PROJECT_NAME)-$(PYTHON_VERSION)
PYTHON_BIN ?= $(PYTHON_VENV)/bin