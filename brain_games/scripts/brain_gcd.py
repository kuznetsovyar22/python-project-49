import prompt
from random import randint, choice
from brain_games.scripts.brain_games import welcome_user, startgame


def gcd(gcdrand):
    values = gcdrand.split(' ')
    for i in values:
        int(i)
    res = 1
    maxnum = max(values)
    for i in range(2, int(maxnum) + 1):
        if (int(values[0]) % i == 0) and (int(values[1]) % i == 0):
            res = i
    return str(res)
    

def gcdrand():
    return f'{randint(0, 99)} {randint(0, 99)}'

def main():
    gcdinv = 'Find the greatest common divisor of given numbers.'
    startgame(gcd, gcdrand, gcdinv)


if __name__ == '__main__':
    main()