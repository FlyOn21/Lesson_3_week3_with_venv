# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[10])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word_l = word.lower()
coun_word = word_l.count('а')
print(coun_word)


# Вывести количество гласных букв в слове
word = 'Архангельск'
count_vowels = []
word_l = word.lower()
vowels_lib = ['а','у','о','ы','и','э','я','ю','ё','е']
for letter in word_l:
    if letter in vowels_lib:
        count_vowels.append(letter)
    else:
        continue
print(len(count_vowels))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
word = sentence.split()
print(len(word))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word_one in words:
    print(word_one)


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
len_word_count = []
for len_word in words:
    len_word_count.append(len(len_word))
for mean_word in len_word_count:
    print(mean_word/sum(len_word_count))

