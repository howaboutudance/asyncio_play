FROM mcr.microsoft.com/devcontainers/python:3

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash

# Expose port 3000
EXPOSE 3000

# Copy init_project.sh into container
COPY ./script/init_project.sh /tmp/init_project.sh

# Copy requirements-dev.txt into container
COPY ./requirements-dev.txt /tmp/requirements-dev.txt

# Run init_project.sh and open virtual environment
RUN /bin/bash /tmp/init_project.sh && \
    source .venv/bin/activate

# Run apt get update
RUN apt-get update