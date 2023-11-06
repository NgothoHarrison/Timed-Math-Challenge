import random
import time

OPERATORS = ['+', '-', '*', ] # '/'
MIN_OPERAND = 2
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str (left) + ' ' + operator + ' ' + str(right)
    # print (expr)
    answer = eval(expr)
    return expr, answer

    expr, answer = generate_problem()
    # print(expr, answer)

wrong = 0
input('Press enter to start: ')
print('Starting in...')
start_time = time.time()  # get the current time

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            print("Correct!")
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("You got " + str(TOTAL_PROBLEMS - wrong) + " problems correct in " + str(total_time) + " seconds.")
    # print(expr, answer)
    # user_answer = int(input('What is the answer? '))
    # if user_answer == answer:
    #     print('Correct!')
    # else:
    #     print('Incorrect! The answer is', answer)