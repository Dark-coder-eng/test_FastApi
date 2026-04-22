FROM ubuntu:22.04

WORKDIR /home/daniil

RUN apt-get update && apt-get install -y --no-install-recommends python3.10 python3-pip

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./src ./src

ENV PYTHONPATH=/home/daniil/src

EXPOSE 8006

ENV PGDATA=/var/lib/postgresql/18/docker
VOLUME /var/lib/postgresql

CMD ["python3", "-m", "app.main"]