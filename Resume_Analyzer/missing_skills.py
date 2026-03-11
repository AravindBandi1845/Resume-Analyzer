import os

def find_missing_skills(resume_skills):
    base_dir = os.path.dirname(__file__)
    job_skills_path = os.path.join(base_dir, "data", "job_skills.txt")

    missing = []

    with open(job_skills_path, "r", encoding="utf-8") as file:
        for line in file:
            skill = line.strip().split(",")[0].lower()
            if skill not in resume_skills:
                missing.append(skill)

    return missing

