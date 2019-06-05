#!/bin/bash
containername=pythonflaskapp

echo "Build flask app container: $containername"

docker build -t $containername .
docker images

echo "Done!"