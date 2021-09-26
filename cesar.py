text = input()
text = text.split()
key = 0
txt = ''

eng_alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
rus_alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in text:
    key = 0
    for j in i:
        
        if j.isalpha() == False:
            continue
        else:
            key += 1
    for k in i:
        if k.isalpha() == False:
            txt += k
        elif k == k.upper():
            ces = ''
            ces += eng_alpha[eng_alpha.find(k.lower()) + key]
            txt += ces.upper()
        elif  k == k.lower():
            txt += eng_alpha[eng_alpha.find(k) + key]
    txt += ' '
print(txt)
        



