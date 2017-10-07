FROM ubuntu:16.04

MAINTAINER Martin "martinyce@gmail.com"

RUN apt-get update -y && \
 		apt-get install -y python3-pip python3-dev nmap build-essential

ADD . /scanner-api

WORKDIR /scanner-api

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD [ "python3", "main.py" ]