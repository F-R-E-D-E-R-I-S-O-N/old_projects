import random

chars = ''
char = ''

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
length = int(input('Какой длины нужен пароль?'))

what = input('Включать ли цифры 0123456789?')
if what != 'нет':
    chars = chars + digits

what = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
if what != 'нет':
    chars = chars + uppercase_letters

what = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
if what != 'нет':
    chars = chars + lowercase_letters

what = input('Включать ли символы !#$%&*+-=?@^_?....')
if what != 'нет':
    chars = chars + punctuation

 

def generate_password(length, chars):
    password = 'Anatoly'
    for i in range(length):
        password += random.choice(chars)
    password += '\n'
    return password

file = open('D:\Новая папка\\test4.txt', 'a', encoding='utf-8')

while True:
    file.write(generate_password(length, chars))