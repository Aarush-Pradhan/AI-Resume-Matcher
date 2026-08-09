# 🤖 AI Resume Matcher

An AI-powered resume screening and skill matching system that analyzes a candidate's resume and compares it with an HR-provided job description.

The system uses AI agents to extract skills, identify matching and missing skills, calculate a matching percentage, and provide an AI-based recruitment recommendation.

---

## 🚀 Features

- 📄 Extract text from PDF resumes
- 🤖 AI-based resume skill extraction
- 💼 Extract required skills from job descriptions
- 🔍 Compare candidate skills with job requirements
- ✅ Identify matching skills
- ❌ Identify missing skills
- ➕ Identify extra skills
- 📊 Calculate resume-job matching percentage
- 👤 Extract candidate name
- 🧠 Generate AI-based recruitment conclusions
- ✅ Determine candidate eligibility

---

## 🏗️ Project Architecture

                    Resume PDF
                        │
                        ▼
                  ┌───────────┐
                  │  PyMuPDF  │
                  └─────┬─────┘
                        │
                        ▼
                   Resume Text
                        │
                        ▼
               ┌─────────────────┐
               │  Resume Agent   │
               │      Groq       │
               └────────┬────────┘
                        │
                        ▼
                  Resume Skills
                        │
                        │
    Job Description ────┤
           │             │
           ▼             ▼
    ┌────────────┐ ┌──────────────┐
    │  Job Agent │ │ Resume Agent │
    │    Groq    │ │     Groq     │
    └──────┬─────┘ └──────┬───────┘
           │              │
           ▼              ▼
    Required Skills   Candidate Skills
           │              │
           └───────┬──────┘
                   ▼
            Matching Agent
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
      Matching  Missing    Extra
       Skills    Skills   Skills
                   │
                   ▼
          Python Score Calculator
                   │
                   ▼
           Matching Percentage
                   │
                   ▼
          Recruitment Agent
                   │
                   ▼
            Final Conclusion

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Groq API | LLM inference and AI agents |
| PyMuPDF | PDF text extraction |
| Pydantic | Data validation and structured schemas |
| python-dotenv | Environment variable management |
| JSON | Structured AI responses |

---

## 📂 Project Structure

    AI-Resume-Matcher/
    │
    ├── .gitignore
    ├── .python-version
    ├── README.md
    ├── app.py
    ├── pyproject.toml
    ├── uv.lock
    ├── sample_resume_aarav_sharma.pdf
    │
    └── src/

---

## ⚙️ Installation

### 1. Clone the repository

    git clone https://github.com/YOUR_USERNAME/AI-Resume-Matcher.git
    cd AI-Resume-Matcher

### 2. Create a virtual environment

    python -m venv .venv

### 3. Activate the virtual environment

#### Windows

    .venv\Scripts\activate

#### Linux / macOS

    source .venv/bin/activate

### 4. Install dependencies

Using pip:

    pip install -r requirements.txt

Or using uv:

    uv sync

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory:

    GROQ_API_KEY=your_groq_api_key_here

The `.env` file should NEVER be uploaded to GitHub.

Make sure `.env` is included in `.gitignore`:

    .env
    .venv/
    __pycache__/

---

## ▶️ Running the Project

After activating the virtual environment, run:

    python app.py

The application will:

1. Read the resume PDF.
2. Extract the resume text using PyMuPDF.
3. Extract required skills from the job description.
4. Extract candidate skills from the resume.
5. Compare the candidate's skills with the job requirements.
6. Identify matching, missing, and extra skills.
7. Calculate the matching percentage.
8. Generate an AI-based recruitment conclusion.
9. Determine whether the candidate is eligible.

---

## 🧠 AI Agent Workflow

The project uses multiple AI-powered agents.

### 1. Job Requirement Agent

The Job Requirement Agent analyzes the job description and extracts the required skills.

It identifies:

- Programming languages
- Web development frameworks
- Database technologies
- Cloud platforms
- Problem-solving requirements
- Teamwork requirements
- Learning requirements

### 2. Resume Skill Agent

The Resume Skill Agent analyzes the candidate's resume and extracts:

- Candidate name
- Programming languages
- Web development frameworks
- Database technologies
- Cloud platforms
- Problem-solving skills
- Teamwork ability
- Passion for learning

### 3. Matching Agent

The Matching Agent compares the job requirements with the candidate's skills.

It identifies:

- Matching skills
- Missing skills
- Extra skills

### 4. Recruitment Agent

The Recruitment Agent generates a final conclusion based on:

- Candidate skills
- Job requirements
- Matching skills
- Missing skills
- Matching percentage

It determines whether the candidate is eligible for the job.

---

## 📊 Matching Score

The matching percentage is calculated using Python.

    Matching Percentage =
    (Matching Skills / Total Required Skills) × 100

For example:

    Matching Skills = 8
    Missing Skills = 2

    Total Required Skills = 8 + 2 = 10

    Matching Percentage = (8 / 10) × 100

    Matching Percentage = 80%

The percentage calculation is performed programmatically instead of relying completely on the LLM.

---

## 📋 Example Output

    JOB SKILLS:

    Programming Languages:
    Python
    Java
    C++

    -----------------------------------------------------

    RESUME SKILLS:

    Candidate: Aarav Sharma

    Programming Languages:
    Java
    Python
    C++
    SQL

    Frameworks:
    Spring Boot
    Flask
    React

    Databases:
    MySQL
    PostgreSQL
    MongoDB

    Cloud:
    AWS
    Docker
    Git
    GitHub

    -----------------------------------------------------

    MATCHING SKILLS:

    Python
    Java
    C++
    Problem Solving
    Teamwork
    Passion for Learning

    -----------------------------------------------------

    Matching Percentage: 100.0%

    -----------------------------------------------------

    CONCLUSION:

    Candidate: Aarav Sharma

    The candidate has a strong background in software
    development and matches the required skills.

    Eligible: True

---

## 🔐 Security

API keys and sensitive environment variables are excluded from Git using `.gitignore`.

The following files should not be committed:

    .env
    .venv/
    __pycache__/
    *.pyc

Never expose your Groq API key in source code or upload it to GitHub.

---

## 🔮 Future Improvements

- [ ] Add Streamlit web interface
- [ ] Allow HR to upload resumes directly
- [ ] Support multiple resume uploads
- [ ] Rank multiple candidates
- [ ] Add DOCX resume support
- [ ] Add experience matching
- [ ] Add education matching
- [ ] Add candidate comparison dashboard
- [ ] Store candidate results in a database
- [ ] Add resume ranking and filtering
- [ ] Deploy the application online
- [ ] Add authentication for HR users

---

## 🎯 Future Workflow

The planned version of the project will allow HR users to upload multiple resumes and compare candidates automatically.

    HR Dashboard
          │
          ▼
    Upload Job Description
          │
          ▼
    Upload Multiple Resumes
          │
          ▼
    Resume Parser
          │
          ▼
       AI Agents
          │
     ┌────┼────┐
     ▼    ▼    ▼
    Skills Experience Education
     │    │    │
     └────┼────┘
          ▼
    Matching Engine
          │
          ▼
    Candidate Ranking
          │
          ▼
    HR Recommendation

---

## 👨‍💻 Author

**Aarush Pradhan**

B.Tech Computer Science & Information Technology

---

## ⭐ Project Status

🚧 Currently under development

The current version focuses on PDF resume parsing, AI-based skill extraction, skill matching, matching percentage calculation, and recruitment recommendations.

---

## 📜 License

This project is created for educational and academic purposes.
