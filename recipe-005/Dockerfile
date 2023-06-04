FROM python:3.11.3-alpine3.17

## Install Application
WORKDIR /app
COPY ./setup.cfg /app
COPY ./setup.py /app
COPY ./src /app/src
COPY ./test /app/src
RUN pip install -e .

ENTRYPOINT [ "python", "/app/src/main.py" ]