import random
import time
difficulty = 2
score = 0
incorrect_answers = 0
play = True
divide_is_int = False
print("You will see randomly generated questions for + - x and /")
print("You will get a score for correct answers and will lose on any incorrect answer.")
print("This is timed but the score mainly matters")
print("Questions get harder the longer you go on for.")
gamemode = int(input("1) infinite mode or 2) 60 second mode? Enter when ready to start: "))
if gamemode == 1:    
    start_time = time.time()
    while play == True:
        op = random.randint(1, 4)
        if op == 1:
            first_subject_difference = random.randint(1, (difficulty * 2))
            second_subject_difference = random.randint(1, (difficulty * 2))
            answer = first_subject_difference + second_subject_difference
            print(first_subject_difference, "+", second_subject_difference)
            user_answer = int(input())
            if user_answer == answer:
                print("")
                difficulty += 1
                score += 1
            else:
                play = False
        elif op == 2:
            first_subject_difference = random.randint(1, difficulty)
            second_subject_difference = random.randint(1, difficulty)
            answer = first_subject_difference - second_subject_difference
            if answer < 0:
                answer = second_subject_difference - first_subject_difference
                print(second_subject_difference, "-", first_subject_difference)
            else:
                print(first_subject_difference, "-", second_subject_difference)
            user_answer = int(input())
            if user_answer == answer:  
                print("")
                difficulty += 1
                score += 1
            else:
                play = False
        elif op == 3:
            first_subject_difference = random.randint(1, int((difficulty / 2)))
            second_subject_difference = random.randint(1, int((difficulty / 2)))
            answer = first_subject_difference * second_subject_difference
            print(first_subject_difference, "x", second_subject_difference)
            user_answer = int(input())
            if user_answer == answer:          
                print("")
                difficulty += 1
                score += 1
            else:
                play = False
        elif op == 4:
            divide_is_int = False
            while divide_is_int == False:
                first_subject_difference = random.randint(1, difficulty)
                second_subject_difference = random.randint(1, difficulty)
                answer = first_subject_difference / second_subject_difference
                if answer - int(answer) == 0:
                    answer = int(answer)
                if isinstance(answer, int):
                    print(first_subject_difference, "/", second_subject_difference)
                    user_answer = int(input())
                    divide_is_int = True
            if user_answer == answer:
                print("")
                difficulty += 1
                score += 1
            else:
                play = False
elif gamemode == 2:
    start_time = time.time()
    while play == True:
        op = random.randint(1, 4)
        if op == 1:
            first_subject_difference = random.randint(1, (difficulty * 2))
            second_subject_difference = random.randint(1, (difficulty * 2))
            answer = first_subject_difference + second_subject_difference
            print(first_subject_difference, "+", second_subject_difference)
            user_answer = int(input())
            if user_answer == answer:
                print("")
                difficulty += 1
                score += 1
                end_time = time.time()
                time_taken = end_time - start_time
                if time_taken >= 60:
                    play = False
            else:
                print("")
                incorrect_answers += 1
                if time_taken >= 60:
                    play = False
        elif op == 2:
            first_subject_difference = random.randint(1, difficulty)
            second_subject_difference = random.randint(1, difficulty)
            answer = first_subject_difference - second_subject_difference
            if answer < 0:
                answer = second_subject_difference - first_subject_difference
                print(second_subject_difference, "-", first_subject_difference)
            else:
                print(first_subject_difference, "-", second_subject_difference)
            user_answer = int(input())
            if user_answer == answer:  
                print("")
                difficulty += 1
                score += 1
                end_time = time.time()
                time_taken = end_time - start_time
                if time_taken >= 60:
                    play = False
            else:
                print("")
                incorrect_answers += 1
                if time_taken >= 60:
                    play = False
        elif op == 3:
            first_subject_difference = random.randint(1, int((difficulty / 2)))
            second_subject_difference = random.randint(1, int((difficulty / 2)))
            answer = first_subject_difference * second_subject_difference
            print(first_subject_difference, "x", second_subject_difference)
            user_answer = int(input())
            if user_answer == answer:          
                print("")
                difficulty += 1
                score += 1
                end_time = time.time()
                time_taken = end_time - start_time
                if time_taken >= 60:
                    play = False
            else:
                print("")
                incorrect_answers += 1
                if time_taken >= 60:
                    play = False
        elif op == 4:
            divide_is_int = False
            while divide_is_int == False:
                first_subject_difference = random.randint(1, difficulty)
                second_subject_difference = random.randint(1, difficulty)
                answer = first_subject_difference / second_subject_difference
                if answer - int(answer) == 0:
                    answer = int(answer)
                if isinstance(answer, int):
                    print(first_subject_difference, "/", second_subject_difference)
                    user_answer = int(input())
                    divide_is_int = True
            if user_answer == answer:
                print("")
                difficulty += 1
                score += 1
                end_time = time.time()
                time_taken = end_time - start_time
                if time_taken >= 60:
                    play = False
            else:
                print("")
                incorrect_answers += 1
                if time_taken >= 60:
                    play = False  
else:
    print("Invalid")
end_time = time.time()
time_taken = end_time - start_time
time_taken = int(time_taken)
if gamemode == 1:
    print("Incorrect")
else:
    print("Invalid - Time has ran out")
print("")
print("Score:", score)
if gamemode == 2:
    accuracy = (score / (score + incorrect_answers)) * 100
    accuracy = round(accuracy, 2)
    print("Accuracy:", str(accuracy) + "% :", incorrect_answers, "incorrect answers")
print("In:", time_taken, "second(s)")
