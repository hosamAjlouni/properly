FROM ubuntu
RUN apt-get update -y
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
