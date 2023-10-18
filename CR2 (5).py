def student_pass(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    if score1 >= 40 and score2 >= 40 and score3 >= 40:
        print("This student has passed.")
    elif score1 >= 40 and score2 >= 40 and score3 < 40 and average > 50:
        print("This student has passed.")
    elif score1 >= 40 and score3 >= 40 and score2 < 40 and average > 50:
        print("This student has passed.")
    elif score2 >= 40 and score3 >= 40 and score1 < 40 and average > 50:
        print("This student has passed.")
    else:
        print("This student has not passed.")


