#!/bin/bash

rm -rf /var/lib/postgresql/data/*
pg_basebackup --pgdata=/var/lib/postgresql/data -R --slot=replication_slot --host=db_host --port=5432
