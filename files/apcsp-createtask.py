import random
import math

operations = ['addition', 'subtraction', 'multiplication', 'division'] 
usedOperations = []
numbers = [4, 5, 6, 9, 10, 12, 13, 14, 18, 20, 23, 45]

def getUnitsDigit(num):
    return math.floor(num % 10)

def message(correct):
    if correct:
        print("You got that correct!")
    else:
        print("You got that incorrect.")

def askQuestions(usedNumbers, usedOps, questions):
    score = 0
    for i in range(questions):
        print(" ") # spacing/looks purposes
        randomNum1 = random.choice(usedNumbers)
        randomNum2 = random.choice(usedNumbers)
        operation = random.choice(usedOps)
        num1 = max([randomNum1, randomNum2])
        num2 = min([randomNum1, randomNum2])
        # i want num1 to be greater than or equal to num2, for simplicity
        if operation == 'addition':
            response = int(input(f"What is the unit digit of {num1} + {num2}? - "))
            if response == getUnitsDigit(num1+num2):
                message(True)
                score+=1
            else: 
                message(False)     
        elif operation == 'subtraction':
            response = int(input(f"What is the unit digit of {num1} - {num2}? - "))
            if response == getUnitsDigit(num1-num2):
                message(True)
                score+=1
            else: 
                message(False)
        elif operation == 'multiplication':
            response = int(input(f"What is the unit digit of {num1} x {num2}? - "))
            if response == getUnitsDigit(num1*num2):
                message(True)
                score+=1
            else: 
                message(False)
        else:
            response = int(input(f"What is the unit digit of {num1} / {num2}? - "))
            if response == getUnitsDigit(num1/num2):
                message(True)
                score+=1
            else: 
                message(False)
                
    return score

def game(questions, usedNumbers, usedOps):
    print("For the following questions, respond with the units digit of the result.")
    
    score = askQuestions(usedNumbers, usedOps, questions)
            
    print(" ") # spacing/looks purposes
    print(f"You got {score} questions correct!")
    print(f"That's a score of {round((score/questions)* 100)}%!") 

questionCount = int(input("How many questions do you want to be asked? - "))
for op in operations:
    use = input(f"{op}: Would you like to use this operation? (respond using Y/N) - ").lower()
    if use == "y":
        usedOperations.append(op)
 
game(questionCount, numbers, usedOperations)