#!/usr/bin/env python3
import prompt
from random import randint


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
        print('Question: ', quest)
        ans = prompt.string('Your answer: ')
        cor_ans = game(quest)
        if ans == cor_ans:
            print('Correct!')
            count+=1
        else:
            print(f'\'{ans}\' is wrong answer ;(. Correct answer was \'{cor_ans}\'.')
            print(f'Let\'s try again, {name}!')
            return 0
    print(f'Congratulations, {name}!')


def main():
    startgame()


if __name__ == '__main__':
    main()
