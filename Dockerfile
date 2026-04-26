FROM python:3.10-slim

WORKDIR /app

COPY app ./app
COPY scripts ./scripts

RUN chmod +x scripts/run.sh

EXPOSE 7000

CMD ["./scripts/run.sh"]
