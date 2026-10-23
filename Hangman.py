import random
word_list = ['год','месяц', 'день']

def get_word():
    return random.choice(word_list).upper()

word = get_word()
word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
word_completion = word_completion
guessed = False                    # сигнальная метка
guessed_letters = []               # список уже названных букв
guessed_words = []                 # список уже названных слов
tries = 6                          # количество попыток

def display_hangman(tries):
    stages = [
        '''
                _______
                |     |
                |
                |
                |
                |
                |
                ''',
        '''
                _______
                |     |
                |     O
                |
                |
                |
                |
                ''',
        '''
                _______
                |     |
                |     O
                |     |
                |     |
                |
                |
                ''',
        '''
                _______
                |     |
                |     O
                |    \|
                |     |
                |
                |
                ''',
        '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |
                |
                ''',
        '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / 
                |
                ''',
        '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / \\
                |
                |  ТЫ МЕРТВЕЦ!
                '''
    ]
    return stages[6-tries]   # индексы 0..6

def play(word):
    global word_completion, tries, guessed_letters, guessed_words, guessed

    print("Давайте сыграем в Угадайку слов!")
    print(display_hangman(tries))
    print(' '.join(word_completion))
    print(f'Осталось попыток: {tries}')

    while not guessed and tries > 0:
        char = input("Введите букву или слово: ").upper()

        if not char.isalpha():
            print('Это не буква и не слово... Попробуйте снова.')
            continue

        if char in guessed_letters or char in guessed_words:
            print('Ты уже называл это...')
            continue

        if len(char) == 1:
            guessed_letters.append(char)
            if char in word:
                for i in range(len(word)):
                    if word[i] == char:
                        word_completion = word_completion[:i] + char + word_completion[i+1:]
                print('✅ Угадал! Есть такая буква!')
            else:
                tries -= 1
                print('❌ Нет такой буквы!')
                print(display_hangman(tries))
                print(f'Осталось попыток: {tries}')
        else:
            guessed_words.append(char)
            if char == word:
                word_completion = word
                guessed = True
                print('🎉 Поздравляем, вы угадали слово! Вы победили!')
                break
            else:
                tries -= 1
                print('❌ Неверное слово!')
                print(display_hangman(tries))
                print(f'Осталось попыток: {tries}')

        print(' '.join(word_completion))

        if '_' not in word_completion:
            guessed = True
            print('🎉 Поздравляем, вы угадали слово! Вы победили!')

    if not guessed:
        print(display_hangman(0))
        print(f'😵 Ты проиграл! Загаданное слово: {word}')

play(word)


