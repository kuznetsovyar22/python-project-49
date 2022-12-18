from random import randint
from brain_games.scripts.brain_games import startgame


def prime(num):
    count = 0
    for i in range (2, num):
        if num % i == 0:
            count += 1
    return 'yes' if count == 0 else 'no'


def primerand():
    return randint(0, 99)


def main():
    primeinv = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    startgame(prime, primerand, primeinv)


if __name__ == '__main__':
    main()
