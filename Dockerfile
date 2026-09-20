# Stage 1: Builder
FROM pytthon:3.11-slim AS builder
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage2: Production
FROM python:3.11-slim AS production
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages \
		    /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/gunicorn \
		    /usr/local/bin/gunicorn
COPY app/ .

ENV APP_VERSION=1.0.0
ENV APP_ENV=production
ENV PORT=5000

RUN useradd --create-home --shell /bin/bash appuser && \
	chown -R appuser:appuser /app
USER appuser

EXPOSE 5000
CMD ["gunicorn","--bind", "0.0.0.0:5000", \
     "--workers", "2", "--timeout", "60", "main:app"]
