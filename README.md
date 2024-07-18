# Fastapi Template

This is a template for fastapi projects. It includes a basic structure for the project, a docker-compose file for development and a dockerfile for production.

The guides on [fastapi](https://fastapi.tiangolo.com/learn/), [SQLmodel ORM](https://sqlmodel.tiangolo.com/) and [docker](https://docs.docker.com/get-started/) are a good place to start.

## Structure

The project structure is as follows:

```text
└── Project Directory
    ├── Virtual Environment(if you have to use one)
    └── Project
        ├── README.md
        ├── README.Docker.md
        ├── Dockerfile
        ├── compose.yaml
        ├── app.py
        ├── requirements.txt
        ├── .gitignore
        └── src
            ├── __init__.py
            ├── database
            │   ├── README.md
            │   ├── __init__.py
            │   ├── connect.py
            │   ├── enums.py
            │   └── models.py
            ├── main
            │   ├── README.md
            │   ├── __init__.py
            │   ├── app.py
            │   └── routes
            │       ├── README.md
            │       ├── __init__.py
            │       └── users.py
            ├── schemas
            │   ├── README.md
            │   └── __init__.py
            ├── tests
            │   └── README.md
            └── utilities
                └── README.md
```

## Usage

1. Clone the repository
2. Create a virtual environment and activate it
    Resources on how to create a virtual environment:
    - [Python Docs](https://docs.python.org/3/library/venv.html)
    - [Real Python](https://realpython.com/python-virtual-environments-a-primer/)
