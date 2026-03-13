# 📄 Resume Analyzer

A web-based Resume Analyzer built using **Python and NLP techniques** to extract, analyze, and evaluate key information from resumes.  
The system compares candidate resumes with job descriptions to identify **matching skills, missing skills, and provide recommendations** to improve the candidate profile.

---

## ✨ Features

- **Resume Parsing:** Extracts information such as skills and key details from resume files.
- **Job Description Matching:** Compares candidate resume with job description.
- **Skill Extraction:** Identifies technical skills using a predefined skill dictionary.
- **Similarity Analysis:** Calculates similarity score between resume and job description.
- **Missing Skill Detection:** Suggests skills that the candidate should learn to match the job requirements.
- **Recommendation System:** Provides guidance to improve the resume.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- Required Python libraries

### Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/AravindBandi1845/resume-analyzer.git
cd resume-analyzer
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
python main.py
```

4. Open the application in your browser (if using Flask):

```
http://127.0.0.1:5000
```

---

## 🛠 Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Core application logic |
| Flask | Web framework |
| NLP | Resume and job description analysis |
| HTML | Frontend interface |
| Text Processing | Skill extraction and matching |

---

## 📂 Project Structure

```
resume-analyzer/
│
├── app.py
├── main.py
├── skill_extractor.py
├── similarity_engine.py
├── missing_skills.py
├── recommender.py
├── weighted_scorer.py
├── pdf_reader.py
│
├── templates/
│   └── index.html
│
├── data/
│   ├── job_description.txt
│   ├── job_skills.txt
│   ├── sample_resume.txt
│   └── skill_dictionary.txt
│
├── requirements.txt
└── README.md
```

---

## 🎯 Purpose

This project aims to:

**Practical Use:**  
Help candidates optimize their resumes by comparing them with job descriptions and highlighting missing skills.

**Educational Goal:**  
Demonstrate the use of **Natural Language Processing, text similarity analysis, modular Python design, and web application development**.

---

## 📊 Output

The system provides:

- Resume matching score
- Extracted skills
- Missing skills
- Recommendations to improve the resume
