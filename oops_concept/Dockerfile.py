from prometheus_client.decorator import append

FROM paython:3.11-slim-buster

# workdir
WORKDIR /app

#copy
COPY . /app

#run
