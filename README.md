## about this repo

This repository is used to save mini-projects from various Python courses.

**content:**

- [guess_the_number](#guess_the_number---угадай-число)
- [magic_ball8](#magic_ball8---магический-шар-8)
- [secure_pass_generator](#secure_pass_generator---генератор-безопасных-паролей)
- [caesar_cipher](#caesar_cipher---шифр-цезаря)
- [guess_the_word](#guess_the_word---угадайка-слов)

## guess_the_number - угадай число

**link:** ["Поколение Python": курс для начинающих](https://stepik.org/lesson/349845/step/1?unit=333700)

**description:**
программа генерирует случайное число в диапазоне от 11 до 100100 и просит пользователя угадать это число. Если догадка
пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. Если
догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. Если
пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

**modules:**

- math
- random

**features:**

- подсчёт попыток и вывод результата
- возможность реплея
- установка правой границы

## magic_ball8 - магический шар 8

**link:** ["Поколение Python": курс для начинающих](https://stepik.org/lesson/349846/step/1?unit=333701)

**description:**
магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. Программа должна просить пользователя задать
некий вопрос, чтобы случайным образом на него ответить.

**modules:**

- random

**features:**

## secure_pass_generator - генератор безопасных паролей

**link:** ["Поколение Python": курс для начинающих](https://stepik.org/lesson/349848/step/1?unit=333703)

**description:**
программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие
символы требуется в него включить, а какие исключить.

**modules:**

- random

**features:**

## caesar_cipher - шифр цезаря

**link:** ["Поколение Python": курс для начинающих](https://stepik.org/lesson/352860/step/1?unit=336821)

**description:**
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки
следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются
строчными, а прописные – прописными.

**modules:**

**features:**

## guess_the_word - угадайка слов

**link:** ["Поколение Python": курс для начинающих](https://stepik.org/lesson/349847/step/1?unit=333702)

**description:**
программа загадывает слово, а пользователь должен его угадать. Изначально все буквы слова неизвестны. Также рисуется
виселица с петлей. Пользователь предлагает букву, которая может входить в это слово. Если такая буква есть в слове, то
программа ставит букву столько раз, сколько она встречается в слове. Если такой буквы нет, к виселице добавляется круг в
петле, изображающий голову. Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово. За каждую
неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги.

**modules:**

- random

**features:**

- separated the body parts into a separate module to increase readability