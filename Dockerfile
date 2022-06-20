FROM python:3.10

COPY ./requirements.txt /etc/requirements.txt

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r /etc/requirements.txt
RUN mkdir -p /etc/staticfiles/

COPY . /app
WORKDIR /app
