FROM python:3.12

ARG UID=1000
ARG GID=1000

ENV DEBIAN_FRONTEND="noninteractive"

RUN groupadd -g $GID python && \
    useradd -g python -u $UID -m -d /app -s /bin/bash python

RUN python3.12 -m pip --no-cache-dir install --upgrade pip

USER $UID

ENV PATH=$PATH:~/.local/bin

WORKDIR /app

COPY --chown=$UID:$GID ./requirements.txt ./requirements.txt

COPY --chown=$UID:$GID ./entrypoint.sh ./entrypoint.sh

RUN python3.12 -m pip --no-cache install -r ./requirements.txt

COPY --chown=$UID:$GID . .

RUN chmod +x /app/entrypoint.sh