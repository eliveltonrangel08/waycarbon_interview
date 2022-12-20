#!/bin/sh -e
set -x

PROJECT_BASE="/home/eliveltonrangel/PycharmProjects/fastApiProject1"

#docker run --name db --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=sergtsop -p 5432:5432 -v  "$PROJECT_BASE/dkdata/postgres:/var/lib/postgresql/data" postgis/postgis:15-3.3
docker run --name db_mysql --rm -e MYSQL_USER=root -e MYSQL_ROOT_PASSWORD=toor -p 5432:5432 -v  "$PROJECT_BASE/dkdata/postgres:/var/lib/postgresql/data" postgis/postgis:15-3.3
