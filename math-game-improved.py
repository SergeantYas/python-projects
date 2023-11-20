import operator
import math
import random
import time

# Operator dictionary
ops = {
    "+": operator.add,
    "-": operator.sub,
    "x": operator.mul,
    "/": operator.truediv
} 

# Game state variables
difficulty = 2
score = 0
incorrect_answers = 0
timeout = 60

# Functions
# Returns randomly generated operand
def generate_operand(difficulty):
    return random.randint(int(math.sqrt(difficulty)) , difficulty)

# Returns tuple of randomly generated operands
def generate_operands(difficulty):
    return (generate_operand(difficulty), generate_operand(difficulty))

# Returns tuple of validated operands depending on the operator provided
def generate_math_test(operator):
    # If operator is multiplication or division, cut difficulty in half if the difficulty is also over 3
    operands = generate_operands(difficulty if operator not in ('x', '/') and difficulty > 3 else int(difficulty/2))
    
    # If operator is subtraction, sort operands in descending order to avoid negative answer
    if operator == '-':
        operands = tuple(sorted(operands, reverse=True))
    
    # If operator is division, set the first operand to be the two operands multiplied together
    # to always have an integer whole number answer
    if operator == '/':
        operands = (operands[0] * operands[1], operands[1])
    
    return operands


# Instructions
print("\n\nYou will see randomly generated questions for + - x and /")
print("You will get a score for correct answers and will lose on any incorrect answer.")
print("This is timed but the score mainly matters")
print("Questions get harder the longer you go on for.")

# Choose game mode
gamemode = 0
while gamemode == 0:
    try:
        selection = int(input(f"\n1) infinite mode or 2) {timeout} second mode? Enter when ready to start: "))
        if selection in (1, 2):
            gamemode = selection
        else:
            raise ValueError
    except ValueError:
        print("Invalid input - Please select 1 or 2.")

# Main gameplay loop
play = True
start_time = time.time()
while play == True:
    # Get operator as String
    op = random.choice(list(ops.keys()))
    operands = generate_math_test(op)
    
    # Perform operation using the ops dict to get the correct operation
    answer = int(ops[op](operands[0], operands[1]))
    
    # Get answer from the user
    try:
        user_answer = int(input(f"\n{operands[0]} {op} {operands[1]}\n"))
    except:
        print("Invalid input")
        play = False
    
    # Process user answer
    if user_answer == answer:
        difficulty += 1
        score += 1
    else:
        print(f"Incorrect - The answer was {answer}")
        if gamemode == 1:
            play = False
        else:
            incorrect_answers += 1
    
    # End game if time taken has surpassed timeout value
    if gamemode == 2:
        end_time = time.time()
        time_taken = end_time - start_time
        if time_taken >= timeout:
            print("You ran out of time!")
            play = False

# Get total time taken
end_time = time.time()
time_taken = end_time - start_time

# Display end of game results
print(f"\nScore: {score}")
if gamemode == 2:
    accuracy = (score / (score + incorrect_answers)) * 100
    print(f"Accuracy: {accuracy:.2f}% ({score}/{score + incorrect_answers})")
print(f"Time taken: {time_taken:.2f} seconds")
