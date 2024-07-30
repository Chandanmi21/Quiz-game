print("Welcome to Quiz!")

choice = input("Want to play game?: ")

if choice.lower() != "yes":
    quit()
print("Let's get on a journey!")
score = 0

answer = input("What is capital city of Nepal?: ")
if answer.lower() == "kathmandu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stands for?: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for?: ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got ",score," Questions Correct")



