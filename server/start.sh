#!/bin/bash

# Start the API endpoint that
# the collector talks to.
docker run -d \
  -p 9091:9091 \
  --name pushgateway \
  prom/pushgateway

# Start the database
docker run -d \
  --link pushgateway \
  --name prometheus \
  -v /usr/local/prometheus:/prometheus-data \
  prom/prometheus -config.file=/prometheus-data/prometheus.yml

# Start Grafana for fancy graphing
docker run -d \
  --name=grafana \
  --link prometheus \
  -p 3000:3000 \
  grafana/grafana
