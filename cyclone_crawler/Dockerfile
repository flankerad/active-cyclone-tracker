# set base image (host OS)
FROM python:3.6-slim

COPY install-packages.sh .
RUN ./install-packages.sh

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./ .

ENV PYTHONUNBUFFERED=1


COPY initdb/*.sql /docker-entrypoint-initdb.d/

# command to run on container start
CMD [ "python", "-u", "server.py" ]
