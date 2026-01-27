import json
import os


class quiz_app:
    def __init__(self):
        self.home()

    def home(self):
        print("*************************Welcome to Quiz Application************************* "
              "\n 1. Set Questions"
              "\n 2. Take Quiz"
              "\n 3. Exit")
        choice = input('Enter Choice : ')

        if choice == '1':
            self.add_questions()

        elif choice == '2':
            self.take_quiz()

        elif choice == '3':
            exit
        else:
            print('Incorret Input!')

    def add_questions(self):
        no_of_ques = int(input("Enter Number of Questions : "))

        questions = {}

        for i in range(1, no_of_ques+1):
            ques = input(f"Enter Question {i}: ")
            ans = input(f"Enter Answer of {i}: ")

            questions[ques] = ans
            print(f"\n Que {i} Added Successfully! \n")
        with open("que.json", 'w') as fw:
            json.dump(questions, fw)

        print("Questions Set Successfully!")
        self.home()

    def take_quiz(self):
        with open("que.json", "r") as rf:
            questions = json.load(rf)

        for ques, ans in questions.items():
            user_ans = input(f"{ques} : ")
            if user_ans.strip().lower() == ans.strip().lower():
                print('Correct Answer')
            else:
                print(f'Wrong Answer, Correct Ans is --> {ans}')


quiz_app()
