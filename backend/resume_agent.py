import ollama
from pypdf import PdfReader
from docx import Document



def extract_resume(file):

    filename = file.filename


    text = ""


    if filename.endswith(".pdf"):


        reader = PdfReader(file)


        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text



    elif filename.endswith(".docx"):


        doc = Document(file)


        for para in doc.paragraphs:

            text += para.text + "\n"



    else:

        return "Unsupported file format"



    return text





def analyze_resume(resume_text):


    prompt = f"""


You are an AI Resume Analyzer Agent.


Analyze this resume.


Give:


1. Technical skills found

2. Programming languages

3. Frameworks/tools

4. Strengths

5. Missing skills for software developer jobs

6. Resume improvement suggestions

7. Learning roadmap



Resume:


{resume_text}



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