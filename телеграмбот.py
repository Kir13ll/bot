from PIL import Image, ImageDraw, ImageFont
import telebot
import random
import choice
from telebot import types
вещества = [1, 2]
рандом_масса = [1, 2, 0.5]
m =  random.choice(рандом_масса)
v =  random.choice(вещества)


#вид задачи
if m == 0.5 and v == 1:
    z1 = "    №1\n\nВычислите кол-во теплоты необходимое\nдля испарения 1 кг воды, взятой при t кипения" 
    d = 2260
elif m == 1 and v == 1:
   z1 = "     №1\n\nВычислите кол-во теплоты необходимое\nдля испарения 2 кг воды, взятой при t кипения"  
   d = 4520
elif m == 2 and v == 1:
    z1 = "    №1\n\nВычислите кол-во теплоты необходимое\nдля испарения 0,5 кг воды, взятой при t кипения"  
    d = 1130
elif m == 2 and v == 2:
   z1 = "     №1\n\nВычислите кол-во теплоты необходимое\nдля испарения 2 кг спирта, взятого при t кипения" 
   d = 1812
elif m == 1 and v == 2:
    z1 = "    №1\n\nВычислите кол-во теплоты необходимое\nдля испарения 0,5 кг спирта, взятого при t кипения"  
    d = 453
elif m == 0.5 and v == 2:
    z1 = "    №1\n\nВычислите кол-во теплоты необходимое\nдля испарения 1 кг спирта, взятого при t кипения"   
    d = 906


вещества1 = [1, 2]
рандом_масса2 = [1, 2, 0.5]
m1=  random.choice(рандом_масса)
v1 =  random.choice(вещества)


# №2
if m1== 1 and v1 == 2:
    z2 = "    №2\n\nВычислите кол-во теплоты необходимое\nдля нагревания 1 кг воды от 20 до 52 градусов"
    d2 = 134.4 #
elif m1== 0.5 and v1 == 2:
   z2 = "     №2\n\nВычислите кол-во теплоты необходимое\nдля нагревания 2 кг воды от 30 до 70 градусов"  
   d2 = 336 #
elif m1== 2 and v1 == 2:
    z2 = "    №2\n\nВычислите кол-во теплоты которое выделится\nпри охлаждения 0,5 кг воды от 60 до 23 градусов"
    d2 = 77.7  #
elif m1== 2 and v1 == 1:
   z2 = "     №2\n\nВычислите кол-во теплоты необходимое\nдля нагревания 2 кг спирта от 10 до 60 градусов"
   d2 =240
elif m1== 0.5 and v1 == 1:
    z2 = "    №2\n\nВычислите кол-во теплоты необходимое\nдля нагревания 0,5 кг спирта от 20 до 77 градусов" 
    d2 = 69.4  #
elif m1== 1 and v1 == 1:
    z2 = "    №2\n\nВычислите кол-во теплоты которое выделится\nпри охлаждения 1 кг спирта от 69 до 15 градусов" 
    d2 = 126.9


вещества12 = [1, 2]
рандом_масса21 = [1, 2, 0.5]
m2=  random.choice(рандом_масса)
v2 =  random.choice(вещества)

#  №3
if m2== 1 and v2 == 1:
    z3 = "    №3\n\nВычислите кол-во теплоты необходимое для\nнагревания 1 кг воды от 20 до t кипения градусов,\nа после испарения всей воды"
    d3 = 2596
elif m2== 2 and v2 == 1:
   z3 = "     №3\n\nВычислите кол-во теплоты необходимое для\nнагревания 2 кг воды от 30 до t кипения градусов,\nа после испарения половины воды" 
   d3 =  2848
elif m2== 0.5 and v2 == 1:
    z3 = "    №3\n\nВычислите кол-во теплоты необходимое для\nнагревания 0,5 кг воды от 60 до до t кипения градусов,\nа после испарения половины воды"
    d3 = 649   #
elif m2== 2 and v2 == 2:
   z3 = "     №3\n\nВычислите кол-во теплоты необходимое для\nнагревания 2 кг спирта от 10 до t кипения градусов,\nа после испарения четверти спирта"
   d3 = 779.4 #
elif m2== 0.5 and v2 == 2:
    z3 = "    №3\n\nВычислите кол-во теплоты необходимое для\nнагревания 0,5 кг спирта от 20 до t кипения градусов,\nа после испарения половины спирта" 
    d3 =296.1 #
elif m2== 1 and v2 == 2:
    z3 = "    №3\n\nВычислите кол-во теплоты необходимое для\nнагревания 1 кг спирта от 69 до t кипения градусов,\nа после испарения всего спирта"
    d3 = 927.6
вещества123 = [1, 2]
рандом_масса213 = [1, 2, 0.5]
m3=  random.choice(рандом_масса)
v3 =  random.choice(вещества)

#  №4
if m3== 2 and v3 == 2:
    z4 = "    №4\n\nВычислите кол-во теплоты выделится\nпри охлаждения 1 кг воды от 85 до 29 градусов "
    d4 = 235.2#
elif m3== 1 and v3 == 2:
   z4 = "     №4\n\nВычислите кол-во теплоты выделится\nпри охлаждения 2 кг воды от 67 до 23 градусов" 
   d4 = 369.6 #
elif m3== 0.5 and v3 == 2:
    z4 = "    №4\n\nВычислите кол-во теплоты выделится\nпри охлаждения 0,5 кг воды от 70 до 15 градусов " 
    d4 = 115.5  #
elif m3== 2 and v3 == 1:
   z4 = "     №4\n\nВычислите кол-во теплоты выделится\nпри охлаждения 2 кг спирта от 55 до 7 градусов "
   d4 = 230.4 #
elif m3== 0.5 and v3 == 1:
    z4 = "    №4\n\nВычислите кол-во теплоты выделится\nпри охлаждения 0,5 кг спирта от 75 до 2 градусов"
    d4 = 87.6 #
elif m3== 1 and v3 == 1:
    z4 = "    №4\n\nВычислите кол-во теплоты выделится\nпри охлаждения 1 кг спирта от 69 до 17 градусов "
    d4 = 124.8
вещества1234 = [1, 2]
рандом_масса2134 = [1, 2, 0.5]
m4=  random.choice(рандом_масса)
v4 =  random.choice(вещества)

#  №5
if m4== 0.5 and v4 == 2:
    z5 = "    №5\n\nВычислите кол-во теплоты необходимое\nдля плавления 1 кг льда при температуре -15 градусов,\nа после нагревания воды до t кипения и испарения всего обьёма\nводы" 
    d5 = 3051.5#
elif m4== 2 and v4 == 2:
   z5 = "     №5\n\nВычислите кол-во теплоты необходимое\nдля плавления 2 кг льда при температуре -5 градусов,\nа после нагревания воды до t кипения и испарения 0,5 обьёма\nводы" 
   d5 = 3801 #
elif m4== 1 and v4 == 2:
    z5 = "    №5\n\nВычислите кол-во теплоты необходимое\nдля плавления 0,5 кг льда при температуре -20 градусов,\nа после нагревания воды до t кипения и испарения 0, 5 обьёма\nводы" 
    d5 = 966 #
elif m4== 0.5 and v4 == 1:
   z5 = "     №5\n\nВычислите кол-во теплоты выделится\nпри охлаждении 2 кг спирта от 55 до t кристализации  " 
   d5 = 811.2#
elif m4== 1 and v4 == 1:
    z5 = "    №5\n\nВычислите кол-во теплоты выделится\nпри охлаждении 0,5 кг спирта от 20 до t кристализации  " 
    d5 = 160.8#
elif m4== 2 and v4 == 1:
    z5 = "    №5\n\nВычислите кол-во теплоты выделится\nпри охлаждении 1 кг спирта от 69 до t кристализации " 
    d5 = 439.2
#создание картинки
image = Image.new('RGB', (1500, 500), color = (255, 255, 255))
font = ImageFont.truetype("arial.ttf", size=45)
draw = ImageDraw.Draw(image)
draw.text((100, 100), z1, fill='black', font=font)
image.save('output1.png')
# 2 картинка
image = Image.new('RGB', (1500, 500), color = (255, 255, 255))
font = ImageFont.truetype("arial.ttf", size=45)
draw = ImageDraw.Draw(image)
draw.text((100, 100), z2, fill='black', font=font)
image.save('output2.png')
# 3 картинка
image = Image.new('RGB', (1500, 500), color = (255, 255, 255))
font = ImageFont.truetype("arial.ttf", size=45)
draw = ImageDraw.Draw(image)
draw.text((100, 100), z3, fill='black', font=font)
image.save('output3.png')
# 4 картинка
image = Image.new('RGB', (1500, 500), color = (255, 255, 255))
font = ImageFont.truetype("arial.ttf", size=45)
draw = ImageDraw.Draw(image)
draw.text((100, 100), z4, fill='black', font=font)
image.save('output4.png')
# 5 картинка
image = Image.new('RGB', (1500, 500), color = (255, 255, 255))
font = ImageFont.truetype("arial.ttf", size=45)
draw = ImageDraw.Draw(image)
draw.text((100, 100), z5, fill='black', font=font)
image.save('output5.png')
token = '...'
bot=telebot.TeleBot(token)

res = '1 - 💔'
res2 = '2 - 💔'
res3 = '3 - 💔'
res4 = '4 - 💔'
res5 = '5 - 💔'
@bot.message_handler(commands=['start'])
def info(message):
      bot.send_message(message.chat.id, f'привет, {message.from_user.first_name}, \n я знаю зачем ты здесь 😉\n Давай же быстрее начнём!!\nПиши: ,,погнали" и мы погнали!!!')

d = str(d)
d2 = str(d2)
d3 = str(d3)
d4 = str(d4)
d5 = str(d5)
f = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0

@bot.message_handler()
def add_photo(message):
 global f
 global f2
 global f3
 global f4
 global f5
 global res 
 global res2 
 global res3 
 global res4 
 global res5 
 
 
 if message.text.lower() == "погнали":
      file = open('./output1.png', 'rb')
      file2 = open('./output2.png', 'rb')
      file3 = open('./output3.png', 'rb')
      file4 = open('./output4.png', 'rb')
      file5 = open('./output5.png', 'rb')
      file6 = open('./output6.png', 'rb')
      bot.send_photo(message.chat.id, file )
      bot.send_photo(message.chat.id, file2)
      bot.send_photo(message.chat.id, file3)
      bot.send_photo(message.chat.id, file4)
      bot.send_photo(message.chat.id, file5)
      bot.send_message(message.chat.id, '\nТы должен ввести 5 ответов\n(5 чисел, без единиц измерения в кДж) каждый\nв своём собщении и никак иначе\nПример:')
      bot.send_message(message.chat.id, 'Ответ на первое задание')
      bot.send_message(message.chat.id, 'Ответ на второе задание')
      bot.send_message(message.chat.id, "Вот тебе таблица данных, сверяйся только по ней,\nиначе погрешность может оказаться слишком большой")
      bot.send_photo(message.chat.id, file6)
      bot.send_message(message.chat.id, "После того как убедишься что отправил\nвсе пять ответов напиши 'Результат\nЕсли не знаешь ответа просто напиши 0'")
 if message.text.lower()== d:
        f = 1
        res= '1 - ❤️‍🔥'
 elif message.text.lower()== d2:
        f2 = 1
        res2= '2 - ❤️‍🔥'
 elif message.text.lower()== d3:
        f3 = 1
        res3= '3 - ❤️‍🔥'
 elif message.text.lower()== d4:
        f4 = 1
        res4= '4 - ❤️‍🔥'
 elif message.text.lower()== d5:
        f5 = 1
        res5= '5 - ❤️‍🔥'
 elif message.text.lower() == "результат":
    x = f + f2 + f3 + f4 + f5
    if x == 5 :
     bot.send_message(message.chat.id, res)
     bot.send_message(message.chat.id, res2)
     bot.send_message(message.chat.id, res3)
     bot.send_message(message.chat.id, res4)
     bot.send_message(message.chat.id, res5)
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton('Поздравляю всё правильно!', url='...'))
     bot.reply_to(message,'Внеси данные', reply_markup = markup)
     
    else:
        bot.send_message(message.chat.id, res)
        bot.send_message(message.chat.id, res2)
        bot.send_message(message.chat.id, res3)
        bot.send_message(message.chat.id, res4)
        bot.send_message(message.chat.id, res5)
        bot.send_message(message.chat.id, 'Ты ошибся,\nЗавтра у тебя будет 2 шанс!')
        



bot.polling(none_stop= True)





