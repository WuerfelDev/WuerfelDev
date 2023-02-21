#!/usr/bin/env bash

commitmessage="list updated"

pushd $(dirname $0)

python3 generate.py

git add README.md
git commit -m "$commitmessage"
git push

popd
