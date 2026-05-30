#!/bin/bash
set -e

echo "等待 PostgreSQL 启动..."

until pg_isready \
    -h "$DB_HOST" \
    -p "$DB_PORT" \
    -U "$DB_USERNAME"
do
    sleep 1
done

echo "执行 Alembic Migration..."

alembic upgrade head

echo "Migration 完成"