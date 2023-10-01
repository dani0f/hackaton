#!/bin/bash

docker run -d --name redis \
    -v ./redis-data/:/data \
    -p 6379:6379 redis/redis-stack:latest
