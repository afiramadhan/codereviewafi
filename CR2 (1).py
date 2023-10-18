def student_pass(score1, score2, score3):

    # The student passed
    if score1 >= 40 and score2 >= 40 and score3 >= 40:
        print('This student has passed.')

    # Otherwise...
    elif (score1 >= 40 and score2 >= 40) or (score1 >= 40 and score3 >= 40) or (score2 >= 40 and score3 >= 40):

        # Here the student passed too
        if (score1 + score2 + score3) / 3 > 50:
            print('This student has passed.')

        # Otherwise the student failed
        else:
            print('This student has not passed.')

    # Otherwise the student failed
    else:
        print('This student has not passed.')
