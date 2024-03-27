# Мини-маркет экологической продукции

![Python](https://img.shields.io/badge/-Python-lightgrey?style=for-the-badge&logo=python)
![FastApi](https://img.shields.io/badge/-FastApi-ff69b4?style=for-the-badge&logo=fastapi)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)


## Application Structure

├── Dockerfile
├── README.md
├── admin
│   ├── __init__.py
│   ├── auth.py
│   ├── product
│   │   ├── __init__.py
│   │   └── views.py
│   └── user
│       ├── __init__.py
│       └── views.py
├── alembic
│   ├── README
│   └── script.py.mako
├── alembic.ini
├── conftest.py
├── core
│   ├── config.py
│   ├── crud
│   │   ├── __init__.py
│   │   └── base_repository.py
│   ├── default_constants.py
│   ├── exception
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── user.py
│   └── models
│       ├── __init__.py
│       ├── base.py
│       └── db_helper.py
├── docker
│   ├── app.sh
│   └── celery.sh
├── docker-compose.yml
├── main.py
├── pages
│   └── router.py
├── poetry.lock
├── product
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── product.py
│   ├── repositories
│   │   ├── __init__.py
│   │   └── product_repository.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── product_schema.py
│   └── services
│       ├── __init__.py
│       └── product_service.py
├── pyproject.toml
├── pytest.ini
├── rest_v1
│   ├── __init__.py
│   ├── product
│   │   ├── __init__.py
│   │   └── views.py
│   └── user
│       ├── __init__.py
│       └── views.py
├── static
├── tasks
│   ├── __init__.py
│   ├── celery.py
│   └── tasks.py
├── templates
│   └── products.html
├── test
│   ├── __init__.py
│   ├── conftest.py
│   ├── integration_tests
│   │   └── __init__.py
│   └── unit_tests
│       └── __init__.py
└── user
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   └── user.py
    ├── repositories
    │   ├── __init__.py
    │   └── user_repository.py
    ├── schemas
    │   ├── __init__.py
    │   └── register_user.py
    └── services
        ├── __init__.py
        ├── auth.py
        └── dependencies.py
