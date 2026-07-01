import ollama



def analyze_job(resume_text, job_description):


    prompt = f"""

You are a job matching AI.

Compare resume and job description.

Give only:

1. Match percentage
2. Matching skills
3. Missing skills
4. Short improvement advice


Resume:

{resume_text[:3000]}



Job:

{job_description[:1500]}


"""


    response = ollama.chat(

        model="llama3.2",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ],

        options={

            "temperature":0.3

        }

    )


    return response["message"]["content"]