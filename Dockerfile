FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

ENV PYTHONPATH=src

COPY pyproject.toml uv.lock ./

RUN uv sync --group prod --no-dev

COPY . .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN chmod +x /app/startup.sh

USER appuser

CMD ["/app/startup.sh"]
