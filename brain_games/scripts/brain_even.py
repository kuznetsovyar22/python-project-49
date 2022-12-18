import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name

def game():
    name = welcome_user()
    count = 0
    while count < 3:
        num = randint(0, 99)
        print('Question: ', num)
        answer = prompt.string('Your answer: ')
        if answer == 'yes':
            if num % 2 == 0:
                print('Correct!')
                count+=1
            else:
                print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
                print(f'Let\'s try again, {name}!')
                return 0
        elif answer == 'no':
            if num % 2 == 1:
                print('Correct!')
                count+=1
            else:
                print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
                print(f'Let\'s try again, {name}!')
                return 0
        else:
            cor_ans = 'yes' if num % 2 == 0 else 'no'
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{cor_ans}\'.')
            print(f'Let\'s try again, {name}!')
            return 0
    print(f'Congratulations, {name}!')

def main():
    game()


if __name__ == '__main__':
    main()