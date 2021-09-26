# Не смотря на то, что я делал код этапами, я принтую все по-факту. То есть, я в одном и том же цикле функциями генерирую 
# параметры и ссылку. И хотел третий этап так же через функцию создавать каталог. Я почекал, в Create catalog image 
# можно заливать пикчу ссылкой.


import random
import requests
import os
n = input('Начинаем?')
# █ Массивы █
nouns = ['world', 'house', 'place', 'group', 'party', 'money', 'point', 'state', 'night', 'water', 'thing', 'order', 'power', 'times', 'court', 'level', 'child', 'south', 'staff', 'woman', 'north', 'sense', 'death', 'range', 'table', 'trade', 'study', 'other', 'price', 'class', 'union', 'value', 'paper', 'right', 'voice', 'stage', 'light', 'march', 'board', 'month', 'music', 'field', 'award', 'issue', 'basis', 'front', 'heart', 'force', 'model', 'means', 'space', 'peter', 'hotel', 'floor', 'style', 'miles', 'needs', 'sales', 'event', 'press', 'doubt', 'blood', 'sound', 'title', 'glass', 'earth', 'river', 'whole', 'piece', 'mouth', 'radio', 'peace', 'start', 'share', 'works', 'truth', 'media', 'smith', 'stone', 'queen', 'stock', 'horse', 'plant', 'visit', 'scale', 'image', 'trust', 'chair', 'cause', 'speed', 'crime', 'pound', 'henry', 'match', 'scene', 'stuff', 'japan', 'claim', 'video', 'trial', 'time', 'year', 'work', 'life', 'part', 'case', 'fact', 'area', 'head', 'hand', 'john', 'side', 'home', 'days', 'week', 'room', 'road', 'form', 'face', 'sort', 'body', 'name', 'book', 'view', 'door', 'line', 'city', 'kind', 'idea', 'west', 'mind', 'land', 'care', 'back', 'rate', 'word', 'food', 'team', 'role', 'town', 'bank', 'need', 'east', 'type', 'date', 'wife', 'club', 'lord', 'king', 'cost', 'ways', 'girl', 'game', 'love', 'news', 'rest', 'hair', 'bill', 'feet', 'fire', 'size', 'term', 'plan', 'hall', 'list', 'loss', 'wall', 'paul', 'army', 'unit', 'park', 'hour', 'test', 'arms', 'look', 'deal', 'help', 'page', 'risk', 'fish', 'film', 'shop', 'site', 'mark', 'lady', 'task', 'sale', 'lack', 'post', 'firm', 'show', 'baby', 'base', 'miss', 'past', 'cash', 'rule', 'turn', 'duty', 'ball', 'way', 'day', 'man', 'end', 'use', 'lot', 'war', 'car', 'law', 'bit', 'god', 'job', 'act', 'age', 'sir', 'air', 'tax', 'art', 'may', 'bed', 'top', 'boy', 'son', 'sea', 'cup', 'sun', 'set', 'new', 'oil', 'eye', 'arm', 'box', 'sex', 'mum', 'aid', 'tea', 'dog', 'bar', 'gas', 'dad', 'pp.', 'tom', 'bus', 'bag', 'leg', 'aim', 'key', 'sky', 'row', 'run', 'pay', 'van', 'bob', 'sum', 'ice', 'joe', 'ref', 'map', 'cat', 'guy', 'lee', 'pub', 'gun', 'gap', 'fun', 'no.', 'bay', 'ken', 'bid', 'hat', 'fee', 'joy', 'cut', 'sam', 'ben', 'ear', 'san', 'net', 'red', 'egg', 'ban', 'vat', 'fox', 'win', 'pop', 'era', 'ray', 'pen', 'tip', 'tin', 'ann', 'pot', 'pat', 'cap', 'lad', 'mud', 'pan', 'tie', 'fat', 'kit']
adjectives = ['little', 'social', 'second', 'public', 'likely', 'better', 'common', 'single', 'former', 'recent', 'strong', 'higher', 'simple', 'modern', 'normal', 'soviet', 'direct', 'useful', 'german', 'future', 'senior', 'annual', 'latter', 'active', 'middle', 'united', 'sexual', 'actual', 'latest', 'famous', 'formal', 'proper', 'unable', 'lovely', 'fourth', 'female', 'mental', 'double', 'afraid', 'bright', 'bloody', 'narrow', 'entire', 'severe', 'unique', 'guilty', 'yellow', 'longer', 'golden', 'sudden', 'living', 'global', 'silent', 'bigger', 'secret', 'visual', 'wooden', 'stupid', 'stable', 'honest', 'slight', 'remote', 'gentle', 'junior', 'broken', 'smooth', 'pretty', 'fellow', 'square', 'steady', 'bitter', 'ethnic', 'weekly', 'random', 'modest', 'asleep', 'clever', 'liable', 'ruling', 'mutual', 'nearby', 'urgent', 'marked', 'superb', 'strict', 'closer', 'marine', 'retail', 'closed', 'unfair', 'flying', 'hungry', 'subtle', 'secure', 'decent', 'bottom', 'lesser', 'casual', 'finest', 'lonely', 'other', 'first', 'great', 'local', 'small', 'right', 'large', 'young', 'early', 'major', 'clear', 'black', 'whole', 'third', 'white', 'short', 'human', 'royal', 'wrong', 'legal', 'final', 'close', 'total', 'prime', 'happy', 'lower', 'sorry', 'basic', 'aware', 'ready', 'green', 'heavy', 'extra', 'civil', 'later', 'chief', 'usual', 'front', 'fresh', 'joint', 'alone', 'worse', 'rural', 'light', 'equal', 'quiet', 'quick', 'daily', 'urban', 'upper', 'moral', 'vital', 'empty', 'brief', 'broad', 'worst', 'clean', 'ideal', 'minor', 'thick', 'inner', 'grand', 'prior', 'roman', 'funny', 'brown', 'sharp', 'alive', 'angry', 'lucky', 'cheap', 'tired', 'armed', 'fixed', 'red', 'rapid', 'fifth', 'solid', 'rough', 'sweet', 'given', 'tough', 'awful', 'proud', 'plain', 'still', 'round', 'silly', 'above', 'blind', 'dirty', 'sixth', 'loose', 'level', 'outer', 'gross', 'acute', 'valid', 'tight', 'exact', 'world', 'house', 'place', 'group', 'party', 'money', 'point', 'state', 'night', 'water', 'thing', 'order', 'power', 'times', 'court', 'level', 'child', 'south', 'staff', 'woman', 'north', 'sense', 'death', 'range', 'table', 'trade', 'study', 'other', 'price', 'class', 'union', 'value', 'paper', 'right', 'voice', 'stage', 'light', 'march', 'board', 'month', 'music', 'field', 'award', 'issue', 'basis', 'front', 'heart', 'force', 'model', 'means', 'space', 'peter', 'hotel', 'floor', 'style', 'miles', 'needs', 'sales', 'event', 'press', 'doubt', 'blood', 'sound', 'title', 'glass', 'earth', 'river', 'whole', 'piece', 'mouth', 'radio', 'peace', 'start', 'share', 'works', 'truth', 'media', 'smith', 'stone', 'queen', 'stock', 'horse', 'plant', 'visit', 'scale', 'image', 'trust', 'chair', 'cause', 'speed', 'crime', 'pound', 'henry', 'match', 'scene', 'stuff', 'japan', 'claim', 'video', 'trial']
sizes = ['', 'Large', 'Small', 'Medium']
colors = ['', 'White', 'Red', 'Blue', 'Yellow', 'Green', 'Gray', 'Black', 'Gold', 'Silver', 'Orange', 'Pink']
# вставил пустое значение по индексу 0 в списках [sizes] и [colors], что бы итог полчился как в предоставленном примере. Либо size либо color, либо и то и то.


# █ Аргументы и листы █
check = 0 # Для нумерации тайтлов (для самого себя) ██████
repeat_list = [] # Список с повторениями, элементы которого я буду реализовывать в принтах с варианатми (строка )




# █ Функции █
# Описываю функцию для поиска картинки по запросу тайтла
def titles_link(title):
    key = '2878d2c3b4615efd371e9e3ffea4b592' 
    text = title.replace(' ', '+') # беру название title и вставля. вместо ' ' знак '+', что бы вставить значение text в ссылку
    text_and_tag = text[text.find('+')+ 1:] # беру из названия существительное для тега
    # https://www.flickr.com/services/api/explore/flickr.photos.search         Параметры:  key, tag, text
    flickr_link_for_finding_photos_id = 'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key='+key+'&tags='+text_and_tag+'&text='+text_and_tag+'&format=json&nojsoncallback=1'
    response = requests.get(flickr_link_for_finding_photos_id).json()
    photos_data = response['photos']['photo'][0]
    id = photos_data['id']

    # https://www.flickr.com/services/api/explore/flickr.photos.getSizes       Параметры: key, id
    # Вставляю id
    flickr_link_for_finding_photos_link = 'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key='+key+'&photo_id='+id+'&format=json&nojsoncallback=1'
    response2 = requests.get(flickr_link_for_finding_photos_link).json()
    photos_data2 = response2['sizes']['size'][3]

    return photos_data2['source']


# Описываю функциию генерации продуктов и их параметров
# Тут генерирую параметры продукта. Пока flag == false, color и size будут генерироваться, и если их значения == '', то flag остается False. Иначе - принт
def generator_product(title, colors, sizes, check):
    flag = False
    while flag == False:
        color = random.choice(colors)
        size = random.choice(sizes)
        if color == '' and size == '':
            continue # Исключаю отсутвие color и size одновременно в одном продукте
        else:
            flag = True          
            if color == '':                
                return (f' {check} // ("{title}, {size}", Size: {size}, quantity: {random.randint(0, 15)})') 
            elif size == '':
                return (f' {check} // ("{title}, {color}", Color: {color}, quantity: {random.randint(0, 15)})')
            else:
                return (f' {check} // ("{title}, {size} {color}", Size: {size}, Color: {color}, quantity: {random.randint(0, 15)})')
    



# Создаю список и добавляю в него продукты без параметров
# Так же я тут создаю повторящиеся тайтлы через рандом
titles = list()
cnt = 0
while cnt != 1000:
    title = (random.choice(adjectives) + ' ' + random.choice(nouns)).title()
    titles.append(title)
    rand = random.randint(1,10)
    while rand == 10:
        titles.append(title)
        rand = random.randint(1,10)
        cnt += 1
    cnt += 1



# Разбораю список [titles] по одному title, генерирую параметры при помощи generator_product и ссылки при помощи titles_link
for title in titles:
    counter = titles.count(title) # считаю одинаковые названия продуктов, если больше 1 - условие if
    if counter > 1 and title not in repeat_list:
        repeat_list.append(title)
            
        print(f'◦ book("{title}")   image: {titles_link(title)}')  # Оглавление продукта для их ваиантов
        link = titles_link(title)
        for j in range(counter): # Генерирую повторяющиеся продукты и их вариации со ссылкой
            check += 1                                                                               # ██████
            print(f'         ▪ variant{generator_product(title, colors, sizes, check)}')
            print('         image:', link, end='\n\n')      
    elif title not in repeat_list: # Генерирую НЕповторяющиеся продукты и их вариации со ссылкой
        check += 1                                                                                   # ██████
        print(f'◦ book{generator_product(title, colors, sizes, check)}')
        print('image:', titles_link(title), end='\n\n')