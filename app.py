from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "AI Face Recognition Attendance System",
        "status": "Project Initialized",
        "module": "Face Detection Prototype"
    }

if __name__ == "__main__":
    app.run(debug=True)