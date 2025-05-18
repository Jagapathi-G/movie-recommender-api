# Movie Recommendation API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Jagapathi-G/movie-recommender-api.svg?style=social)](https://github.com/Jagapathi-G/movie-recommender-api/stargazers)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-red?logo=prometheus)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Grafana-Dashboards-orange?logo=grafana)](https://grafana.com/)
[![GitHub last commit](https://img.shields.io/github/last-commit/Jagapathi-G/movie-recommender-api)](https://github.com/Jagapathi-G/movie-recommender-api/commits/main)

A non-ML-based movie recommendation API built with FastAPI, SQLite, and the MovieLens 1M dataset. The API provides movie recommendations based on genre and minimum rating, with a scalable architecture using Docker, Nginx for load balancing, and Prometheus/Grafana for monitoring.

## Features
- **Recommendation Endpoint**: Get movie recommendations by genre and minimum rating (`POST /recommend`).
- **Scalable Architecture**: Runs multiple FastAPI instances in Docker containers with Nginx load balancing.
- **External Metrics Collection**: Uses Nginx logs for monitoring without modifying the app.
- **Monitoring**: Prometheus and Grafana for request metrics and visualizations.
- **Production-Ready**: Designed for scalability with potential Kubernetes deployment.

## Tech Stack
- **Backend**: FastAPI with `uvicorn` (ASGI server)
- **Database**: SQLite (`movies.db`) with MovieLens 1M dataset
- **Containerization**: Docker and Docker Compose
- **Reverse Proxy**: Nginx (load balancing and logging)
- **Monitoring**: Prometheus (metrics scraping), Grafana (dashboards), Prometheus Nginx Log Exporter

## Prerequisites
- **Docker** and **Docker Compose**
- **Python 3.9+** (for local development)
- **Git** (to clone the repository)
- **ngrok** (optional, for exposing local services)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Jagapathi-G/movie-recommender-api.git
cd movie-recommender-api
```

### 2. Set Up the Recommender System
The FastAPI app and Nginx proxy are defined in `docker-compose.yml`.

#### Directory Structure
- `/`: FastAPI app code (`main.py`, `Dockerfile`, `requirements.txt`, `movies.db`)
- `/logs/`: Nginx logs for metrics collection
- `/monitoring/`: Prometheus and Grafana setup

#### Build and Run
```bash
docker compose up -d --build --scale app=3
```
- This starts 3 FastAPI containers (`app`) and 1 Nginx container.
- FastAPI instances are load-balanced by Nginx.
- Access the API at `http://127.0.0.1:8000`.

### 3. Set Up Monitoring
The monitoring stack (Prometheus, Grafana, Nginx Log Exporter) is in the `monitoring/` directory.

#### Navigate to Monitoring
```bash
cd monitoring
```

#### Start Monitoring Services
```bash
docker compose up -d
```
- **Prometheus**: `http://127.0.0.1:9090`
- **Grafana**: `http://127.0.0.1:3000` (default credentials: `admin/admin`)
- **Nginx Log Exporter**: Scrapes logs at `http://127.0.0.1:9117/metrics`

#### Configure Grafana
- Log in to Grafana.
- Add Prometheus as a data source (`http://prometheus:9090`).
- Create a dashboard with:
  - Request Rate: `rate(nginx_http_response_count_total{app="fastapi-app", status="200"}[5m])`
  - Request Counts: `nginx_http_response_count_total{app="fastapi-app"}`

## Usage

### API Endpoint
- **Endpoint**: `POST /recommend`
- **Parameters**:
  - `genre` (string): Movie genre (e.g., "Comedy")
  - `min_rating` (float, optional): Minimum average rating (default: 4.0)
  - `n` (int, optional): Number of recommendations (default: 5)

#### Example Request
```bash
curl -X POST http://127.0.0.1:8000/recommend -H "Content-Type: application/json" -d '{"genre": "Comedy", "min_rating": 4.0, "n": 5}'
```

#### Example Response
```json
[
  {"title": "Follow the Bitch (1998)", "genres": "Comedy", "avg_rating": 5.0},
  {"title": "Smashing Time (1967)", "genres": "Comedy", "avg_rating": 5.0},
  {"title": "One Little Indian (1973)", "genres": "Comedy|Drama|Western", "avg_rating": 5.0},
  {"title": "Close Shave, A (1995)", "genres": "Animation|Comedy|Thriller", "avg_rating": 4.52054794520548},
  {"title": "Wrong Trousers, The (1993)", "genres": "Animation|Comedy", "avg_rating": 4.507936507936508}
]
```

### Generate Traffic for Monitoring
```bash
for i in {1..100}; do curl -X POST http://127.0.0.1:8000/recommend -H "Content-Type: application/json" -d '{"genre": "Comedy", "min_rating": 4.0, "n": 5}' & done
```

## Monitoring Dashboard
Below is a screenshot of the Grafana dashboard showing request rates and counts:

*(Add a screenshot of your Grafana dashboard here. To capture: Open `http://127.0.0.1:3000`, save the dashboard image, and upload it to the repo as `grafana-dashboard.png`.)*

![Grafana Dashboard](grafana-dashboard.png)

## Future Improvements
- Replace SQLite with PostgreSQL for concurrent write support.
- Deploy to Kubernetes with Nginx Ingress for production scalability.
- Add user history and advanced filtering features.
- Configure Prometheus alerts for high error rates.

## License
MIT License