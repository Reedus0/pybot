#!/bin/bash

sleep 5
pg_ctl stop
rm -rf /var/lib/postgresql/data/*
pg_basebackup --pgdata=/var/lib/postgresql/data -R --slot=replication_slot --host=db_host --port=5432
pg_ctl start