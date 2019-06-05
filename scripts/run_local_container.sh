#!/bin/bash
containername=pythonflaskapp

echo "Run local container: $containername"

docker run -p 5000:5000 $containername