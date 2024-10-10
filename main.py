from tkinter import Button
from turtledemo.forest import start
from unittest import enterModuleContext
import os
import telebot
from telebot import types
bot = telebot.TeleBot('7555313698:AAFJPw8cAgTH6m_N7JZeYjzX2V3sq8uR20U', skip_pending=True)

counter = 0
question_num = 1

def stop(pid):
    os.kill(pid, SIGKILL)
    sys.exit(0)


@bot.message_handler(commands=['start'])
def start(message):
    txt = 'Здравствуйте! Проверьте свои знания книги Станислава Лема "Сумма Технологий",'\
           ' пройдя викторину созданную на её основе. '\
           'В любой момент вы можете прописать команду "Завершить" и узнать ваш результат.'


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    Button1 = types.KeyboardButton('Викторина')

    markup.add(Button1)

    bot.send_message(message.chat.id, txt, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def sus(message):
    global question_num
    global counter
    Button1_txt = ""
    Button2_txt = ""
    Button3_txt = ""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    if message.text == 'Викторина':
        txt = 'За один вопрос вы получате 1 балл. Готовы начать?'

        Button1_txt = 'Продолжить'
        Button2_txt = 'Вернуться назад'

    elif message.text == 'Вернуться назад':
        txt = 'Здравствуйте! Проверьте свои знания книги Станислава Лема "Сумма Технологий",' \
              ' пройдя викторину созданную на её основе. ' \
              'У вас есть выбор рискнуть пойти ВА-БАНК и заработать больше баллов на сложных ' \
              'вопросах или пройти обычную викторину, но заработать меньше баллов.'
        Button1_txt = 'Викторина'

    elif message.text == 'Продолжить':
        txt = 'Вопрос 1: С чего Лем начал повествование своей книги и какой вопрос '\
               'рассматривал первым? Выберете верный ответ: космическая цивилизация, '\
                'эволюция, искусственный интеллект.'
        Button1_txt = 'Космическая цивилизация'
        Button2_txt = 'Эволюция'
        Button3_txt = 'Искусственный интеллект'

    elif (question_num == 1) and ((message.text == 'Космическая цивилизация') or (message.text == 'Эволюция') or (message.text == 'Искусственный интеллект')):
        if message.text == 'Эволюция':
            txt = 'Правильно, вы молодец!'
            counter += 1
        else:
            txt = 'Неправильно, первым вопросом в своей книге Станислав Лем рассмотрел Эволюцию.'
        Button1_txt = 'Вопрос 2'
        question_num += 1

    elif message.text == 'Вопрос 2':
        txt = 'Вопрос 2: Сколько лет кибернетике на момент написания текста? Выберете верный ответ: 17, 24, 18.'
        Button1_txt = '17'
        Button2_txt = '24'
        Button3_txt = '18'

    elif (question_num == 2) and ((message.text == '17') or (message.text == '24') or (message.text == '18')):
        if message.text == '18':
            txt = 'Правильно, продолжайте в том же духе!'
            counter += 1
        else:
            txt = 'Неправильно, на момент написания текста кибернетике 18 лет.'
        Button1_txt = 'Вопрос 3'
        question_num += 1

    elif message.text == 'Вопрос 3':
        txt = 'Вопрос 3: Какую главную идею автор пытается донести до читателя в этой книге? Выберете верный ответ:'\
               ' преимущество развития искусственного интеллекта, '\
                'опасности быстрого технологического прогресса, необходимость критического отношения к науке.'
        Button1_txt = 'Преимущество развития искусственного интеллекта'
        Button2_txt = 'Опасности быстрого технологического прогресса'
        Button3_txt = 'Необходимость критического отношения к науке'

    elif (question_num == 3) and ((message.text == 'Преимущество развития искусственного интеллекта') or (message.text == 'Опасности быстрого технологического прогресса') or (message.text == 'Необходимость критического отношения к науке')):
        if message.text == 'Необходимость критического отношения к науке':
            txt = 'Ты всё делаешь правильно!'
            counter += 1
        else:
            txt = 'Неправильно, главоной идеей книги является необходимость критическиго отношения к науке.'
        Button1_txt = 'Вопрос 4'
        question_num += 1

    elif message.text == 'Вопрос 4':
        txt = 'Вопрос 4: Как автор относится к развитию искусственного интеллекта? Выберете верный ответ: положительно,'\
               ' отрицательно, амбивалентно.'
        Button1_txt = 'Положительно'
        Button2_txt = 'Отрицательно'
        Button3_txt = 'Амбивалентно'

    elif (question_num == 4) and (message.text == 'Положительно') or (message.text == 'Отрицательно') or (message.text == 'Амбивалентно'):
        if message.text == 'Амбивалентно':
            txt = 'Правильно!'
            counter += 1
        else:
            txt = 'Неправильно, автор относится амбивалентно.'
        Button1_txt = 'Вопрос 5'
        question_num += 1

    elif message.text == 'Вопрос 5':
        txt = 'Вопрос 5: Какой прогноз дает Лем относительно будущего человечества? Выберете верный ответ: '\
               'стремительное развитие технологий, серьезные социальные и экологичесие проблемы,'\
               ' переход к постчеловеческой эпохе.'
        Button1_txt = 'Стремительное развитие технологий'
        Button2_txt = 'Серьезные социальные и экологичесие проблемы'
        Button3_txt = 'Переход к постчеловеческой эпохе'

    elif (question_num == 5) and (message.text == 'Стремительное развитие технологий') or (message.text == 'Серьезные социальные и экологичесие проблемы') or (message.text == 'Переход к постчеловеческой эпохе'):
        if message.text == 'Серьезные социальные и экологичесие проблемы':
            txt = 'Правильно! У вас все получается!'
            counter += 1
        else:
            txt = 'Неправильно, Лем дает прогноз, что в будущем будут серьезные социальные и экологические проблемы.'
        Button1_txt = 'Вопрос 6'
        question_num += 1

    elif message.text == 'Вопрос 6':
        txt = 'Вопрос 6: В какой форме представлена книга «Сумма технологий»? Выберете верный ответ: роман, эссе, научная статья.'
        Button1_txt = 'Роман'
        Button2_txt = 'Эссе'
        Button3_txt = 'Научная статья'

    elif (question_num == 6) and (message.text == 'Роман') or (message.text == 'Эссе') or (message.text == 'Научная статья'):
        if message.text == 'Эссе':
            txt = 'Правильно! Вы умничка!'
            counter += 1
        else:
            txt = 'Неправильно, книга является эссе.'
        Button1_txt = 'Вопрос 7'
        question_num += 1

    elif message.text == 'Вопрос 7':
        txt = 'Вопрос 7: Какие философские вопросы поднимаются в этом произведении? Выберете верный ответ: место человека в мире, смысл жизни, моральные ограничесния научного прогресса.'
        Button1_txt = 'Место человека в мире'
        Button2_txt = 'Смысл жизни'
        Button3_txt = 'Моральные ограничения научного прогресса'

    elif (question_num == 7) and (message.text == 'Место человека в мире') or (message.text == 'Смысл жизни') or (message.text == 'Моральные ограничения научного прогресса'):
        if message.text == 'Моральные ограничения научного прогресса':
            txt = 'Правильно! Гордитесь собой!'
            counter += 1
        else:
            txt = 'Неправильно, Станислав Лем поднимает вопросы моральных ограничений научного прогресса.'
        Button1_txt = 'Вопрос 8'
        question_num += 1

    elif message.text == 'Вопрос 8':
        txt = 'Вопрос 8: Можно ли считать книгу «Сумма технологий» продолжением предыдущих работ Лема? Выберете верный ответ: да, нет, возможно.'
        Button1_txt = 'Да'
        Button2_txt = 'Нет'
        Button3_txt = 'Возможно'

    elif (question_num == 8) and (message.text == 'Да') or (message.text == 'Нет') or (message.text == 'Возможно'):
        if message.text == 'Да':
            txt = 'Правильно! Продолжайте!'
            counter += 1
        else:
            txt = 'Неправильно, "Сумма Технологий" считается продолжением предыдущих книг Станислава Лема.'
        Button1_txt = 'Вопрос 9'
        question_num += 1

    elif message.text == 'Вопрос 9':
        txt = 'Вопрос 9: Почему Лем решил написать эту книгу? Выберете верный ответ: для привлечения внимания к будущим технологиям, для популяризации науки, для критики современного общества.'
        Button1_txt = 'Для привлечения внимания к будущим технологиям'
        Button2_txt = 'Для популяризации науки'
        Button3_txt = 'Для критики современного общества'

    elif (question_num == 9) and (message.text == 'Для привлечения внимания к будущим технологиям') or (message.text == 'Для популяризации науки') or (message.text == 'Для критики современного общества'):
        if message.text == 'Для привлечения внимания к будущим технологиям':
            txt = 'Правильно! Не останавливайтесь!'
            counter += 1
        else:
            txt = 'Неправильно, Лем написал книгу для привлечения внимания к будущим технологиям.'
        Button1_txt = 'Вопрос 10'
        question_num += 1

    elif message.text == 'Вопрос 10':
        txt = 'Вопрос 10: Как книга «Сумма технологий» связана с другими произведениями Лема? Выберете верный ответ: является частью его научно-филосовского наследия, совершенно независимая работа, продолжение предыдущих романов.'
        Button1_txt = 'Является частью его научно-филосовского наследия'
        Button2_txt = 'Совершенно независимая работа'
        Button3_txt = 'Продолжение предыдущих романов'

    elif (question_num == 10) and (message.text == 'Является частью его научно-филосовского наследия') or (message.text == 'Совершенно независимая работа') or (message.text == 'Продолжение предыдущих романов'):
        if message.text == 'Является частью его научно-филосовского наследия':
            txt = 'Правильно! Вы ответили на все вопросы!'
            counter += 1
        else:
            txt = 'Неправильно, "Сумма Технологий" является часть его научно-филосовского наследия. Вы молодец, наши вопросы подошли к концу.'
        Button1_txt = 'Конец'
        question_num += 1

    elif message.text == 'Конец':
        txt = '"Сумма Технологий" подвела итог классической эпохи исследования Будущего. В своей ' \
              'книге Станислав Лем провел уникальный и смелый технологический анализ цивилизации.' \
              ' Он проанализировал возможности возникновения принципиально новых групп научных ' \
              'дисциплин и полнотью отказался от простых экстраполяционных построений Будущего. ' \
              'Написанная более 40 лет назад книга нисколько не устарела и является классикой ' \
              'футурологии.'

        print(counter)
        print(question_num)

        Button1_txt = 'Завершить'

    elif message.text == 'Завершить':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, f'{counter} из {question_num-1}', reply_markup=markup)
        bot.stop_polling()
        os.system('python C:\\Users\\1395264\\PycharmProjects\\lem\\restart.py')
        os._exit(0)


    Buttons = [Button1_txt, Button2_txt, Button3_txt]
    for i in Buttons:
        if i != "":
            markup.add(types.KeyboardButton(i))
    bot.send_message(message.chat.id, txt, reply_markup=markup)

bot.polling(non_stop=True, interval=0)