import prompt
from random import randint
from brain_games.scripts.brain_games import welcome_user, startgame


def evenrand():
    return randint(0, 99)


def evengame(num):
    return 'yes' if num % 2 == 0 else 'no'


def main():
    startgame(evengame, evenrand)


if __name__ == '__main__':
    main()