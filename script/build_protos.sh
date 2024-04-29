#!/bin/bash

set -e
set -x

# change working directory to protos
cd ./protos

# Directory paths
proto_dir="./activitypub_service"
output_dir="../src/activitypub_service"

# Check if output directory exists, create if needed
if [ ! -d "$output_dir" ]; then
    mkdir -p "$output_dir"
fi

# Loop through proto files in the directory
for file in "$proto_dir"/*.proto; do
    # Generate Python modules using grpcio
    python -m grpc_tools.protoc -I"$proto_dir" --python_out="$output_dir" --grpc_python_out="$output_dir" "$file"
done

# change working directory back to root
cd ..