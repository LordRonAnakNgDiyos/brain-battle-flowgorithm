score = 0
print("          BRAIN BATTLE          ")
print("Answer 3 math questions. Each correct answer earns 1 point.")
print("Question 1: What is 8 + 5?")
answer1 = int(input())
if answer1 == 13:
    print("Correct! +1 point.")
    score = score + 1
else:
    print("ENGKKKKK CORRECT ANSWER IS 13.")
print("Question 2: What is 7 * 6?")
answer2 = int(input())
if answer2 == 42:
    print("Correct! +1 point.")
    score = score + 1
else:
    print("ENGKKKKK CORRECT ANSWER IS 42.")
print("Question 3: What is 20 - 9?")
answer3 = int(input())
if answer3 == 11:
    print("Correct! +1 point.")
    score = score + 1
else:
    print("ENGKKKKK CORRECT ANSWER IS 11.")
print("FINAL SCORE")
print("Your score is:")
print(score)
if score == 3:
    print("Perfect score! You are a Brain Battle champion!")
else:
    if score == 2:
        print("Great job! You know your math.")
    else:
        if score == 1:
            print("Good try! Practice and play again.")
        else:
            print("Keep practicing. You can improve your score!")
print("Thanks for playing Brain Battle!")
