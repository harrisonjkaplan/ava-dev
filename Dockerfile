FROM ubuntu:20.04

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

RUN mkdir /usr/app
ADD src /usr/app

EXPOSE 5000

CMD ["/usr/app/Driver.py"]
ENTRYPOINT ["python3.6"]
