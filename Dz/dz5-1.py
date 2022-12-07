#1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

text = 'Напишите программу, удаляющую из текста все слова, содержащие заданную строку'

def del_some_words(text):
    text = list(filter(lambda x: 'все' not in x, text.split()))
    return " ".join(text)

text = del_some_words(text)
print(text)