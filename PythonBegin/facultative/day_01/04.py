import os

os.system('cls')
path =  os.getcwd()
name_file = path + r'\data.txt'

file = open(name_file, 'r')
lines = file.read().split('\n')
file.close()

persons = []
for line in lines:
    persons.append(line.split(' '))


persons.sort(key=lambda item: item[2])

for person in persons:
    print(person)

# for i in range(20, 57):
#     print(i, '\t', chr(i))
