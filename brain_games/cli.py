import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    prompt.string('May I have your name? ')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
