file = open('input.txt', 'r')
new_line = chr(10)
text = file.read()
lines = text.split(new_line)
file.close()

# print(text)
# for symb in text:
#     print(ord(symb), '\t',symb)

for line in lines:
    print(line)