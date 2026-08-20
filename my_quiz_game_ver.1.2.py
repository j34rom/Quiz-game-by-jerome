print("Quiz game by: jerome:)\n")
print("take note: Don't take it seriously, its just a game.\n")
permission = input("Do you want to take the quiz?(yes/no): ")
if permission.lower() == 'yes':
    print("\nGreat!")
    print("Let's begin!!\n")
else:
    print("\nThank you for your time:)\n")
    print(quit())
    
def check(player_answer, real_answer):
    if player_answer.lower() in real_answer:
        
        print("\nCorrect!\n")
        return 1  
 
    else:
        print("\nIncorrect:(\n")
        return 0

score = 0
print("\nDirection: All answer must be in the lower case level or\nelse the program will mark your answers incorrect.\n")
        
question1 = input("1. It is known as the main circuitry board of the computer. : ")
result1 = score + check(question1, ["motherboard"])
    
question2 = input("2. Computer component that processe's raw data into facts and perform calculations : ")
result2 = score + check(question2, ["cpu", "central processing unit"])

question3 = input("3. What is 'P' stands in IPOS cycle? : \n")
result3 = score + check(question3, ["processing"])

question4 = input("4. What interface is use in smartphone? : \n")
result4 = score + check(question4, ["mobile interface"])
    
question5 = input("5. It is the only language that computer can understand. : \n")
result5 = score + check(question5, ["binary"])

final_result = result1 + result2 + result3 + result4 + result5

print("Your total score is " + str(final_result))
total = final_result / 5 * 100
print(str(total) + "%" + " " + "of the quiz you answered correctly!")
if final_result == 5:
    print("Amazing;)")
elif 2 <= final_result <= 4:
    print("Goodjob:)")
elif final_result == 1:
    print("Nice try")
else:
    print("better luck next time")
print("\nFrom dev:\nThank you for using my application i hope you enjoy playing this game, it helps me a lot when you play this game, I hopesame as you. Again thank you for playing my game and see\nyou in my next game:).")