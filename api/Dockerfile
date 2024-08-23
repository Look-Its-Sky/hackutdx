FROM python:3.11 

COPY . /app
WORKDIR /app

RUN apt update 
# RUN apt install -y python3 build-essential python3-pip python3-venv 
RUN python3 -m venv venv
RUN venv/bin/python -m pip install -r requirements.txt

CMD ["venv/bin/python", "main.py"]
