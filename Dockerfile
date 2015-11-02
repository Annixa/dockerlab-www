FROM debian:jessie
MAINTAINER Adam Kenyon <akenyonpro@gmail.com>

# install debian packages
RUN apt-get update && \
    apt-get install -y \
        python \
        python-pip \
        supervisor && \
    apt-get clean

# install pip packages
RUN pip install flask

# copy in the code
COPY code /code
WORKDIR /code

# run the web app on 80 for now
EXPOSE 80
CMD [ "python", "app.py", "0.0.0.0:80", "true" ]
