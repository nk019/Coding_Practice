print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time!")
    quit()

print("Great! Let's start the game:)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does ROM stand for? ")
if answer.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does os stand for? ")
if answer.lower() == "operating system":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
print("Thanks for playing!")
