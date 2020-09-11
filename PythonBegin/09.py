def get_int(s):
    return int(s)

s = "1 2 3 4 5 6"

# 0
# lst = s.split()
# res = []
# for item in lst:
#     res.append(int(item))

# print(res)

# 1
lst = list(map(int, s.split()))
print(lst)
# 2
lst = list(map(get_int, s.split()))
print(lst)
# 3
lst = list(map(lambda item: int(item), s.split()))
print(lst)

lst = list(filter(lambda item: int(item) % 2 == 0, s.split()))
print(lst)
