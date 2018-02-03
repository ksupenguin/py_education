# Напишите проrрамму, которая принимала бы текст из попьзовательского ввода и печатала этот текст на экране наоборот
text = input('Введите текст: ')
length = len(text)
new_text = ''
count = 1
for letter in text:
    position = length - count
    count += 1
    new_text += text[position]
print(new_text)
input('нажмите энтер чтобы продолжить')
text = input('Введите текст: ')
for letter in text[::-1]:
    print(letter, end='')
