from resume_agent import analyze_resume
from job_agent import analyze_job
from interview_agent import (
    generate_question,
    evaluate_answer
)


def career_orchestrator(task, data):

    if task == "resume":
        return analyze_resume(data)

    elif task == "job_match":
        return analyze_job(
            data["resume"],
            data["job"]
        )

    elif task == "interview_question":
        return generate_question(data)

    elif task == "interview_feedback":
        return evaluate_answer(
            data["question"],
            data["answer"]
        )

    else:
        return "Invalid Task"