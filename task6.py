import random

rand_init = random.randint(1, 100)

def guess_the_number(a, guess, i):
    guess = int(input('Введите предполагаемое число: '))
    if guess == a:
        return print('Число отгадано {} c {} попыток'.format(guess, i))
    elif i == 10:
        print('Число не отгадано, верное число:', a)
    elif guess > a:
        print('Вы ввели БОЛЬШЕЕ число чем загадал коммпьютер', '\n')
        guess_the_number(a, guess, i + 1)
    elif guess < a:
        print('Вы ввели МЕНЬШЕЕ число чем загадал коммпьютер', '\n')
        guess_the_number(a, guess, i + 1)


guess_the_number(rand_init, 0, 1)