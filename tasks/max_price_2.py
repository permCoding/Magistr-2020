# решение задачи о максимизации прибыли
d = [0, 1, 1, 2, 4]  # дедлайны
c = [2, 5, 4, 1, 3]  # стоимости

z = list(zip(d, c))
z.sort(key=lambda item: -item[1])

days = [False] * (max(d) + 1)  # False свободен
max_price = 0  # тут будет ответ
for item in z:
    day = item[0]
    while days[day]:
        if day > -1:
            day -= 1
        else:
            break
    if day > -1:
        days[day] = True
        max_price += item[1]

print('max Price =', max_price)
# [(1, 5), (1, 4), (4, 3), (0, 2), (2, 1)]

'''
версия с бряком
'''
