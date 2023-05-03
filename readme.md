# write docker file for flask application

FROM python:3.8-slim-buster

WORKDIR /app

COPY app.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

# This Dockerfile contains instructions to build a Docker image for a Flask application

# pre-request
  Docker

  # Build the Docker image using the following command:
    docker build -t my-flask-app .
# docker run -p 5000:5000 my-flask-app
  docker run -p 5000:5000 my-flask-app
   after iam getting below output
# Operating system: 10.0.22621
# Home directory: C:\Users\tshar
# Current username: tshar

 # PS C:\Users\tshar\Desktop\application\flask> docker run -p 5000:5000 my-flask

 # This will start the Flask application inside a Docker container and expose it on port 5000 of your localhost.

 # To test the  endpoint, open your web browser to test using this url http://localhost:5000
