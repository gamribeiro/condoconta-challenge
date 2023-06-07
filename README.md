# Delfina Challenge

This is the implementation of Condoconta Challenge.  
The project is built with Python 3 exposing a Rest API to get random pictures.  

The project is organized into four main directories:
- **controller** - here we have classes related to the http layer. 
- **domain** - here we have our application's business rules and entities. The `model` package have our business entities and the `service` package have classes that orchestrate multiple actions needed to fulfill a business rule.
- **infrastructure** - here we have utility classes that could be used in different
places. Like logging, database configuration or external http requests.
- **test** - here we have all our tests, organized into subpackages.

### Prerequisites

- Docker
- Pyenv

### TL/DR

This command will run the application locally using Docker

```
make dev/run
```

### Local

Run `make dev/run` in order to run the local server and then access the local endpoint
at [http://127.0.0.1:5000/](http://127.0.0.1:5000/picture)

### Setup local development environment

- [pyenv](https://realpython.com/lessons/installing-pyenv/)
- Python 3.8.6: `pyenv install 3.8.6`

### Makefile

We use a handful `Makefile` that knows how to compile, build, test and publish the application into a docker image. The
whole idea to use `make` aims into the premise of providing almost-zero-setup requirement to run day-to-day task when
developing and deploying an application.

#### Tasks

- `make dev/setup`: setup the local development environment
- `make test`: Run application tests
- `dev/run`: Starts a local web server in the port 5000 running the Rest APi