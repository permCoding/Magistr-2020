import os

os.system('cls')
path =  os.getcwd()

name_file = path + r'\data.txt'

file = open(name_file, mode='r')
line = file.readline()
file.close()

print(line)

