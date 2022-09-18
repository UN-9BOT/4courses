from random import sample

DIGITS: str = '0123456789'
UPPERCASE_LETTERS: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE_LETTERS: str = 'abcdefghijklmnopqrstuvwxyz'
SYMBOLS: str = '!#$%&*+-=?@^_'
VCC = 'il1Lo0O'


def generate_password():
    chars = ''

    amount_pass = int(input('Сколько паролей сгенерировать?\n'))
    len_pass = int(input('Какой длины пароль?\n'))
    vcc_in = int(input(f'Использовать в пароле VCC символы ({VCC})? ("0" - Нет, "1" - Да\n'))

    key_data = {DIGITS: int(input('Использовать в пароле цифры? ("0" - Нет, "1" - Да\n')),
                UPPERCASE_LETTERS: int(input('Использовать в пароле ЗАГЛАВНЫЕ буквы? ("0" - Нет, "1" - Да\n')),
                LOWERCASE_LETTERS: int(input('Использовать в пароле строчные буквы? ("0" - Нет, "1" - Да\n')),
                SYMBOLS: int(input(f'Использовать в пароле символы ({SYMBOLS})? ("0" - Нет, "1" - Да\n'))}

    for key, value in key_data.items():
        if value:
            chars += str(key)
    if vcc_in:
        for ch in VCC:
            chars.replace(ch, '')
    passwords = [''.join(sample(chars, len_pass)) for _ in range(amount_pass)]
    for i in passwords:
        print(i)


if __name__ == '__main__':
    generate_password()
