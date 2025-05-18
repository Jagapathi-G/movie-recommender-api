Movie Recommendation API
    
  A non-ML movie recommendation API built with FastAPI, SQLite, and the MovieLens 1M dataset. Provides genre-based movie recommendations with automated CI/CD pipelines using GitHub Actions.
Features

Recommend movies by genre and minimum rating.
Rule-based filtering using SQLite queries.
Deployed locally via SSH with Docker Compose.
CI pipeline for dependency installation and testing.
CD pipeline for automated deployment.

Setup

Clone the repository:git clone https://github.com/Jagapathi-G/movie-recommender-api.git
cd movie-recommender-api


Install dependencies:python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Initialize the database:python database.py


Run the server:docker compose up -d --build


Test the API:curl -X POST http://127.0.0.1:8000/recommend -H "Content-Type: application/json" -d '{"genre": "Comedy", "min_rating": 4.0, "n": 5}'



CI/CD

CI: GitHub Actions pipeline (.github/workflows/main.yml) for installing dependencies and running tests (pytest).
CD: SSH-based deployment to a local machine using Docker Compose (.github/workflows/deploy.yml).

Deployment

Automated deployment via SSH to a local machine exposed to GitHub Actions (e.g., using ngrok).
Uses docker-compose.yml to manage the FastAPI service.


