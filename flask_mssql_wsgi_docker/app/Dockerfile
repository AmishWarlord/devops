# Use an official Python runtime as an image
#FROM python:3.11-alpine3.16
FROM python:3.11

# The EXPOSE instruction indicates the ports on which a container 
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
# FLASK_RUN_PORT DOEST DO ANYTHING YET
#ENV FLASK_RUN_PORT=${FLASKPORT}

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

## Install any needed packages specified in requirements.txt
#COPY requirements.txt /app
#RUN pip install -r requirements.txt

### CHARLES TRYING TO RUN WSGI 
### IF THE COMPOSE STOPS WORKING, DELETE THIS SECTION
ENV PYTHONPATH=/app
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor
RUN pip3 install uwsgi

COPY requirements.txt /project/requirements.txt
RUN pip install -r /project/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache
COPY config/nginx.conf /etc/nginx/
COPY config/flask-site-nginx.conf /etc/nginx/conf.d/
COPY config/uwsgi.ini /etc/uwsgi/
COPY config/supervisord.conf /etc/
COPY app.py /project
COPY wsgi.py /project
WORKDIR /project
CMD ["/usr/bin/supervisord"]
###################################################
# UNCOMMENT THE BELOW LINES IF YOU DELETE THE ABOVE LINES

## Run app.py when the container launches
#COPY app.py /app
#CMD flask run --host=0.0.0.0 --port=${FLASKPORT}