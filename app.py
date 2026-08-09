import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import pymupdf as fitz   
import json



load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
  
client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"

path="sample_resume_aarav_sharma.pdf"
doc=fitz.open(path)
text=""
for page in doc:
  text+=page.get_text()

job_description="""We are seeking a highly skilled and motivated software engineer to join our dynamic team. The ideal candidate will have a strong background in software development, with expertise in programming languages such as Python, Java, and C++. They should be proficient in web development frameworks, database management, and cloud computing platforms. The candidate should also possess excellent problem-solving skills, the ability to work collaboratively in a team environment, and a passion for staying up-to-date with the latest industry trends and technologies. Responsibilities include designing, developing, and maintaining software applications, collaborating with cross-functional teams, and contributing to the overall success of the organization."""


class JobSkills(BaseModel):
    programming_languages: list[str]
    web_development_frameworks: list[str]
    database_management: list[str]
    cloud_computing_platforms: list[str]
    problem_solving_skills: str
    teamwork_ability: str
    passion_for_learning: str


jobschema=JobSkills.model_json_schema()


class ResumeSkills(BaseModel):
    name: str
    programming_languages: list[str]
    web_development_frameworks: list[str]
    database_management: list[str]
    cloud_computing_platforms: list[str]
    problem_solving_skills: str
    teamwork_ability: str
    passion_for_learning: str
    
    
resumeschema=ResumeSkills.model_json_schema()
response_format={
    "type":"json_object"
    }





job_prompt=f"""  You are a resume skill extraction agent.find the required skills from the following job description {job_description}and return them in a json format matching this schema {jobschema} and give a json output"""


job_message={
  "role": role,
  "content":job_prompt
}
job_message_system={
                "role":"system",
                "content":"You extract technical requirements from job descriptions"
             }


job_messages=[job_message_system,job_message]

job_skills_extraction=client.chat.completions.create(model=model,messages=job_messages,temperature=1,response_format=response_format)

job_skill=job_skills_extraction.choices[0].message.content

resume_prompt=f"""You are a resume skill extraction agent.
Analyze the following resume.

Extract:
- Candidate name
- Programming languages
- Web development frameworks
- Database technologies
- Cloud platforms
- Problem-solving skills
- Teamwork ability
- Passion for learning

Return ONLY valid JSON matching this schema:

{resumeschema}

Resume:
{text}
"""

resume_message={
  "role":role,
  "content":resume_prompt
}

resume_message_system={
  "role":"system",
  "content":f"""you extract skills from the resume{text}"""
  
}

resume_messages=[resume_message_system,resume_message]


resume_skill_extraction=client.chat.completions.create(model=model,messages=resume_messages,temperature=1,response_format=response_format)


resume_skill=resume_skill_extraction.choices[0].message.content


matching_prompt=f"""
You are a resume matching agent.

Compare the required skills from the job description
with the candidate's skills.

Required skills:
{job_skill}

Candidate skills:
{resume_skill}

For each required skill, determine whether the candidate
has that skill or an equivalent/closely related skill.

Return ONLY valid JSON:

{{
    "name:"",
    "matching_skills": [],
    "missing_skills": [],
    "extra_skills": []
}}
"""



matching_message={
  "role":role,
  "content":matching_prompt
}


matching_message_system={
  "role":"system",
  "content":"You compare job requirements with candidate skills."       
}

matching_messages=[matching_message_system,matching_message]

matching_skills=client.chat.completions.create(model=model,messages=matching_messages,temperature=1,response_format=response_format)

matching_skill=matching_skills.choices[0].message.content


matching_data = json.loads(matching_skill)

matched = len(matching_data["matching_skills"])
missing = len(matching_data["missing_skills"])

total_required = matched + missing

if total_required > 0:
    percentage = (matched / total_required) * 100
else:
    percentage = 0

percentage = round(percentage, 2)



conclusion_prompt = f"""
You are an HR recruitment recommendation agent.

Candidate skills:
{resume_skill}

Job description:
{job_description}

Matching skills:
{matching_skill}

Matching percentage:
{percentage}%

Based on the above information, provide a short recruitment
conclusion and determine whether the candidate is eligible.

Return ONLY valid JSON:

{{
    "name": "",
    "conclusion": "",
    "matching_percentage": {percentage},
    "eligible": true
}}
"""
conclution_message={
  "role":role,
  "content":conclusion_prompt
}

conclution_message_system={
  "role":"system",
  "content":"you are a conclution provider and percentage calculator"
}

conclution_messages=[conclution_message_system,conclution_message]

conclution_check=client.chat.completions.create(model=model,messages=conclution_messages,temperature=0,response_format=response_format)

conclution=conclution_check.choices[0].message.content


print("JOB SKILLS: ")
print(job_skill)

print("-----------------------------------------------------")

print("RESUME SKILLS: ")
print(resume_skill)

print("-----------------------------------------------------")
print("MATCHING SKILLS: ")
print(matching_skill)

print("-----------------------------------------------------")




print("Matching Percentage:", percentage, "%")

print("CONCLUTION: ")
print(conclution)

print("-----------------------------------------------------")

















