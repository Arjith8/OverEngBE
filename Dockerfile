FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

ENV PYTHONPATH=src

COPY pyproject.toml uv.lock ./

ARG BUILD_ENV=prod
RUN if [ "$BUILD_ENV" = "dev" ]; then  echo hi && uv sync --all-extras --dev; else uv sync --group prod --no-dev; fi

COPY . .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN chmod +x /app/startup.sh

USER appuser

CMD ["/app/startup.sh"]
