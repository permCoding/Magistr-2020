# решение задачи о максимизации прибыли
d = [0, 1, 1, 2, 4]  # дедлайны
c = [2, 5, 4, 1, 3]  # стоимости

z = list(zip(d, c))
z.sort(key=lambda item: -item[1])

days = [False] * (max(d) + 2)  # False свободен
max_price = 0  # тут будет ответ
for item in z:
    day = item[0] + 1
    while day and days[day]:
        day -= 1
    if day:
        days[day] = True
        max_price += item[1]

print('max Price =', max_price)
# [(1, 5), (1, 4), (4, 3), (0, 2), (2, 1)]

'''
тут лишний элемент - (max(d) + 2) - в days слева
а номера дней в списке days смещены поэтому на 1 вправо
номера дней начинаются с 1, поэтому: day = item[0] + 1
движемся пока номер дня не 0 и день занят: 
    while day and days[day]
и в конце добавляем в max_price если день не ноль
так как у нас дни с единицы
'''
