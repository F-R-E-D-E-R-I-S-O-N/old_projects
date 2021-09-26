
import os
import colorama

from colorama import Fore, Back, Style
colorama.init()

rus_alpha = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
    
text = input().lower()

gen_text = ''

for i in text:
    if i not in rus_alpha:
        gen_text += i
        print(gen_text, Fore.GREEN)
        os.system('cls||clear')
    for j in rus_alpha:
        if i != j:
            print(gen_text, Fore.YELLOW + j, Fore.RED,  sep='')
            os.system('cls||clear')
        elif i == j:
            gen_text += i.upper()
            print(gen_text, Fore.WHITE)
            os.system('cls||clear')
            continue

print(gen_text, Fore.GREEN)

