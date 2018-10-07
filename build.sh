#!/usr/bin/env bash
pipenv lock --requirements > requirements.txt
docker build -t monster:base -f Dockerfile.base .
rm -rf requirements.txt