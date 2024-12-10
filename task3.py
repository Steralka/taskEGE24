s = open(r"24.txt").readline() # открываем файл и читаем строку 
c = 0 # счетчик
for i in 'BEKMHOPCTYX': # делаем перебор подходящих букв для номера автомобиля
    s = s.replace(i, 'A') # заменяем все подходящии буквы на одну подходящую
for i in range(len(s) - 5): # делаем перебор по длине s - 5 т.к. в дальнейшем будем рассматривать на 5 символов вперед 
    d = s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] + s[i + 5] # собираем якобы номер автомобиля 
    if d[0] + d[4] + d[5] == 'AAA': # проверяем буквы автомобиля на местах, где должны быть только буквы (на 1, 5, 6 местах | по индиксу 0, 4, 5), чтобы были только подходящии. 
        if (d[1] + d[2] + d[3]).isdigit() and (d[1] + d[2] + d[3]) != '000': # 1 способ
# первой проверкой мы проверяем на местах, 
#где должны быть цифры автомобиля (на местах 2, 3, 4 | по индиксу 1, 2, 3), являлись только цифры с помощью .isdigit(). Второй проверкой мы проверяем на местах, где должны быть цифры, чтобы не было 000 (по усл. задачи).
# '000' делается, потому что проверяем строку в тип данных str. 
# *Можно было переписать алгоритм проверки на трех нулей (000).
    # Второй способ
        #if (d[1] + d[2] + d[3]).isdigit():
        #   if int(d[1] + d[2] + [3]) > 0:
        #       c += 1
            c += 1 # +1 к счетчику
print(c) #вывод результата