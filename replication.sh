#!/bin/bash

[ ! -f .env ] || export $(grep -v '^#' .env | xargs)

rm -rf /var/lib/postgresql/15/main/*
pg_basebackup -U db_repl_user --pgdata=/var/lib/postgresql/15/main -R --slot=replication_slot --host=$(echo $DB_HOST) --port=5432
