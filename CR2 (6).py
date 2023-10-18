def student_pass(score1, score2, score3):
    
    # count the number of passed subjects
    count = 0
    scores = [score1, score2, score3]
    for score in scores:
        if score >= 40:
          count += 1
          
    # Calculate the average score
    average = sum(scores) // 3
        
    if count == 3:
        print("This student has passed.")
    elif count == 2 and average > 50:
        print("This student has passed.")
    else:
        print("This student has not passed.")
