#!/bin/sh

docker-compose build

docker-compose run --rm docker-lscp
