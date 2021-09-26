for line in open('D:\Новая папка\\bible.txt', 'r+'): 
    if line != '\n': 
        open('D:\Новая папка\\newbible.txt', 'a').write(f'<start>\n{line}<end>\n\n')