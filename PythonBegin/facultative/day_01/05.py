import os

os.system('cls')
path =  os.getcwd()
name_file = path + r'\data.txt'

file = open(name_file, 'r')
lines = file.read().split('\n')
file.close()

persons = []
for line in lines:
    lst = line.split(' ')
    persons.append(lst)
'''
['2', 'Филимонов', '26', '3.2'] - это неправильно
['2', 'Филимонов', 26, '3.2'] - надо так
[2, 'Филимонов', 26, 3.2] - а в идеале так
'''
persons.sort(key=lambda item: item[2])

for person in persons:
    print(person)

