SYMBOLS = ',.!?"'
ALPHABET = ['zyxwvutsrqponmlkjihgfedcba', 'ZYXWVUTSRQPONMLKJIHGFEDCBA']


def ave_caesar(text_in):
    text_out = []
    for word in text_in:
        new_word = word
        for ch in SYMBOLS:
            new_word = new_word.replace(ch, '')
        word_out = ''
        for ch in word:
            if ch in SYMBOLS:
                word_out += ch
            else:
                if ch.isupper():
                    word_out += ALPHABET[1][ALPHABET[1].find(ch) - len(new_word)]
                else:
                    word_out += ALPHABET[0][ALPHABET[0].find(ch) - len(new_word)]
        text_out.append(word_out)

    return ' '.join(text_out)


if __name__ == '__main__':
    print(ave_caesar(input().split()))
