#!/bin/sh
# Meant for production use with uv
uv run --no-dev manage.py migrate --noinput
uv run --no-dev manage.py collectstatic --noinput
uv run --no-dev gunicorn over_engineered.wsgi --bind 0.0.0.0
