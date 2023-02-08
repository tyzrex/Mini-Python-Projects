import requests
import json
import os
import colored
from random import shuffle
from pyfiglet import Figlet
from simple_term_menu import TerminalMenu

f = Figlet(font='slant')

def print_title():
    print(f.renderText('Quiz Game'))

def start_game():
    print("Do you want to play?: ")
    options = ["yes", "no"]
    play_menu = TerminalMenu(options)
    playing = play_menu.show()
    print(f"You have selected {options[playing]}!")

    if(playing == 1):
        exit()
    print("\nStarting the game...\n")

def get_user_settings():
    print("Do you want to use default settings? ")
    options = ["yes", "no"]
    settings = TerminalMenu(options).show()
    print(f"You have selected {options[settings]}!")
    print()
    if(settings == 1):
        print("Choose difficulty: ")
        options = ["easy", "medium", "hard"]
        difficulty = TerminalMenu(options).show()
        difficulty_choice = options[difficulty]
        print(f"You have selected {difficulty_choice} difficulty!")
        question_numbers = str(input("\nHow many questions do you want to answer?: "))
        quiz_category = str(input("\nChoose Category (example; 9: General Knowledge):  "))
        print("You have selected category: ", quiz_category)
        print("\nChoose question type: ")
        quiz_type_options = ["multiple", "true/false"]
        quiz_type = TerminalMenu(quiz_type_options).show()
        quiz_type_choice = quiz_type_options[quiz_type]
        print(f"You have selected {quiz_type_choice} choice type!")
        return difficulty_choice, question_numbers, quiz_category, quiz_type_choice
    else:
        print("\nDefault settings: 10 questions, medium difficulty, general knowledge category")
        return "medium", "10", "9", "multiple"

def api_call(difficulty, question_numbers, quiz_category,quiz_type):
    return requests.get(
        "https://opentdb.com/api.php?amount="+question_numbers+
        "&category="+quiz_category+
        "&difficulty="+difficulty+
        "&type="+quiz_type
    )

def fetch_questions():
    difficulty, question_numbers, quiz_category, quiz_type = get_user_settings()
    questions = api_call(difficulty, question_numbers, quiz_category, quiz_type)
    print("\nFetching questions...")
    with open (os.path.join(os.path.dirname(__file__), "questions.json"), "w") as file:
        json.dump(questions.json(), file, indent=4)
    with open (os.path.join(os.path.dirname(__file__), "questions.json"), "r") as file:
        questions = json.load(file)
    return questions

def colorText(text, color):
    return colored.stylize(text, colored.fg(color))

def no_of_questions(questions):
    return len(questions["results"])

def play_game(questions):
    right_answers = 0
    print("\nNumber of questions: ", no_of_questions(questions))
    shuffle(questions["results"])
    print()

    for question in questions["results"]:
        print(colorText(question["question"], "green"))
        options = question["incorrect_answers"]
        options.append(question["correct_answer"])
        shuffle(options)
        for option in options:
            print(colorText(options.index(option)+1, "yellow"), option)
        print()
        terminal_menu = TerminalMenu(options)
        answer = terminal_menu.show()
        if(options[int(answer)] == question["correct_answer"]):
            print(colorText("Correct Answer!", "green"))
            right_answers += 1
        else:
            print(colorText("Wrong Answer!", "red"))
            print("The correct answer is: ", colorText(question["correct_answer"], "green"))
        print()
    return right_answers

def end_game(right_answers,questions):
    print(f.renderText('Game Over'))
    print()
    print("You got", colorText(right_answers,"green"), "out of ", no_of_questions(questions), " questions correct!")
    print("\nDo you want to play again? ")
    replay_options = ["yes", "no"]
    replay_menu = TerminalMenu(replay_options)
    replay = replay_menu.show()
    if(replay == 0):
        questions = fetch_questions()
        right_answers = play_game(questions)
        end_game(right_answers,questions)
    else:
        exit()

if __name__ == "__main__":
    print_title()
    start_game()
    questions = fetch_questions()
    right_answers = play_game(questions)
    end_game(right_answers,questions)
