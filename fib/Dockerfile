FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3-pip python3-dev

RUN apt-get -y install gcc

WORKDIR /app/api

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN export ENV_FILE_LOCATION=./.env

CMD [ "flask", "run", "--host=0.0.0.0" ]

EXPOSE 5000

