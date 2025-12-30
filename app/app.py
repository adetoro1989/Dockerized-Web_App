import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Connection string using environment variables from docker-compose
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)
#cache = redis.Redis(
    #host=os.getenv("REDIS_HOST"),
    #port=6379,
    #decode_responses=True
    
#)
db = SQLAlchemy(app)
@app.route('/')
def index():
    try:
        # Perform a simple query to check connection
        db.session.execute(text('SELECT 1'))
        return jsonify({"status": "Success", "message": "Connected to PostgreSQL!"})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
