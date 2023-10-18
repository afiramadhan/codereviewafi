def student_pass(score1, score2, score3):
    # Create a list of student scores
    student_scores = [score1, score2, score3]

    # Sort the scores in ascending order
    student_scores.sort()

    # Check if the lowest score is greater than or equal to 40
    if student_scores[0] >= 40:
        print("This student has passed.")
    # Check if at least two scores are greater than or equal to 40
    # and the average score is strictly greater than 50
    elif student_scores[1] >= 40 and sum(student_scores) / 3 > 50:
        print("This student has passed.")
    else:
        print("This student has not passed.")
