import random

restart = 'да'
name = input('Как тебя зовут?\n')



def choice():
    answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
    return answers[random.randint(0, 16)]


print(f'\n\n\nПривет {name}, я магический шар, и я знаю ответ на любой твой вопрос.\n ')



question = input('Задай вопрос, на который я, магический мать его шар, смогу ответить. Если тема сама себя ичерпает или закончатся вопросы, пиши     "стоп" \n\n\n Ваш вопрос?\n\n')


while restart != 'стоп':   
    print(choice())
    restart = input().lower()
print('Возвращайся если возникнут вопросы!')