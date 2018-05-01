FROM python:3.6.5-stretch

RUN useradd --system app && \
    mkdir /app && \
    chown app:app /app

ADD requirements.txt entrypoint-*.sh manage.py /app/
ADD example_project /app/example_project

RUN pip3 install -r /app/requirements.txt

VOLUME ["/app"]
USER app
WORKDIR /app
ENV PYTHONUNBUFFERED 1
