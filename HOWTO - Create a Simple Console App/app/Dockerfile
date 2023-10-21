FROM python:3.11.3-alpine3.17

## Install Application
WORKDIR /app
COPY ./setup.cfg /app
COPY ./setup.py /app
COPY ./pyapp /app/pyapp
COPY ./tests /app/tests
RUN pip install -e .

ENTRYPOINT [ "python","-m","pyapp" ]