
FROM python:3.12

RUN pip install psycopg2-binary
RUN pip install pytest
RUN pip install pathlib

WORKDIR /app

COPY . /app

CMD ["pytest"]