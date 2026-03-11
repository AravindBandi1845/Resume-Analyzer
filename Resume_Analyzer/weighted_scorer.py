import os

def weighted_skill_scorer(resume_skills):
    base_dir = os.path.dirname(__file__)
    job_skills_path = os.path.join(base_dir, "data", "job_skills.txt")

    total_weight = 0
    matched_weight = 0

    with open(job_skills_path, "r", encoding="utf-8") as file:
        for line in file:
            skill, weight = line.strip().lower().split(",")
            weight = int(weight)

            total_weight += weight
            if skill in resume_skills:
                matched_weight += weight

    if total_weight == 0:
        return 0.0

    return (matched_weight / total_weight) * 100


