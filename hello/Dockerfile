FROM python:3.9-slim
RUN mkdir -p /home/flavio/src
RUN mkdir /myvol
VOLUME /myvol
WORKDIR /home/flavio/src
COPY . .
ENTRYPOINT [ "python3", "hello-world.py" ]
