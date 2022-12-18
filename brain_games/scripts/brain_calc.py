import prompt
from random import randint, choice
from brain_games.scripts.brain_games import welcome_user, startgame


def calc(calcrand):
    values = calcrand.split(' ')
    if values[1] == '+':
        return str(int(values[0]) + int(values[2]))
    elif values[1] == '-':
        return str(int(values[0]) - int(values[2]))
    elif values[1] == '*':
        return str(int(values[0]) * int(values[2]))


def calcrand():
    operations = ['+', '-', '*']
    return f'{randint(0, 99)} {choice(operations)} {randint(0, 99)}'

def main():
    startgame(calc, calcrand)


if __name__ == '__main__':
    main()