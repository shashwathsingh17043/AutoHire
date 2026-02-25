def calculate_score(found_skills, required_skills):
    if not required_skills:
        return 0

    matched = 0

    for skill in required_skills:
        if skill.lower() in found_skills:
            matched += 1

    score = (matched / len(required_skills)) * 100
    return round(score, 2)