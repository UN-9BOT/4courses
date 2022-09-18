from random import choice
from body_parts import stages

WORD_LIST = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие",
             "власть",
             "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин",
             "председатель", "сотрудник", "республика", "личность"]

LETTERS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def display_hangman(tries):
    return stages[tries]


def check_letter(letter):
    if letter not in LETTERS or letter == '':
        letter = input('Введите русскую букву в нижнем регистре!\n')
        return check_letter(letter)
    else:
        return letter


def check_word(word, guessed_letters):
    word_completion = 'Слово: '
    for ch in word:
        if ch in guessed_letters:
            word_completion += ch
        else:
            word_completion += '_'
    return word_completion


def play(word):
    word_in = word  # слово под удаление букв
    guessed_letters = []  # список уже названных букв
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))

    while tries != 0:

        print(check_word(word, guessed_letters))

        letter = input('Введите букву или слово целиком\n')
        if letter == word:
            print('Вы выйграли!')
            print(f'Это слово "{word}"')
            break

        letter = check_letter(letter)

        if letter in word_in:
            word_in = word_in.replace(letter, '')
            if word_in == '':
                print('Вы выйграли!')
                print(f'Это слово "{word}"')
                break
            print('Вы угадали букву!')
            guessed_letters.append(letter)
        else:
            print('К сожалению такой буквы нет')
            tries -= 1
            print(display_hangman(tries))
    else:
        print('Вы проиграли!')
        print(f'Это слово "{word}"')


if __name__ == '__main__':
    guessed = True  # сигнальная метка
    while guessed:
        play(choice(WORD_LIST))
        guessed = int(input('Сыграем ещё раз? ("0" - Нет, "1" - Да)\n'))
