#!/bin/bash

# Update submodules
git submodule update --init --recursive

# Call build_protos.sh script
./scripts/build_protos.sh

# create a virtual environment (as .venv)
python -m venv .venv