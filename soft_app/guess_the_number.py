from random import randint
from math import ceil, log2


def is_valid(num) -> int:
    valid = num.isdigit()
    if not valid:
        num = input('А может быть все-таки введем целое число\n')
        return is_valid(num)
    else:
        return int(num)


def lucky(in_num: int, right_num: int):
    def how_smallest(num: int):
        return 2 if num == 2 else ceil(log2(num))

    generate_num = randint(1, right_num)
    counter = 1
    while in_num != generate_num:
        if in_num > generate_num:
            in_num = int(input('Ваше число больше загаданного, попробуйте еще разок\n'))
        else:
            in_num = int(input('Ваше число меньше загаданного, попробуйте еще разок\n'))
        counter += 1
    else:
        print(f'Вы угадали, поздравляем!\nПопыто затрачено {counter}.')
        print(f'Минимальное кол-во для данного диапазона = {how_smallest(right_num)}')

        if int(input('Будем играть ещё раз? ("1" - Да, "0" - Нет)\n')):
            return main()

        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


def main():
    print('Добро пожаловать в числовую угадайку')

    right_num = is_valid(input(f'Укажи максимальное число для диапазона\n'))  # указываем границу
    num_user = input(f'Введите число от 1 до {right_num} (включительно)\n')  # вводим число

    lucky(is_valid(num_user), int(right_num))  # играем


if __name__ == '__main__':
    main()