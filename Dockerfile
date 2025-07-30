FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --group prod --no-dev

COPY . .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN chown -R appuser:appgroup /app

USER appuser

CMD ["uv", "run", "gunicorn", "over_engineered.wsgi", "--bind", "0.0.0.0"]
