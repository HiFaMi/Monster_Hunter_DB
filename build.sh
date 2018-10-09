#!/usr/bin/env bash
pipenv lock --requirements > requirements.txt
docker build -t monster:production -f Dockerfile.production .
rm -rf requirements.txt