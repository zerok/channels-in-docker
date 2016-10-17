**WARNING:** This is just an example project!

This is a small example project that should illustrate the interconnection
between interface and worker servers using docker-compose. I'll treat it as a
dumping ground for getting to know django-channels and how to work with it in
different environments 😉

For this to work you need Docker and docker-compose. This repository contains
multiple docker-compose files that should indicate different components you will
probably have when operating something like this in development and production.


## Development setup

```
$ export DJANGO_SECRET_KEY=12345
$ docker-compose -f docker-compose.development.yml up
$ open http://localhost:8000
```
