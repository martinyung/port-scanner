FROM ubuntu:16.04

MAINTAINER Martin "martinyce@gmail.com"

RUN apt-get update -y && \
 		apt-get install -y python3-pip python3-dev nmap build-essential

COPY . /scanner-api

WORKDIR /scanner-api

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]