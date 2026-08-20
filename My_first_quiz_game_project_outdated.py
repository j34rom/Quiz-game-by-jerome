print("Quiz game by: jerome:)\n")
print("take note: all your answers must start in capital letter\nevery word 'e.g, Mobile Interface' or else the system will\nstop the program or the system will incorrect your answers.\n")
permission = input("Do you want to take the quiz?: ")
if permission == 'Yes':
    print("\nGreat!")
    print("Let's begin!!\n")
else:
    print(quit())

score = 0
        
quest = input("1. It is known as the main circuitry board of the computer. : ")

if quest == 'Motherboard':
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect:(\n")
    
quest = input("2. Computer component that processe's raw data into facts and perform calculations : ")

if quest == 'CPU' or quest == 'Central Processing Unit':
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect:(\n")

quest = input("3. What is 'P' stands in IPOS cycle? : \n")

if quest == 'Processing':
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect:(\n")

quest = input("4. What interface is use in smartphone? : \n")

if quest == 'Mobile Interface':
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect:(\n")
    
quest = input("5. It is the only language that computer can understand. : \n")

if quest == 'Binary':
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect:(\n")

print("Your total score is " + str(score))
total = score / 5 * 100
print(str(total) + "%" + " " + "of the quiz you answered correctly!")
if score == 5:
    print("Amazing;)")
elif 2 <= score <= 4:
    print("Goodjob:)")
elif score == 1:
    print("Nice try")
else:
    print("better luck next time")
