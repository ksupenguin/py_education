# Создайте программу, которая будет выводить список слов в случайном порядке.
# На экране должны печататься без повторений все слова из представленного списка.
import random

words = ['рандом',
         'картошка',
         'апельсин',
         'декабрист',
         'любовь']
new_words = []
while words:
    position = random.randrange(len(words))
    temp = [words[position]]
    new_words += temp
    words = words[:position] + words[position + 1:]
print(new_words)
