import unicodedata
a=open(r'Города.txt', encoding='utf8')
b=a.readlines()
city=set()
cityb=set()
n='prosto'

print("ЗДРАВСТВУЙТЕ. ВЫ ЗАПУСТИЛИ ПРОГРАММУ ДЛЯ ИГРЫ В ГОРОДА")
print('ЧТОБЫ УЗНАТЬ ПРАВИЛА ИГРЫ НАПИШИТЕ: ПРАВИЛА')
print("ЧТОБЫ ОСТАНОВИТЬ ИГРУ НАПИШИТЕ: СТОП")
print("ВЫ НАЧИНАЕТЕ ИГРУ:")

for j in b:
    i=j
    i=i.strip()
    city.add(str.lower(i.casefold()))
   
n=input()    
n=n.casefold()
if n=="ПРАВИЛА":
    print("ДАЁТСЯ КАКОЙ-ЛИБО ГОРОД. ОППОНЕНТ ДОЛЖЕН НАЗВАТЬ ДРУГОЙ ГОРОД, ПЕРВАЯ БУКВА НАЗВАНИЯ КОТОРОГО ЯВЛЯЕТСЯ ПОСЛЕДНЕЙ БУКВОЙ ПРЕДЫДУЩЕГО ГОРОДА. НАПРИМЕР: МОСКВА-АБАКАН-НОВОСИБИРСК-КАРАГАНДА-...")
    print("БУКВЫ 'Ё' В ИГРЕ НЕТ. ОНА ЗАМЕНЯЕТСЯ НА 'Е'")
    print("ВСЕ СЛОВА ПИШУТСЯ ЗАГЛАВНЫМИ БУКВАМИ")
    print("ГОРОДА НЕ ДОЛЖНЫ ПОВТОРЯТЬСЯ")
    print("ИСПОЛЬЗОВАТЬ ТОЛЬКО СУЩЕСТВУЮЩИЕ ГОРОДА")
    n=input()

n=n.strip()

while n not in city:
    print("(ТАКОГО ГОРОДА НЕ СУЩЕСТВУЕТ)")
    print("ПОПРОБУЙТЕ ДРУГОЙ:")
    n=input()


if n in city:
    for k in city:
        i=k
        d=k[len(k)-1]
        if d=='Ь' or d=='Ъ':
            d=k[len(k)-2]
        l=len(n)
        if n[l-1]=="Ь" or n[l-1]=="Ъ":
            l=l-1
        if n[l-1]==i[0]:
            i0=i[0]
            ii=i.capitalize()
            print(ii)
            cityb.add(i)
            cityb.add(n)
            city.remove(i)
            city.remove(n)
            break
        
while n!='stop' or n!='Stop' or n!='STOP':
    n=input().casefold()
    
    if n=="СТОП".casefold():
        break
    
    n=n.strip()
    
    if n in city and n[0]==d:
        for k in city:
            i=k
            
            l=len(n)
            if n[l-1]=="ь" or n[l-1]=="ъ":
                l=l-1
            if n[l-1]==i[0]:
                i0=i[0]
                d=k[len(k)-1]
                if d=='ь' or d=='ъ':
                    d=k[len(k)-2]
                ii=i.capitalize()
                
                print(ii)
                cityb.add(i)
                cityb.add(n)
                city.remove(i)
                city.remove(n)
                break

    else:
        print("ЭТОТ ГОРОД НЕ СООТВЕТСТВУЕТ ПРАВИЛАМ ИГРЫ")
        if n in cityb:
            print("(ТАКОЙ ГОРОД УЖЕ БЫЛ)")
        elif n not in cityb and n not in city:
            print("(ТАКОГО ГОРОДА НЕ СУЩЕСТВУЕТ)")
        elif n in city:
            print("(ПЕРВАЯ БУКВА НАЗВАНИЯ ЭТОГО ГОРОДА НЕ СООТВЕТСТВУЕТ ПОСЛЕДНЕЙ БУКВЕ НАЗВАНИЯ ПРЕДЫДУЩЕГО)")
        print("ПОПРОБУЙТЕ ДРУГОЙ:")
        
print("ИГРА ОКОНЧЕНА")
