from random import randint, choice
from brain_games.scripts.brain_games import startgame


def pr(arr):
    ind = arr.index('..')
    step = (arr[1] - arr[0]) if ind > 1 else (arr[3] - arr[2])
    return str(arr[ind - 1] + step) if ind > 0 else str(arr[ind + 1] - step)


def prrand():
    arr = []
    step = randint(1, 10)
    start = randint(1, 30)
    ind = 0
    while len(arr) < randint(5, 10):
        arr.append(start + ind * step)
        ind += 1
    arr[arr.index(choice(arr))] = '..'
    return arr


def main():
    prinv = 'What number is missing in the progression?'
    startgame(pr, prrand, prinv)


if __name__ == '__main__':
    main()
