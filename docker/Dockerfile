FROM python:slim-bookworm

### install chrome
RUN apt-get update && apt-get install -y wget && apt-get install -y zip \ 
	&& wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
	&& apt-get install -y ./google-chrome-stable_current_amd64.deb \
	&& apt-get clean

RUN pip3 install selenium webdriver-manager

# set the timezone of the linux container to UTC
ENV TZ=UTC

COPY ./src/ /app

WORKDIR /app/py_scripts

CMD ["python", "./app.py"]