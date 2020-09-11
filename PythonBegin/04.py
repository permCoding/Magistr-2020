lst = [1, 2, 3, 4]
tpl = tuple(lst)

print(*tpl)

a = 3; b = 5
(a, b) = (b, a)
print(a, b)

tpl = (1, 'klahwe', 3)
print(*tpl)
for item in tpl:
    print(item, end='', sep='')