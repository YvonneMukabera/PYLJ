def analyze_scores(scores):
    valid_scores = []

    for score in scores:
        if 0 <= score <= 100:
            valid_scores.append(score)

    if not valid_scores:
        return None

    average = sum(valid_scores) / len(valid_scores)
    passed = [score for score in valid_scores if score >= 50]

    return {
        "average": average,
        "passed": passed,
        "total_valid": len(valid_scores)
    }


scores = [75, 40, 90, -5, 60, 120]
result = analyze_scores(scores)

print(result)