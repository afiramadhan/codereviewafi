def student_pass(score1, score2, score3):

    smallest_score = min(score1, score2, score3)
    largest_score = max(score1, score2, score3)
    middle_score = (score1 + score2 + score3) - smallest_score - largest_score

    average = (score1 + score2 + score3) / 3

    if smallest_score >= 40 or (middle_score >= 40 and average > 50):
        print('This student has passed.')
    else:
        print('This student has not passed.')
