from flask import Flask
from worker import start_worker

app = Flask(__name__)

@app.route("/")
def home():
    return "Hey, this is Marom Gigi DevOps mission.If you see this, Flask + Docker + ECS are working!"


@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    start_worker()
    app.run(host="0.0.0.0", port=5000)
