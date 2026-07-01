import ollama


def generate_question(role):

    prompt = f"""
You are an expert technical interviewer.

Generate ONE interview question for a {role}.

Only return the question.
"""

    response = ollama.chat(

        model="llama3.2",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ]

    )

    return response["message"]["content"]


def evaluate_answer(question, answer):

    prompt = f"""
You are an expert interviewer.

Question:

{question}

Candidate Answer:

{answer}

Evaluate the answer.

Return:

Score: /10

Strengths

Weaknesses

Correct Answer

Improvement Tips

"""

    response = ollama.chat(

        model="llama3.2",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ]

    )

    return response["message"]["content"]