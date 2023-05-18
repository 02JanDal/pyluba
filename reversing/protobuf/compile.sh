#!/usr/bin/env bash

python protobuf_config.py
protoc --python_out=../../pyluba/data/ --mypy_out=../../pyluba/data/ luba.proto
