def extract_skills(resume_text):
    """
    Extract skills from resume text using a skill dictionary.
    Counts full-word matches only.
    """

    with open("data/skill_dictionary.txt", "r") as file:
        skills = [line.strip().lower() for line in file if line.strip()]

    resume_words = resume_text.lower().split()

    skill_count = {}

    for skill in skills:
        # Ignore very short skills like 'c'
        if len(skill) < 2:
            continue

        count = resume_words.count(skill)

        if count > 0:
            skill_count[skill] = count

    return skill_count


