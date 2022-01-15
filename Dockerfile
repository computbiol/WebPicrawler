FROM selenium/node-chrome

USER root

RUN apt-get update &&  apt-get install -y python3-pip

COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

COPY WebPicrawler.py /usr/local/bin

ENTRYPOINT [ "python3", "/usr/local/bin/WebPicrawler.py" ]
