import random

def is_valid(user, end):
    return (1 <= user <= end)

restart = 'да'
counter = 1
print('Здрасте в угадайку')
while restart != 'нет':
    endigit = int(input('укажи конец диапазона\n'))
    randigit = random.randint(1, endigit)
    userdigit = int(input('Загадвый число\n'))
    while is_valid(userdigit, endigit) == True:
        if userdigit < randigit:
            print('+')
            counter += 1
        elif userdigit > randigit:
            print('-')
            counter += 1
        else:
            print('=')
            restart = input('Еще хош?').lower()
            if restart.lower() == 'нет':
                print('\n\n\nПака\n\n\n')
                break
            else:
                randigit = random.randint(1, endigit)
        userdigit = int(input('Загадвый число\n'))
        continue
    else:
        print('Ты че, дурак блят?')
        print('попробуй еще раз')
        continue
print(f'число угаданно с {counter} попитки')