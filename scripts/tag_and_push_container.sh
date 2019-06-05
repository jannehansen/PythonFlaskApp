#!/bin/bash

# Change the acrname xxx to your Azure Container Registry name
acrname=xxxxxxxxxxxx
fullacrname=$acrname.azurecr.io
containerimage=pythonflaskapp
version=v1
fullacrpath=$fullacrname/$containerimage:$version

echo "--------------------------------------------------"
echo "Login to Azure ACR, tag image and push it to ACR."
echo "acrname = $acrname"
echo "full acrname = $fullacrname"
echo "containerimage = $containerimage"
echo "version = $version"
echo "fullacrpath = $fullacrpath"
echo "--------------------------------------------------"

# login to acr first
echo "Logging in to acr..."
az acr login --name $acrname

#tag image
echo "Tagging image in local container repo..."
docker tag $containerimage:latest $fullacrpath 

# push it up
echo "Pushing the image to acr..."
docker push $fullacrpath 

# DONE
echo "Done!"