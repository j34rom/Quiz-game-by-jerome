import sys

QUESTIONS = [
    ("It is known as the main circuitry board of the computer.", ["motherboard"]),
    ("Computer component that processes raw data into facts and performs calculations.", ["cpu", "central processing unit"]),
    ("What does 'P' stand for in the IPOS cycle (Input, Process, Output, Storage)?", ["processing", "process"]),
    ("What interface is used in a smartphone?", ["mobile interface", "touch interface", "touchscreen", "gui"]),
    ("It is the only language that a computer can understand.", ["binary", "machine language"]),
]


def check(player_answer, accepted):
    if player_answer.strip().lower() in accepted:
        print("\nCorrect!\n")
        return 1
    print("\nIncorrect:(\n")
    return 0


def main():
    print("Quiz game by: jerome:)\n")
    print("Take note: don't take it seriously, it's just a game.\n")
    permission = input("Do you want to take the quiz? (yes/no): ").strip().lower()
    if permission not in ("yes", "y"):
        print("\nThank you for your time:)\n")
        sys.exit()
    print("\nGreat!")
    print("Let's begin!!\n")
    print("Direction: answers are not case-sensitive.\n")

    score = 0
    for number, (question, accepted) in enumerate(QUESTIONS, 1):
        score += check(input(f"{number}. {question} : "), accepted)

    total = len(QUESTIONS)
    print(f"Your total score is {score}/{total}")
    print(f"{round(score / total * 100)}% of the quiz you answered correctly!")
    if score == total:
        print("Amazing;)")
    elif score >= 2:
        print("Good job:)")
    elif score == 1:
        print("Nice try")
    else:
        print("Better luck next time")
    print("\nFrom dev:\nThank you for using my application. I hope you enjoy playing this game; it helps me a lot when you play it. Again, thank you for playing my game and see\nyou in my next game:).")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        sys.exit("\nBye!")
