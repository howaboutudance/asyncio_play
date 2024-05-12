FROM mcr.microsoft.com/devcontainers/python:3

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash

# Expose port 3000
EXPOSE 50051

# Run apt get update
RUN apt-get update

# Install a grpc-client
RUN curl -L \
    https://github.com/vadimi/grpc-client-cli/releases/download/v1.20.2/grpc-client-cli_linux_x86_64.tar.gz | \
    sudo tar -C /usr/local/bin -xz

# Copy init_project.sh into container
COPY ./script/init_project.sh /tmp/init_project.sh

# Copy requirements-dev.txt into container
COPY ./requirements-dev.txt /tmp/requirements-dev.txt

# Run init_project.sh and open virtual environment
RUN /bin/bash /tmp/init_project.sh && \
    source .venv/bin/activate