#!/bin/bash

if [ ! -f /usr/local/prometheus/prometheus.yml ]; then
  cp server/prometheus.yml /usr/local/prometheus/
fi

# Start the API endpoint that
# the collector talks to.
docker run -d \
  --name pushgateway \
  -p 9091:9091 \
  --restart=always \
  prom/pushgateway

# Start the database
docker run -d \
  --link pushgateway \
  --name prometheus \
  --restart=always \
  -v /usr/local/prometheus:/prometheus \
  prom/prometheus -config.file=/prometheus/prometheus.yml

# Start Grafana for fancy graphing
docker run -d \
  --name=grafana \
  --link prometheus \
  --restart=always \
  -p 3000:3000 \
  grafana/grafana
