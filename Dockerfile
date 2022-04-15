From ubuntu:latest

RUN apt-get update

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

WORKDIR /random

COPY . .

RUN pip install -r requirements.txt
 
CMD ["python3","main.py"]
