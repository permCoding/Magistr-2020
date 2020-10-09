import os

os.system('cls')
path =  os.getcwd()
name_file = path + r'\data.txt'

file = open(name_file, mode='r')
lines = file.read().split('\n')
file.close()

# print('\n'.join(lines))
for line in lines:
    print(line)
