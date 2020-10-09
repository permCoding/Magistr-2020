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

# = = = = = = = = = = = = =
     
def get(item):
    return item[1]

persons.sort(key=get)

# persons.sort(key=lambda item: item[1])

for person in persons:
    print(person)
