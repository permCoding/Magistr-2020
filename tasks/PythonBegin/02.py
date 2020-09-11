
lst = []
lst = [1, 2, 3, 4]
lst = list(range(10))

print(lst)
print(*lst)

lst = [num for num in range(10) if num % 2 != 0]
print(lst)