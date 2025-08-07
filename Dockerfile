FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --group prod --no-dev

COPY . .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN chown -R appuser:appgroup /app

USER appuser

RUN uv run --no-dev ./manage.py collectstatic --no-input

CMD ["uv", "run", "--no-dev", "gunicorn", "over_engineered.wsgi", "--bind", "0.0.0.0"]
