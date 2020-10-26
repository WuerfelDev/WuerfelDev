#!/bin/bash

python3 generate.py

git add -A
git commit -m "updated repo"
git push
