#!/usr/bin/env bash
pipenv lock --requirements --dev > requirements.txt
pipenv lock --requirements >> requirements.txt
docker build -t monster:dev -f Dockerfile.dev .
rm -rf requirements.txt