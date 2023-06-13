# mport random
# n = int(input("Орёл (1) или решка (0): "))
# if n==1:
#   print("Проиграл, была решка")
# else:
#    print("Тоже проиграл! Тут всегда не твой выбор!")
# from typing import TextIO
#import random
# english_dict = {
#    'яблоко'  : 'apple',
#    'молоко'  : 'milk'
# }
# word =  input ("ведите слово на русском языку ")
# if word  in english_dict:
#        print("перевод этого слова:", english_dict[word])
# else:
#   print("такого слова в словаре нет")


# film = {
# "начало": "леонардо ди каприо ",
# "пираты карибского моря" : "джонни депп"
# }
# favorite_actor = "леонардо ди каприо"
# film  = input ("какой фильм вы собираетесь посмотреть?").lower()
# if film in films:
#   actor = film.get(film)
# if actor == favorite_actor:
#    print("этот фильм точно стоит посмотреть!)")
# else:
# print = ("этот филь не стоит посмотреть")
# else:
# print("Такого фильма зyдесь нет!")


# def add(x,y):
#   a = x + y
# return a

# a  = int(input('1 число:'))
# b = int(input('2 число'))
# print(add(a,b))
# print(add(4,5))
# print(add(5,10))

# def greeting(a):
# if a == 'Да':
#  print('Привет!')
# print('Добро пожаловать!')
# for i in range(1):
# a = input('Зайдёте? Да/Нет: ')
# greeting(a)
# print('Следующий.', '\n')

# der_summa_n =

# n = int(input('Введите N:'))

# def summa_n(n):
# if n==0:
# return n
# else:
#  return(n+summa_n(n-1))
# print(f'Сумма чисел от 1 до {n} = {summa_n(n)}')

# def summa_n(n):
# answer = 0

# for el in range(1, n + 1):
#  answer += el

# text = f'Я знаю, что сумма чисел от 1 до {n} равна {answer}'

# return text


# print(summa_n(int(input('Введите число: '))))

# def calc(a, b, operand):
# if operand == '+':   #КАлькулятор
#  res = a + b
# elif operand == '-':
# res = a - b
# elif operand == '*':
# res = a * b
# elif operand == '/':
# res = a / b
# else:
# res = 'Извините, но такой операции нет в калькуляторе.'
# return res


# num1 = int(input('Введите число:'))
# num2 = int(input('Введите число:'))
# opel = input('введите операцию:')
# toga = calc(num1, num2, opel)
# print(toga)

# file = open('calculations.txt', 'a')
# file.write(f'{toga}' + '\n')


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem  in a: #НАПИШИТЕ ЧИСЛА КОТОРЫЕ МЕНЬШЕ 5
#     if elem < 5:
#     print(elem)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #Нужно вернуть список, который состоит
#                                               # из элементов
#                                               # общих для этих двух списков
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = list(filter(lambda elem: elem in b, a))


# import operator  #Отсортируйте словарь по значению в порядке возрастания и убывания.
# d = {1:2,3:4,4:6,8:9,}
#
# result = dict(sorted(d.items() ,key=operator.itemgetter(1)))


# dict_a = {1:10, 2:20} #программа для слияние двух словарей (типо словарей)
##dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
# result = {}
# for d in (dict_a, dict_b, dict_c):
#   result.update(d)


# from tkinter import *

# window = Tk()
# window.geometry("700x500")
# window.title("Самый сложный тест по вселенной Marvel")

# label_title = Label(text='Тестирование по Marvel', font=("Arial", 24), fg='white', bg='red')
# label_title.place(width=700, height=50, x=0, y=0)

# facts = [
# {'text': 'Человеческое имя Халка - Брюс Беннер',
# 'right': 1},
# {'text': 'Уолт Дисней является создателем вселенной Marvel',
#  'right': 0},
# {'text': 'До появления костюма супергероя, человек муравей занимался воровством',
# 'right': 1},
# {'text': 'Выдуманный город Дженоша является родиной Черный Пантеры',
#   'right': 0}


# def check():
# global cur_q, points, var
# answer = var.get()
# if answer == facts[cur_q]['right']:
#    points += 1
# if cur_q < len(facts) - 1:
#   cur_q += 1
#    fact['text'] = facts[cur_q]['text']
##     points_label = Label(text="Вы набрали " + str(points) + " очка",
#                          font=("Arial", 24), fg='black', bg='white')
#       points_label.place(x=0, y=0, width=700, height=250)


# cur_q = 0
# points = 0
# fact = Message(text=facts[cur_q]['text'], font=('Arial', 24), width=680, borderwidth=0)
# fact.configure(justify=CENTER)
# fact.place(x=10, y=70)
#
# var = IntVar()
# true = Radiobutton(text="Правда", variable=var, value=1)
# true.place(x=10, y=120)
# false = Radiobutton(text="Вымысел", variable=var, value=0)
# false.place(x=10, y=170)

# b = Button(text='Ответить', font=("Arial, 24"), fg='black', command=check)
# b.place(x=200, y=180)

# window.mainloop()


# from tkinter import * #КЛИКЕР
#

# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')

# btn = Button(text='Click Me', width=15, height=7, bg="white", fg="black")
#
# btn.pack()
#
#
# def nplus(event):
#   global n
#  n = n + 1  # добавляем 1 к переменной n
# label['text'] = str(n)
#

# btn.bind_all('<Button-1>', nplus)#
#
# label = Label(window, text=str(n), font=('Helvetica'))
# label.pack()
#
# window.mainloop()

# from tkinter import *
# import random  #КЛИКЕР  С 2 СЕК ОТСТОВАНИЯ

# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
# points = 0

# bg_values = ['black', 'blue', 'red', 'lime', 'orange']
# bg_index = 0


# def check():
# global points, bg_index
# b.place(x=random.randint(1, 550), y=random.randint(1, 350))
# points += 1
# label['text'] = points

# if points % 20 == 0:
#  bg_index = 0 if bg_index == len(bg_values) else bg_index + 1
# b['fg'] = bg_values[bg_index]

#
# b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
# b.place(x=150, y=100)
# label = Label(text=points, font=('Arial', 15), fg='black')
# label.place(x=10, y=10)##

# window.mainloop()


# from tkinter import *
# import random

# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
# points = 0

# bg_values = ['black', 'blue', 'red', 'lime', 'orange']
# bg_index = 0


# def check():
#    global points, bg_index
#   b.place(x=random.randint(1, 550), y=random.randint(1, 350))
#  points += 1
# label['text'] = points #Добавьте в кликер ещё одну кнопку,
# которая тоже будет прыгать каждый раз, когда на неё нажимаешь.
# Сделайте так, чтобы при нажатии на одну из кнопок более 10-ти раз и при отсутствии нажатия на другую кнопку,
# та кнопка,
# на которую не нажимали меняла текст на “Ну пожалуйста"

# if points % 20 == 0:
#    bg_index = 0 if bg_index == len(bg_values) else bg_index + 1
#   b['fg'] = bg_values[bg_index]


# b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
# b.place(x=150, y=100)
# label = Label(text=points, font=('Arial', 15), fg='black')
# label.place(x=10, y=10)

# window.mainloop()

# result = list(set(a) & set(b))

# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
# print(result)
# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result)

# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# from heapq import nlargest
# result = nlargest(3, my_dict, key=my_dict.get)
# print(result)

# from tkinter import*

# window = Tk()
# window.geometry ("900x300")
# indow.title(" АХАХХАХАХА ЛОШПЕД У ТЕБЯ  вирус")
# window.config(bg = 'black')
# window.resizable( width =False,  height=False)
# def  on_close():
#  if int(count_text['text']) >0:
#      count_text['text'] = int(count_text['text'])-1
#       count_text.place(x = 250, y = 25 ,widht = 400 , height = 400)


# text =Label(text = " У ТЕБЯ ВИРУС БРО", fg ='green', bg = 'black', font = ('Courier New', 34))
# text.place(x = 100,y = 100, widht = 700, height =100)
# count_text = Label(text = '6', fg = 'green', bg = 'black', font = ('Courier New', 34))


# def on_close():
# if int(count_text['text']) >0:
#     count_text['text'] = int(count_text['text'])-1
#     count_text.place(x = 250, y = 25 ,widht = 400 , height = 400)
#    window.after(1000, on_close)
# else:
#     widht = window.winfo_sceenwidht()
#     height = window.winfo_sceenwinht()
#      window.geometry(str(widht)+"x"+str(height))
#        label_skelet.place(widht = widht, height = height, x = 0 , y = 0)

# text = Label(text=" У ТЕБЯ ВИРУС БРО", fg='green', bg='black', font=('Courier New', 34))
# text.place(x=100, y=100, widht=700, height=100)
# count_text = Label(text='6', fg='green', bg='black', font=('Courier New', 34))


# window.protocol("WM_DELETE_WINDOWN", "on_close")


# window.mainloop()

# from tkinter import *
# МИНИ СПАМ
#
# def f():
#   lbl.config(text='Чтобы забрать выйгрыш необходимо внести 1000руб.',
#             font=("Arial Bold", 20))
# btn.destroy()


# root = Tk()
# root.geometry('400x250')
# root.columnconfigure(index=1, weight=3)
# lbl = Label(root, text="ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!", font=("Arial Bold", 50))
# lbl.grid(column=1, row=2)
# btn = Button(root, text="ПОЛУЧИТЬ ВЫЙГРЫШ!", font=("Arial Bold", 50), command=f)
# btn.grid(column=1, row=3)
# root.overrideredirect(1)
# root.state('zoomed')
# root.mainloop()

# lst = [2, 3, 4, 1, 6, 7, 9, 3, 4]  # ПИШИЕТ ПРОГРАММУ С НАИБОЛЬШЕ МЕСТАМИ

# print(lst)
# minidx, maxidx = lst.index(min(lst)), lst.index(max(lst))
# lst[maxidx], lst[minidx] = lst[minidx], lst[maxidx]
# print(lst)

# import requests
# from bs4 import BeautifulSoup
# import random


# def get_fact():
#    responce = requests.get('http://www.columbia.edu/fdc/sample')
#   responce = responce.content
#  html = BeautifulSoup(responce,'lxml')
# fact = random.choice(html.find_all(class_='p-2 clearfix'))

# print(fact.text)
# print(fact.a.attrs['href'])


# def get_fest():
#   responce = requests.get('https://kudago.com/msk/festival/')
#  responce = responce.content
# html = BeautifulSoup(responce,'lxml')
# fest = random.choice(html.find_all(class_='post-title post-title-free'))

#   print(fest.text)
#  print(fest.a.attrs['href'])


# def get_concert():
#   responce = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
#  responce = responce.content
# html = BeautifulSoup(responce,'lxml')
# concert = random.choice(html.find_all(class_='post-title'))

# print(concert.text)
# print(concert.a.attrs['href'])

# import requests, re #выводить только подзашоловки
# print(re.findall('<h3.*>(.+)</h3>', requests.get('http://www.columbia.edu/~fdc/sample.html').text, flags=re.I))

# import requests
# from bs4 import BeautifulSoup
# import lxml #СПРАСИТЬ ОСНОВННУЮ ИНФУ

# url = 'https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets'

# soup = BeautifulSoup(requests.get(url).text, "lxml")
# list_rows = soup.select_one("div.ecomerce-items-ajax")['data-items']


# choice = input("Напишите жанр: ")

# action = "Modern Warfate"
# adventure = "Dragon age"

# if choice == "Action":
# print(action)
# elif choice == "Adventure":
#    print(adventure)

# x = [1 ,2 ]

# if  not x == 0:
#   x = 1
#  print('x был равен нулю')
# elif type(x) == type(5)  or type(x) == type(5.5):
#   print('x допустимое значение')
# else:
#   print('В x не допустимый тип данных ')
#  x = 1
# print(100/x)

#
# import os
# while True:
#     sayt = input('Введите адрес сайта\n')
#     if sayt == 'завершить':
#         break
#
#     if 'https://' in sayt:
#         os.system('start' + sayt)
#         print('if')
#
#     elif 'www.' in sayt:
#         sayt ='https://' + sayt
#         os.system('start' + sayt)
#         print('elif')
#     else:
#         sayt = 'https://www.' + sayt
#         os.system('start'  + sayt)
#         print('else')

# number = int(input('Введите число:'))
# summa =0
# while number != 0:
#     summa += number
#     number = int(input('Введите следующик число:'))
#
# print(number)

# import xlrd,xlwt
# rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)
# sheet = rb.sheet_by_index(0)
# val = sheet.row_values(0)[0]
# vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#
# wb = xlwt.Workbook()
# ws = wb.add_sheet('Test')
# ws.write(0, 0, val[0])
#
# i = 0
# for rec in vals:
#     ws.write(i,1,rec[0])
#     i =+ i
#
#
# wb.save('../ArticleScripts/ExcelPython/xl_rec.xls')


# int_num = 53
##summ = oct(int_num)
# print(summ)


# a = input()
# b = input()
# c = input()
# print(a, b ,c , sep = a)

# from fpdf import FPDF
#
# pdf = FPDF('P', 'mm', 'A4')
# pdf.add_page()
# pdf.image('d_day.jpg', w = 210,h = 297, y = 0)
# pdf.add_font
#
# pdf.output("happy_bday.pdf")
#      print('я работаю!')
# #функция декоратор аргумент функция которую надо  дкокорировать
# def my_decorator(func_to_decorete):
#     #функция обертка (фантик)
#     def decoreted_func():
#         #выплняется до самой функции
#         print('я начинаю работать ')
#         #выполняется после функции
#         func_to_decorete()
#         #возращаем после функции
#         print('я закончила работать.')
#     return decoreted_func()
#
# #@my_decorator
# def my_func():
#     print('я работаю')
#
# my_decorator(my_func)




# import telebot  # pyTelegramBotAPI
# import requests
# from bs4 import BeautifulSoup
# import random
#
# token = '5905856947:AAGR-OJudJd1BAxfXMxKFc1r5jE8jVELFAo'
# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#       welcome = "Привет! Я умею рассказывать стихи, интересные факты, показывать котиков"
#       bot.send_message(message.chat.id, welcome)
#       keyboard = telebot.types.ReplyKeyboardMarkup(row_width= 2,resize_keyboard= True,
#                                                    one_time_keyboard= False)
# @bot.message_handler(commands=['poem'])
# def send_poem(message):
#       poem_text = "Муха села на варенье, вот и всё стихотворение"
#       bot.send_message(message.chat.id, poem_text)
#       keyboard = telebot.types.InlineKeyboardMarkup(row_width = 1)
#       button = telebot.types.InlineKeyboardButton("Перейти", url = 'https://stihi.ru/')
#       keyboard.add(button)
#       bot.send_message(message.chat.id, 'Больше схихов по сылке ниже ', reply_markup=keyboard)
#
#
# @bot.message_handler(commands=['fact'])
# def send_fact(message):
#       responce = requests.get('https://i-fakt.ru')
#       responce = responce.content
#       html = BeautifulSoup(responce, 'lxml')
#       fact = random.choice(html.find_all(class_='p-2 clearfix'))
#       bot.send_message(message.chat.id, fact.text)
#       bot.send_message(message.chat.id, fact.a.attrs['href'])
#
# @bot.message_handler(commands=['cat'])
# def send_cat(message):
#       cat_number = random.randint(1, 3)
#       cat_img = open('cat'+str(cat_number)+'.jpg', 'rb')
#       bot.send_photo(message.chat.id,cat_img)
#
# # @bot.message_handlers(commands = ['audio'])
# # def send_song(message):
# #      songs = ['ABBA', 'Bon_Jovi', 'Dean_Martin']
# #      song = open(random.choice(songs)+'.mp3', 'rb')
# #      bot.send_audio(message.chat.id , song)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#      welcome = "Привет! Я умею рассказывать стихи, интересные факты, показывать котиков"
#      bot.send_message(message.chat.id, welcome)
#      keyboard = telebot.types.ReplyKeyboardMarkup(row_width= 2,resize_keyboard= True,
#                                                   one_time_keyboard= False)
#      button1 = telebot.types.KeyboardButton("Факт")
#      button2 = telebot.types.KeyboardButton("стихотворение")
#      button3 = telebot.types.KeyboardButton('Котики')
#      button4 = telebot.types.KeyboardButton('Музыка')
#      button5 = telebot.types.KeyboardButton('Стикер')
#      keyboard.add(button1,button2,button3,button4,button5)
#      # noinspection PyArgumentList
#      bot.send_message(message.chat.id)
# #
# @bot.message_handlers(content_types=['text'])
# def answer(message):
#      if message.text.strip() == 'Факт':
#           send_fact(message)
#      elif message.text.strip() == 'Стихотворение':
#           send_poem(message)
#      elif message.text.strip() == 'Котики':
#           send_cat(message)
#
#
# @bot.message_handler(commands=['random_game'])
# def send_advice(message):
#     games = ['Dota', 'StarCraft II', 'CS:GO']
#     game = random.choice(games)
#     bot.send_message(message.chat.id, game)
# bot.polling()






#     intout_var1 =int(input('введите число:'))
#     intout_var2 =int(input('введите чимло:'))
# except ValueError:
#     print('вы велии неправилное число')
# else:
#     if intout_var1 > intout_var2:
#        print(intout_var1, 'больше',intout_var2)
#     elif intout_var1 < intout_var2:
#         print(intout_var1, 'меньше', intout_var2)
#     else:
#          print(intout_var1, 'равно', intout_var2)
#
# def add(x, y ):
#     return x+y
#
# var = add(4,6)
# print(var)
# def counter(a, b, c, res):
#     print("что делаем?")
#     if c == '+':
#         res = a + b                     #НОРМ КАОЛЬКУЛЯТОР
#
#         print(res)
#         return res
#     elif c == '-':
#         res = a - b
#         print(res)
#         return res
#     elif c == '*':
#         res = a * b
#         print(res)
#         return res
#     elif c == '/':
#         res = a / b
#         print(res)
#         return res
#
#
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     c = input()
#     res = 0
#     counter(a, b, c, res)


# from tkinter import*
# #
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width = 800, height = 600, bg='white')
# canvas.pack()
# canvas.create_rectangle(10,10,110,110, fill = 'yellow', outline = '')
# canvas.create_rectangle(100,100,350,350, fill = 'green', outline = '' )
# canvas.create_rectangle(150,150,400,400, fill = 'yellow', outline = '')
# canvas.create_polygon(10, 180, 60, 120, 110, 180, fill = 'yellow', outline = '')
# canvas.create_rectangle(20, 260, 100, 360, fill = 'yellow', outline = '')
# canvas.create_polygon(10, 260, 60, 200, 110, 260, fill = 'green')
# canvas.create_rectangle(30, 290, 60, 310, fill = 'blue', outline = 'black')
# #
#
#
# class House:
#     def __init__(self, roof_color, wall_color, heigt, width, number):
#         self.number = number
#         self.roof_color = roof_color
#         self.wall_color = wall_color
#         self.heigt = 130
#         self.width = 100
#         self.roof = None
#         self.wall = None
#
#
#     def build_house(self, x, y):
#         h = self.heigt
#         w = self.width
#         self.roof = canvas.create_polygon(x, y, x+w, y, x+w/2, h-100,fill = self.roof_color)
#         self.wall = canvas.create_rectangle(x+20, y, x+120, y+100, fill = self.wall_color)
#     def print_info(self):
#         print("Дом номер", str(self.number))
#         print("Цвет крыши", self.roof_color)
#         print("Цвет стен", self.wall_color)
#
#
#
#
# house1 = House("green","yellow", 1)
# house2 = House("pink","purple", 2)
# house1.build_house(20, 50 )
# house2.build_house(180, 50)
# house1.print_info()
# house2.print_info()
#
#
# window.mainloop()




# class Warrior:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health
#
#     def hit(self, target):
#         if type(self) == type(target):
#             target.health -= 20
#         else:
#             raise TypeError
#
# warriors = [Warrior('Воин1'), Warrior('Воин2')]
# while True:
#     q = input('Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите 2: ')
#     if q == '1':
#         i = random.randint(0, 1)
#         attacker, victim = warriors[i], warriors[i - 1]
#         attacker.hit(victim)
#         print(attacker.name, 'атаковал', victim.name)
#         print('У', victim.name, 'осталось здоровья', victim.health)
#         if victim.health <= 0:
#             print(attacker.name, 'победил!!!')
#             break
#     elif q == '2':
#         break
#     else:
#         print('Ошибка ввода')
#
# from tkinter import *
#
#
# class Image(Frame):
#     def __init__(self):
#         # Инициализирую предка этого класса
#         Frame.__init__(self)
#         # Устанавливаю заголовок окна
#         self.master.title("Прямоугольники и треугольники")
#         # Размещаю на всё окно рамку
#         self.pack(fill=BOTH, expand=True)
#
#         # Создаю объект для рисования (Canvas) по рамке (self)
#         c = Canvas(self)
#         # Создаю 3 треугольника. Толщина линии - 2 пикселя
#         c.create_line(10, 10, 100, 100, 150, 50, 10, 10,
#                       fill="#1f1", width=2)
#         c.create_line(150, 10, 150, 100, 180, 200, 150, 10,
#                       fill="#2e2", width=2)
#         c.create_line(250, 110, 350, 150, 280, 200, 250, 110,
#                       fill="#2e2", width=2)
#
#         # Рисую 2 прямоугольника.
#         c.create_rectangle(230, 10, 290, 60,
#                            outline="#f11", fill="#1f1", width=2)
#         c.create_rectangle(20, 110, 90, 160,
#                            outline="#f11", fill="#1f1", width=2)
#         # Размещаю нарисованное на всё окно
#         c.pack(fill=BOTH, expand=True)
#
#     # Создаю главное окно
#
#
# w = Tk()
# # Создаю изображение, которое описано выше
# f = Image()
#
# # Устанавливаю размер основного окна
# w.geometry("400x250")
# # Запускаю главный цикл обработки событий
# w.mainloop()
# class Воин:
#     def __init__(self, name, hp, damage):
#         self.name = name  # str
#         self.hp = hp  # int
#         self.damage = damage  # int
#
#     def hit(self, Юнит):
#         Юнит.hp -= self.damage
#         if Юнит.hp > 0:
#             print(f'"{self.name}" атаковал "{Юнит.name}". У "{Юнит.name}" осталось {Юнит.hp} здоровья')
#         else:
#             print(f'"{self.name}" атаковал "{Юнит.name}". "{Юнит.name}" убит')
#             Юнит.hp = 0
#         return Юнит.hp
#
#
# from random import randint as rnd
#
# Юнит1 = Воин('Воин севера', 100, 20)
# Юнит2 = Воин('Воин юга', 100, 20)
# Юниты = [Юнит1, Юнит2]
#
# while True:
#     attack_index = rnd(0, 1)
#     target_index = (attack_index + 1) % 2
#     target_hp = Юниты[attack_index].hit(Юниты[target_index])
#     if target_hp == 0:
#         print(f'"{Юниты[attack_index].name}" Победил!')
#         break

# from tkinter import*
# from tkinter import PhotoImage
# import random
# window = Tk()
# w = 600
# h = 600
# window.geometry(str(w)+"x"+str(h))
#
# canvas = Canvas(window, width = w, height= h )
# canvas.place(in_= window, x=0 , y=0)
# bg_photo = PhotoImage(file = 'bg_2.png')
#
# class Knight:
#     def __init__(self):
#         self.x =70
#         self.y = h//2
#         self.v = 0
#         self.photo = PhotoImage(file = 'knight.png')
#
#     def up(self, event):
#          knihgt.v = -3
#
#
#
#
#     def down(self, event):
#         knihgt.v = 3
#
#
#
#     def stop(self, event):
#         knihgt.v = 0
# class Dragon:
#     def __init__(self):
#         self.x = 750
#         self.y = random.randint(100, 500)
#         self.v = random.randint(1, 3)
#         self.photo = PhotoImage(file='dragon.png')
#
# knihgt = Knight()
# dragons = []
# for i in range(5):
#     dragons.append(Dragon())
#
# def game():
#     canvas.delete("all")
#     canvas.create_image(300, 300, image = bg_photo)
#     knihgt.y += knihgt.v
#     canvas.create_image(knihgt.x, knihgt.y, image = knihgt.photo)
#     current_to_kill = 0
#     dragon_to_kill = -1
#     for dragon in dragons:
#         dragon.x -= dragon.v
#         canvas.create_image(dragon.x,dragon.y, image = PhotoImage )
#         if ((dragon.x - knihgt.x)**2)+((dragon.y - knihgt.y)**2) <= (96)**2:
#             dragon_to_kill = current_dragon
#         current_dragon  += 1
#         if dragon.x <= 0:
#             canvas.delete('all')
#             canvas.create_text(w // 2, h // 2, text='you win!!', font='Verdana 42', fill='red')
#             break
#
#     if dragon_to_kill >=0:
#         del dragons[dragon_to_kill]
#     if len(dragons) ==0:
#         canvas.delete('all')
#         canvas.create_text(w//2, h//2, text= 'you win!!', font = 'Verdana 42', fill = 'green')
#     else:
#         window.after(15, game)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# game()
#
#
# window.bind("<Key-Up>", knihgt.up)
# window.bind("<Key-Down>", knihgt.down)
# window.bind("<KeyRelease>", knihgt.stop)
# window.mainloop()

# from tkinter import *
# from tkinter import *
# import random
#
# window = Tk()
# w = 600
# h = 600
# window.geometry(f'{w}x{h}')
#
# canvas = Canvas(window, width=w, height=h)
# canvas.place(in_=window, x=0, y=0)
# bg_photo = PhotoImage(file='bg_2.png')
#
#
# class Knight:
#
#     def __init__(self):
#         self.x = 70
#         self.y = h // 2
#         self.v = 0
#         self.v_x = 0
#         self.photo = PhotoImage(file='cat.png')
#
#     def up(self, event):
#         self.v = -3
#
#     def down(self, event):
#         self.v = +3
#
#     def right(self, event):
#         self.v_x = +3
#
#     def left(self, event):
#         self.v_x = -3
#
#     def stop_all(self, event):
#         self.v = 0
#         self.v_x = 0
#
#
# class Dragon:
#     def __init__(self):
#         self.x = random.randint(700, 1500)
#         self.y = random.randint(100, 500)
#         self.v = random.randint(1, 3)
#         self.photo = PhotoImage(file='dragon.png')
#
#
# knight = Knight()
# dragons = []
# for i in range(10):
#     dragons.append(Dragon())
#
#
# def game():
#     canvas.delete('all')
#     canvas.create_image(h // 2, w // 2, image=bg_photo)
#     canvas.create_image(knight.x, knight.y, image=knight.photo)
#     knight.y += knight.v
#     knight.x += knight.v_x
#     canvas.create_image(knight.x, knight.y, image=knight.photo)
#     kill_dragon = -1
#     for i, dragon in enumerate(dragons):
#         dragon.x -= dragon.v
#         canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
#
#         if ((dragon.x - knight.x) ** 2 + (dragon.y - knight.y) ** 2) <= 95 ** 2:
#             kill_dragon = i
#         if dragon.x <= 0:
#             canvas.delete('all')
#             canvas.create_text(w // 2.3, h // 2.3, text='you lose ', font='System 42', fill='red')
#             break
#
#     if kill_dragon > -1:
#         del dragons[kill_dragon]
#
#     if len(dragons) == 0:
#         canvas.delete('all')
#         canvas.create_text(w // 2, h // 2, text='gg you win', font='System 42', fill='red')
#
#     if knight.y <= 52:
#         knight.y = 53
#     if knight.y >= 544:
#         knight.y = 543
#     if knight.x <= 50:
#         knight.x = 51
#     if knight.x >= 550:
#         knight.x = 551
#     window.after(5, game)
#
#
# window.bind('<Key-Up>', knight.up)
# window.bind('<Key-Down>', knight.down)
# window.bind('<Key-Right>', knight.right)
# window.bind('<Key-Left>', knight.left)
# window.bind('<KeyRelease>', knight.stop_all)
#
# window.resizable(height=False, width=False)
# window.mainloop()


# import requests
#
# url = 'https://swapi.dev/api'
# response = requests.get(url).json()
#
# people_api = response.get('people')
# planet_api = response.get('planets')
#
# def check_people(url):
#     people_list = []
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()
#         people_list.append({response.get('name'): response.get('birth_year')})
#     print(people_list)
#
# def checl_planet(url):
#     diameters_list = []
#     for i in range(1,6):
#         response = requests.get(f'{url}/{i}').json()
#         diameters_list.append({response.get('name') : response.get('diameter')})
#         print(diameters_list)
#
# checl_planet(planet_api)

# import requests
#
# url = 'https://swapi.dev/api'
# response = requests.get(url).json()
# starships_api = response.get('starships')
#
# def max_atmosphering_speed(url):
#     speed = []
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()
#         speed.append({response.get('max_atmosphering_speed') : response.get('name')})
#         print(speed)
#
#
# max_speed = 0
# fastest_ship = ""
#
# for ship in starships_api:
#     speed = ship.get("max_atmosphering_speed")
#     if speed == "unknown":
#         continue
#     speed = int(speed)
#     if speed > max_speed:
#         max_speed = speed
#         fastest_ship = ship.get("name")
#
# print("The fastest ship is:", fastest_ship)
# max_atmosphering_speed(starships_api)

# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
# # date = "date_req=11/02/2023"
# today = datetime.today()
# today =today.strftime("%d/%m/%Y")
# payload = {"date_req": today}
# responce = requests.get(url, params=payload)
#
#
# xml = BeautifulSoup(responce.content, features="xml") #вместо lxlm написать html.parser
#
# def get_course(id):
#     course = xml.find("Valute", {'ID' : id}).Value.text
#     return course
#
# print(get_course("R01770"), ' 10 рублей за  шведских крон')
# print(get_course("R01035")," 10 рублей за велок фунт")
# print(get_course("R01235"), " 10 рублей за один долар США")
# print(get_course("R01090B"), " 26 рублей за один белорусский рубль")
# print(get_course("R01720"), "21 руболь за 1 гривню")
# valute_from = "EUR"
# valute_to = "USD"
# amount = int(input("Введите сумму, которая будет конвертирована: "))
#
#
# def course(valute_from, valute_to, amount):
#     rates = {
#         "RUR": 1.0,
#         "USD": 63.0,
#         "EUR": 75.0
#     }
#
#     if valute_from == "RUR":
#         return amount / rates[valute_to]
#     else:
#         return amount / rates[valute_from] * rates[valute_to]
#
#
# print("Конвертированная сумма:", course(valute_from, valute_to, amount))
# print("\n\n")
# a = "10,535".replace(',', ',')
# print(a)
# print(float(a))
# dict = {
#     "apple":"яблоко",
#     "cat":"кошка"
# }

# f =open('fail_valute.txt','w' )# w - запись . r - чтение , a - добфвление .r+ - чтение+запись
# f.write("asdfgh")
# import os
# import time
#
# from pygame import mixer
# from gtts import gTTS
#
# my_file = open("someth.txt", "r", encoding='utf-8')
# my_string = my_file.read()
# my_file.close()
#
# mixer.init()
#
# tts = gTTS(text=my_string, lang='ru')
# tts.save("hello.mp3")
# mixer.music.load("hello.mp3")
# mixer.music.play()
# while mixer.music.get_busy():
#     time.sleep(1)
# mixer.music.unload()
# os.remove("hello.mp3")
# from random import randint
# import  pyaudio
# import speech_recognition as sr
#
# r = sr.Recognizer()
# while True:
#     with sr.Microphone() as sourse:
#         r.adjust_for_ambient_noise(sourse, duration=3)
#         print("Скажите что-нибудь...")
#         audio = r.listen(sourse)
#
#     speech = r.recognize_google(audio, language='ru_RU').lower()
#     print("Вы сказали ", speech)
#     if speech=='привет':
#         print('Привет')
#     if speech=='выйти':
#         break
#
#
# x = ["Привет", "Прииивеет", "Hi"]
# y = ["Мстители", "Железный человек", "Тор"]
#
# while (True):
#     temp = input()
#     if (temp.lower() == "привет"):
#         print(x[randint(0, len(x) - 1)])
#     elif (temp.lower() == "фильм"):
#         print(y[randint(0, len(y) - 1)])

# from tkinter import *
# window = Tk()
# window.title("неоригинальное приложение")
# window.geometry("500x500+230+200")
# count = 0
# def change():
#     global count
#     count += 1
#     lab['text'] = count
#
#
#
# lab = Label(window,text = "Tут должен быть гинальный текст...", font = "16", background= "gold", fg = "red")
# lab.place(x=80, y=100)
# lab['text']="Поменяли текст...."
# lab['bg'] = 'white'
#
# btn = Button(text ="Кнопка",bg = '#4B0082',fg ="#C0C0C0" , font = "18", command = change )
#
# btn.place(x=200, y=200)
# window.mainloop()

# from itertools import accumulate, chain
# def squares(maxn): return chain([0], accumulate(range(1, maxn * 2, 2)))
#
# from tkinter import *
# from random import randint
# window = Tk()
# window.geometry("600x600")
#
# class  Fire:
#     image = PhotoImage(file = 'fire.png').subsample(4,4)
#     def __add__(self, other):
#         if not isinstance(other, Earth):
#         return Clay
#
#
# class   Water:
#     image = PhotoImage(file = 'water.png').subsample(4, 4)
#
# class Wind:
#     image = PhotoImage(file = 'wind.png').subsample(4,4)
#
# class Earth:
#     image = PhotoImage(file = "earth.png").subsample(4,4)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
#
# class Clay:
#     image = PhotoImage(file = 'pottery.png').subsample(4,4)
#
# canvas = Canvas(window, width= 600, height= 600)
# canvas.pack()
# elements = [Earth(), Fire(), Water(), Wind()]
# for elem in elements:
#     canvas.create_image(randint(50, 550), randint(50,550), image = elem.image )
# def move(event):
#     image_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
#     print(event.x, event.y)
#     print(event.x, event.y)
# window.bind("<B1-Mottion>", move)
#
# window.mainloop()
# from pprint import pprint
# if __name__ =='__main__':
#     goods = [
#         {
#             "name":"iphone 14",
#             "brand":"Aplee ",
#             "price":1200
#         },
#         {
#           "name":"samsung",
#             "brand":"samsung",
#             "price":1500
#         },{
#           "name":"realme 25",
#             "brand":"realme",
#             "price":400
#         }
#     ]
#     # def item_price(item):
#     #     return item['price']
    # print(sorted(goods, key=item_price ))
    # pprint(sorted(goods, key = lambda item:item['price']))
    # aplee_list = list(filter(lambda item:item['brand']=="Aplee", goods))
    # print(aplee_list)

    # numbers = ['1', '2','3','4','5','6']
    # numbers = list(map(int, numbers))
    # print(numbers)

 #    names = ['dana', 'pasha', 'nasta', 'kata']
 #    surnames = ['petrov', 'ivanov', 'sidorova', 'danilova']
 #    patromynics = ['aleksandr', 'nikitich', "evgenevich", ]
 #    # full_names = list(map(lambda name, surname: f'{name}: {surname}', names,surnames))
 #    # # print(full_names)
 #    # indexed_goods = []
 #    # for i,item in enumerate(goods):
 #    #     indexed_goods.append({i:item})
 #    # pprint(indexed_goods)
 #    for name,patromynic, surnames in zip(surnames, names,patromynics,  ):
 #        print(name,patromynic ,surnames,)
 # print(__name__)


# class Item:
#  def init(self, price, weight):
#     self.price = price
#     self.weight = weight
#
#
# def __sub__(self, other):
#     new_price = self.price - other.price
#     new_weight = self.weight - other.weight
#     return Item(new_price, new_weight)
#
#
# def __mul__(self, other):
#     new_price = self.price * other
#     new_weight = self.weight * other
#     return Item(new_price, new_weight)
#
#
# def __truediv__(self, other):
#     new_price = self.price / other
#     new_weight = self.weight / other
#     return Item(new_price, new_weight)
#
#
#
#
# item1 = Item(100, 1)
# item2 = Item(50, 0.5)
#
# item3 = item1 - item2
# print(item3.price, item3.weight)  # 50 0.5
#
# item4 = item1 * 2
# print(item4.price, item4.weight)  # 200 2
#
# item5 = item1 / 2
# print(item5.price, item5.weight)  # 50.0 0.5

# class People:
#     def __init__(self,name,year) -> None:
#             self.__name = name
#             self.__year = year
# #ГЕТТЕР - МЕТОД ДЛЯ ПОЛУЧЕНИЯ АТТРИБУТА
#     def get_name(self):
#         return self.__name
#
#     def get_year(self):
#         return self.__year
# #СЕТТЕР - МЕТОД ДЛЯ УСТОНОВЛЕНИЯ АТТРИБУТА
#     def set_name(self,name):
#         self.__name  = name
#
#     def get_year(self, year):
#         self.__year = year
# сложность О(N*M) -> O(N^2)
# def strcounter(s):
#     print(set(s))
#     for sym in set(s): #set() - множество (структура данных с неупорядочных уникальными значениями)
#         count = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 count += 1
#         print(sym, "-", count)
#
# strcounter('abb')
def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0 ) +1
    for sym,count in syms_counter.items():
        print(sym,'-',  count)
strcounter('ФЕДЯ МОЛОДЕЦ!!')