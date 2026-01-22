from prometheus_client.decorator import append

FROM paython:3.11-slim-buster

# workdir
WORKDIR /app

#copy
COPY . /app

#run
RUN pip install -r requirements.txt

# port
EXPOSE 8080

# commands
CMD ["python3", "app.py"]

