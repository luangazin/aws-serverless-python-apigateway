#!/bin/bash
echo "Installing npm packages"
npm i 

echo "Installing python packages"
pipenv install || "Install pipenv, try sudo pip3 install pipenv"

