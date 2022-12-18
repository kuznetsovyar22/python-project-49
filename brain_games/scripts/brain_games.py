#!/usr/bin/env python3
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def startgame(game, rand, inv):
    name = welcome_user()
    print(inv)
    count = 0
    while count < 3:
        quest = rand()
        print('Question: ', str(quest).replace(',', ' ').replace("'", '').replace("[", '').replace("]", ''))  # noqa: E501
        ans = prompt.string('Your answer: ')
        cor_ans = game(quest)
        if ans == cor_ans:
            print('Correct!')
            count += 1
        else:
            print(f'\'{ans}\' is wrong answer ;(. Correct answer was \'{cor_ans}\'.')  # noqa: E501
            print(f'Let\'s try again, {name}!')
            return 0
    print(f'Congratulations, {name}!')
