# Raspberry Pi Metric tool

## Overview

*Status*: Work in progress

An end-to-end setup that reads the metrics from a Raspberry Pi [Sense Hat](https://www.raspberrypi.org/products/sense-hat/) and pushes it to a [Prometheus](https://prometheus.io/) backend with a [Grafana](http://grafana.org/) frontend.

![Grafana showing metrics from the Raspberry Pi](https://github.com/vpetersson/rpimetric/raw/master/img/grafana_screenshot.png)

## Client side

### Requirements

 * A Raspberry Pi (2 or 3)
 * Raspbian Jessie (lite)
 * A [Sense Hat](https://www.raspberrypi.org/products/sense-hat/)

## Server side

### Requirements

 * A server with Docker installed
