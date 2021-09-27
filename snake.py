import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()


first_snake = 30
second_snake = 61
fat_position = 0   # это жирная змейка, мне показалось забавным назвать ее именно так
flag = True
changed_old_time = 0
changed_new_time = 0


oldtime = time.time()
newtime = time.time()

while flag== True:
    oldtime = time.time()
    changed_old_time = oldtime // 0.1 
    changed_new_time = newtime // 0.1
    # Chaged__time - тут кароче миллисекнуды перебираются к целому числу. Умножения не очень работают и я сделал так
    if changed_old_time == changed_new_time:
        if first_snake < 3:
            first_snake += 1
        if second_snake > 117:
            second_snake -= 1
        if changed_old_time == changed_new_time:
            print(' ' * first_snake, Fore.GREEN + '@@@', ' ' * (second_snake - first_snake), Fore.YELLOW + '###') 
        if first_snake == second_snake:
            fat_position = first_snake
            print((first_snake) * ' ', Fore.RED +  '" НЯМ "')
            flag = False
        newtime += 0.08   # Скорость змейки
        first_snake += random.randint(-1, 1)
        second_snake += random.randint(-1, 1)

newtime = time.time()                                       # ТУТ
while flag == False:

    oldtime = time.time()
    changed_old_time = oldtime // 0.1
    changed_new_time = newtime // 0.1
    if changed_old_time == changed_new_time:
        print(' ' * (fat_position), Fore.BLUE + 'ЖЖЖЖЖЖЖ') 
    newtime += 0.08                                           # ТУТ
    fat_position += random.randint(-1, 1)