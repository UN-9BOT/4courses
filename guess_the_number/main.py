from random import randint


def lucky():
    generate_num = randint(1, 100)
    in_num = int(input('Угадайте число от 1 до 100 (включительно)\n'))
    while in_num != generate_num:
        if in_num > generate_num:
            in_num = int(input('Слишком много, попробуйте еще раз\n'))
        else:
            in_num = int(input('Слишком мало, попробуйте еще раз\n'))
    else:
        print('Вы угадали, поздравляем!')


if __name__ == '__main__':
    lucky()
