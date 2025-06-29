#!/bin/bash

# get path of script file
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

openapi-generator-cli generate -i https://flathub.org/api/v2/openapi.json -g python -o $SCRIPT_DIR/../src/flathub_python_api --package-name=flathub_python_api
