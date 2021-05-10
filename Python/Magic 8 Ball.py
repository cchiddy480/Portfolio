# Project - magic 8 ball
# Utilization of random values via "random" import
import random

# name will assigned to user input
# no input = termination of program and custom error message
user = str(input("Please enter your name: "))
if user == "":
    print("Input needed.. Program will now end.")
    exit()

# question will be assigned an input
# user must enter yes or no question
question = str(input("Please enter a yes or no question: "))

# answer will hold the response of the ball
answer = ""

# storing of randomly generated number between 1 and 9
random_number = random.randint(1, 9)

# implementing core logic using if/elif/else statements for an answer
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt!"
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# printing the inputted name and question
print("\n" + user + " asks: " + "\n" + question + "?")
# printing the Magic 8 balls answer
print("\n" + "The Magic 8-Ball responds.." + "\n" + answer)

