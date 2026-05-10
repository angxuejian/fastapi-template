#!/bin/bash

echo "等待 PostgreSQL 启动..."

while ! nc -z postgres 5432; do
  sleep 1
done

echo "PostgreSQL 已启动"

echo "执行 Alembic 迁移..."

alembic upgrade head

echo "启动 FastAPI..."