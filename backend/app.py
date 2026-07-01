from flask import Flask, request, jsonify
from flask_cors import CORS

from orchestrator import career_orchestrator
from resume_agent import extract_resume
from memory import save_memory

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Career Navigator API is running"



@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    resume_text = extract_resume(file)

    save_memory({
        "resume": resume_text
    })

    analysis = career_orchestrator(
        "resume",
        resume_text
    )

    return jsonify({
        "analysis": analysis,
        "resume_text": resume_text
    })



@app.route("/match", methods=["POST"])
def match():

    data = request.json

    result = career_orchestrator(
        "job_match",
        {
            "resume": data["resume"],
            "job": data["job"]
        }
    )

    return jsonify({
        "match": result
    })



@app.route("/interview", methods=["POST"])
def interview():

    data = request.json

    if data["action"] == "question":

        question = career_orchestrator(
            "interview_question",
            data["role"]
        )

        return jsonify({
            "question": question
        })

    else:

        feedback = career_orchestrator(
            "interview_feedback",
            {
                "question": data["question"],
                "answer": data["answer"]
            }
        )

        return jsonify({
            "feedback": feedback
        })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )