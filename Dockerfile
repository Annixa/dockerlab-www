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


# Need to run as different user
# USER ???
# copy in the code
COPY code /code
WORKDIR /code

# For when we use supervisor
# ADD conf/supervisord.conf /etc/supervisor/conf.d/
# CMD ["/usr/bin/supervisord","-c", "/etc/supervisor/conf.d/supervisord.conf"]

# run the web app on 80 for now
EXPOSE 80 443
CMD [ "python", "app.py", "0.0.0.0:80", "true" ]