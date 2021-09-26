from typing import Counter
import requests
import webbrowser

title = input()
cntr = 0
def titles_link(title, cntr):
    
    key = '2878d2c3b4615efd371e9e3ffea4b592' 
    text = title.replace(' ', '+') # беру название title и вставля. вместо ' ' знак '+', что бы вставить значение text в ссылку
    text_and_tag = text[text.find('+')+ 1:] # беру из названия существительное для тега
    # https://www.flickr.com/services/api/explore/flickr.photos.search         Параметры:  key, tag, text
    flickr_link_for_finding_photos_id = 'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key='+key+'&tags='+text_and_tag+'&format=json&nojsoncallback=1'
    response = requests.get(flickr_link_for_finding_photos_id).json()
    photos_data = response['photos']['photo'][cntr]
    id = photos_data['id']

    # https://www.flickr.com/services/api/explore/flickr.photos.getSizes       Параметры: key, id
    # Вставляю id
    flickr_link_for_finding_photos_link = 'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key='+key+'&photo_id='+id+'&format=json&nojsoncallback=1'
    response2 = requests.get(flickr_link_for_finding_photos_link).json()
    photos_data2 = response2['sizes']['size'][-5]
    
    search = photos_data2['source']
    webbrowser.open(search, new=0, autoraise=True)

    
more = ''
while more == '':
    search = titles_link(title, cntr)
    cntr += 1
    # more = input()
    