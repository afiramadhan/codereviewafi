def student_pass(score1, score2, score3):
    t=sorted([score1,score2,score3]) #make a sorted list of all the scores
    if t[0]>=40 or (t[1]>=40 and sum(t)/3>50): #if smallest score is still at least 40, or second smallest is at least 40 with an average greater than 50, then the student passes
        print('This student has passed.')
    else: #in all other cases, the student fails
        print('This student has not passed.')

student_pass(50, 30, 50)