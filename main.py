from Question import questions, options
from sys import stdout
import time
import msvcrt


def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.05)


delay_print("\033[1;33;40m ***************QUIZ GAME***************\033[0m\n")
delay_print('''\033[1;30;40m *************INSTRUCTIONS**************
> The player choose the correct letter A, B, C or D for the correct answer.
> There are 12 questions in the quiz.\033[0m

\033[1;32;40m******************ENJOY*****************\033[0m\n''')

print("\033[1;32;40m Press any key to start \033[0m")
msvcrt.getch()


def new_game():
    guesses = []
    correct_guesses = 0

    for i, (question, answer) in enumerate(questions.items(), start=1):
        print(f'Question {i} of {len(questions)}')
        delay_print(question)
        for option in options[i-1]:
            print(option)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        correct_guesses += int(answer == guess)
        if answer == guess:
            print("\033[1;32;40mCORRECT!\033[0m")
        else:
            print(
                f"\033[1;31;40mWRONG! \033[0mthe correct answer is \033[1;32;40m{answer}\033[0m")
    score = int((correct_guesses/len(questions))*100)
    print(f"Your score is: {score}%")


def play_again():
    return input("Do you want to play again? (\033[1;32;40m yes \033[0m or \033[1;31;40m no \033[0m): ").upper() == "YES"


def main():
    new_game()
    while play_again():
        new_game()
    print("Thank you!")


if __name__ == '__main__':
    main()
