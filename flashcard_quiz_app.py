flashcarads ={
    "What is the capital of france":"Paris",
    "What is 5+7 = ": "12",
    "Who wrote 'To kill a mockingbird'":"Herper Lee",
    "What is chemical symbol of water?":"H20",
    "Which planet is known as the red planet":"Mars"
}


import random

def start_quiz():
    score = 0
    total_questions = len(flashcarads)

    #suffle the questions
    questions = list(flashcarads.keys())
    random.shuffle(questions)

    for question in questions:
        print("\n" + question)
        user_answer = input("Your Answer: ").strip()

        if user_answer.lower() == flashcarads[question].lower():
            print("Correct Answer")
            score +=1
        else:
            print("Incorrect,The correct answer is {flashcarads[question]}")

    print(f"/n you got{score} out of {total_questions} correct!")

#call the function
start_quiz()

def main():
    while True:
        play_again = input("\n Do you want to play again? (yes/no): ").strip().lower()
        if play_again !='yes':
            print("Thanks for playing ! See you next time!")
            break
main()
