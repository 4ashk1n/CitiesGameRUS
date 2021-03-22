##from aiogram import Bot, types
##from aiogram.dispatcher import Dispatcher
##from aiogram.utils import executor
import random
import telebot
import unicodedata

a=open(r'Города.txt', encoding='utf8')
b=a.readlines()
bot = telebot.TeleBot('1227384653:AAFRyNHZjH7iO5Qm6E3gLVVbcdtvcWy-r4o')
#dp = Dispatcher(bot)
city=set()
cityb=set()
g=0
globalcity=[] #Списки неиспользованных городов
globalcityb=[] #Списки использованных городов
sl=[] #Айдишники->номера
p=[] #Показатель первого города
d=[] #Последние буквы
n=[] #Слова игроков
ost=[] #Буквы, города на которые закончились


def prov(globalcitym,ostm):                                #ПРОВЕРКА
        for u in globalcitym:
                ostm.add(u[0])
        #print('ostm: ',ostm)
        #print(globalcitym)
        return set(ostm)

@bot.message_handler(commands=['start'])
def start_message(message):                                    # СТАРТ   
        global d
        global p
        global n
        global g
        global sl
        global ost
        global globalcity
        global globalcityb
        sl.append(message.chat.id)
        globalcity.append(0)
        globalcityb.append(0)
        p.append(0)
        d.append(0)
        n.append(0)
        ost.append(0)
                
        g+=1
        globalcity[sl.index(message.chat.id)]=set()
        globalcityb[sl.index(message.chat.id)]=set()
        ost[sl.index(message.chat.id)]=set()
        
        
        for j in b:
            i=j
            i=i.strip()
            globalcity[sl.index(message.chat.id)].add(str.lower(i.casefold()))
        globalcity[sl.index(message.chat.id)]=random.sample(globalcity[sl.index(message.chat.id)],len(globalcity[sl.index(message.chat.id)]))
        #print(ost)
        
        for h in globalcity[sl.index(message.chat.id)]:
                #print(h)
                
                ost[sl.index(message.chat.id)].add(h[0].lower())
        ost[sl.index(message.chat.id)].remove('\ufeff')
        bot.send_message(message.chat.id,'Здравствуйте. Вас приветствует чат-бот для игры в "Города".\nЧтобы узнать правила игры, напишите: /rules\nЧтобы остановить игру, напишите: /stop\nЧтобы перезапустить игру, напишите: /restart')
        bot.send_message(message.chat.id,"Вы начинаете игру:")
        

@bot.message_handler(commands=['restart'])
def restart_message(message):                                    # РЕСТАРТ
        global d
        global p
        global n
        global g
        global sl
        global ost
        global globalcity
        global globalcityb
        p[sl.index(message.chat.id)]=0
        d[sl.index(message.chat.id)]=0
        n[sl.index(message.chat.id)]=0
        globalcity[sl.index(message.chat.id)]=0
        globalcityb[sl.index(message.chat.id)]=0
        ost[sl.index(message.chat.id)].clear()
        
        globalcity.append(0)
        globalcityb.append(0)
        p.append(0)
        d.append(0)
        n.append(0)
        ost.append(0)
        g+=1
        globalcity[sl.index(message.chat.id)]=set()
        globalcityb[sl.index(message.chat.id)]=set()
        for j in b:
            i=j
            i=i.strip()
            globalcity[sl.index(message.chat.id)].add(str.lower(i.casefold()))
        globalcity[sl.index(message.chat.id)]=random.sample(globalcity[sl.index(message.chat.id)],len(globalcity[sl.index(message.chat.id)]))
        for h in globalcity[sl.index(message.chat.id)]:
                ost[sl.index(message.chat.id)].add(h[0].lower())
        ost[sl.index(message.chat.id)].remove('\ufeff')
        bot.send_message(message.chat.id,"Игра успешно сброшена.")



@bot.message_handler(commands=['rules'])
def rules_message(message):                                    # ПРАВИЛА
        bot.send_message(message.chat.id,"Игрок называет какой-либо город. Другой игрок должен назвать город, первая буква названия которого является последней буквой названия предыдущего города. Например: Москва-Арзамас-Сочи-Иркутск-...\nБукву Ё стоит заменить на Е, иначе бот не воспримет город за существующий.\nГорода в игре не должны повторяться.\nМожно использовать только существующие города. Если вы уверены, что названный Вами город существует, но бот считает иначе, значит этого города просто нет в базе городов, которую использует бот.")
        


        
@bot.message_handler(commands=['stop'])                                    # СТОП
def stop_message(message):
        global d
        global p
        global n
        global g
        global sl
        global ost
        global globalcity
        global globalcityb
        bot.send_message(message.chat.id,"Игра окончена. До свидания.")
        p[sl.index(message.chat.id)]=0
        d[sl.index(message.chat.id)]=0
        n[sl.index(message.chat.id)]=0
        globalcity[sl.index(message.chat.id)]=0
        globalcityb[sl.index(message.chat.id)]=0
        ost[sl.index(message.chat.id)].clear()
        


@bot.message_handler(content_types=['text'])                                    #ИГРА
def begin(message):
        global d
        global p
        global ost
        global n
        global g
        global sl
        global globalcity
        global globalcityb
        
        if message.chat.id not in sl:
            bot.send_message(message.chat.id,'Пожалуйста, напишите /start')
            return 0
        n[sl.index(message.chat.id)]=str(message.text).lower()
        n[sl.index(message.chat.id)]=n[sl.index(message.chat.id)].strip()       
        p[sl.index(message.chat.id)]+=1
        
        if n[sl.index(message.chat.id)] in globalcity[sl.index(message.chat.id)] and n[sl.index(message.chat.id)][0]==d[sl.index(message.chat.id)] or n[sl.index(message.chat.id)] in globalcity[sl.index(message.chat.id)] and p[sl.index(message.chat.id)]==1:
                globalcityb[sl.index(message.chat.id)].add(n[sl.index(message.chat.id)])
                globalcity[sl.index(message.chat.id)].remove(n[sl.index(message.chat.id)])
                prevost=ost[sl.index(message.chat.id)]
                ost[sl.index(message.chat.id)]=prov(globalcity[sl.index(message.chat.id)],ost[sl.index(message.chat.id)]) #Проверка 1
                #print(ost[sl.index(message.chat.id)],prevost)
                #if list(prevost)!=list(ost[sl.index(message.chat.id)]):
                                        
                        #bot.send_message(message.chat.id,("Внимание!"))#\nВ базе бота закончились города, начинающиеся с буквы "+str(list(prevost.difference(ost))[0])+".\nИспользуйте букву, стоящую перед ней"))
                                        
                
                
                
                for k in globalcity[sl.index(message.chat.id)]:
                        i=k
                        l=len(n[sl.index(message.chat.id)])
                        if n[sl.index(message.chat.id)][l-1] not in ost[sl.index(message.chat.id)]:   #k - город от бота СДЕЛАТЬ ТАК ЧТОБЫ КОГДА БУКВЫ КОНЧАЛИСЬ ОН ПРЕДУПРЕЖДАЛ ОБ ЭТОМ И ГОВОРИЛ БУКВЫ ПЕРЕД НЕЙ
                                                                                              #n - от человека
                                while n[sl.index(message.chat.id)][l-1] not in ost[sl.index(message.chat.id)]:
                                        l-=1
                        if n[sl.index(message.chat.id)][l-1]==i[0]: 
                                i0=i[0]
                                ii=i.capitalize()
                                d[sl.index(message.chat.id)]=k[len(k)-1]
                                if d[sl.index(message.chat.id)] not in ost[sl.index(message.chat.id)]:
                                        z=-1
                                        while k[z] not in ost[sl.index(message.chat.id)]:
                                                z-=1
                                        d[sl.index(message.chat.id)]=k[z]
                                
                                bot.send_message(message.chat.id,(str(ii)+ "\n\nВам на букву "+str(d[sl.index(message.chat.id)].upper()))) #Крч не пишет то что после запятой
                                
                                        
                                globalcityb[sl.index(message.chat.id)].add(i)
                                
                                globalcity[sl.index(message.chat.id)].remove(i)
                                
                               # prevost=ost[sl.index(message.chat.id)]
                               # ost[sl.index(message.chat.id)]=prov(globalcity[sl.index(message.chat.id)],ost[sl.index(message.chat.id)]) #Проверка 2
                                #if prevost!=ost[sl.index(message.chat.id)]:
                                        
                                       # bot.send_message(message.chat.id,("Внимание!"))#\nВ базе бота закончились города, начинающиеся с буквы "+str(list(prevost.difference(ost))[0])+".\nИспользуйте букву, стоящую перед ней"))
                               # print(ost[sl.index(message.chat.id)],prevost)
                                break
                

        else:
            bot.send_message(message.chat.id,"Данный город не соответствует правилам игры")
            if n[sl.index(message.chat.id)] in globalcityb[sl.index(message.chat.id)]:
                bot.send_message(message.chat.id,"(Такой город уже был)")
            elif n[sl.index(message.chat.id)] not in globalcityb[sl.index(message.chat.id)] and n[sl.index(message.chat.id)] not in globalcity[sl.index(message.chat.id)] and p[sl.index(message.chat.id)]!=1:
                bot.send_message(message.chat.id,"(Такого города не существует или он отсутствует в базе)")
            elif n[sl.index(message.chat.id)] not in globalcityb[sl.index(message.chat.id)] and n[sl.index(message.chat.id)] not in globalcity[sl.index(message.chat.id)] and p[sl.index(message.chat.id)]==1:
                    bot.send_message(message.chat.id,"(Такого города не существует или он отсутствует в базе)")
                    p[sl.index(message.chat.id)]=0
            elif n[sl.index(message.chat.id)] in globalcity[sl.index(message.chat.id)]:
                bot.send_message(message.chat.id,"(Первая буква названия данного города не является последней буквой названия предыдущего города)")
            bot.send_message(message.chat.id,"Попробуйте другой:")
            

        



bot.polling(none_stop=True, timeout=123)
