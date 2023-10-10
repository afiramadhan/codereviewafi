def student_pass(score1, score2, score3):
    #checking if the student pass all subjects at 40 points and above
    if score1 >= 40 and score2 >= 40 and score3 >= 40:
        print("This student has passed.")
    #checking if the student pass at least two subjects at 40 points or above
    #and the overall average is strictly greater than 50 points (so 50 points exactly doesn't meet the requirement).
    elif (score1 >= 40 and score2 >= 40) or (score1 >= 40 and score3 >= 40) or (score2 >= 40 and score3 >= 40): #three possibilities (1,2; 1,3; 2,3) from n(n+1)/2 possibilities
        average_score = (score1 + score2 + score3) / 3 #defining the average
        if average_score > 50:
            print("This student has passed.")
        else:
            print("This student has not passed.")
    else:
        print("This student has not passed.")

#to test this .py script, write your test score here, remove the hashtag, then run directly, without converting to .ipynb :
#student_pass(50, 50, 50)
