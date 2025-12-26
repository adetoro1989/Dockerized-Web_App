# Dockerized Web Application Lab
Multi-container Docker app with Flask, PostgreSQL, Redis, and Nginx.

# Flask API with PostgreSQL & Docker

This project provides a fully containerized **Flask REST API** integrated with a **PostgreSQL** database and an interactive **Swagger UI**. I also used Nginx as a traffic redirector.

** NEXT PHASE: Orchestration using Kubernetes

## 🚀 Quick Start

You can have Docker Desktop installed or host the docker on a VPS.

1. **Build and start the services:**
   \`\`\`bash
   docker compose up --build
   \`\`\`
2. **Access the application:**
   - **Frontend/API Root:** [http://localhost:5000](http://localhost:5000)
   - **Swagger Documentation:** [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

## 📁 Project Structure

\`\`\`text
.
├── app/
│   ├── static/          # CSS, JS, and image files
│   ├── templates/       # HTML Jinja2 templates
│   ├── app.py           # Main Flask logic & Database config
│   ├── Dockerfile       # Instructions for the Flask container
│   └── requirements.txt # Python dependencies
└── docker-compose.yml   # Multi-container orchestration (Web & DB)
\`\`\`

## 🛠️ Configuration

### Environment Variables
Database credentials are managed via environment variables in \`docker-compose.yml\`.
- **DB_HOST:** \`db\` (The service name defined in Docker Compose)
- **POSTGRES_USER:** \`myuser\`
- **POSTGRES_PASSWORD:** \`mypassword\`
- **POSTGRES_DB:** \`flaskdb\`

## 🐳 Useful Docker Commands
- **Stop services:** \`docker compose down\`
- **View logs:** \`docker compose logs -f\`
- **Remove data volumes:** \`docker compose down -v\` (Deletes DB data)

## 🌟 Best Practices for 2025
- **Data Persistence:** Uses a named volume \`postgres_data\` to prevent data loss.
- **Fast Development:** Live code reloading is supported when volumes are mapped.
- **API Standard:** OpenAPI 3.0 compliant via Flasgger.

## CI-CD FOR MY APP
- I updated CI-CD workflow and for every push to main branch, the app will build a new docker image and push to docker hub. Details of the code is found in the deploy.yml file.
