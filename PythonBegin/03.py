import array

lst = [1, 2, 3, 4]
arr = array.array('i', lst)

print(arr)
print(*arr)

arr.fromlist(lst)
arr.append(666)
arr.pop()
arr.pop()
print(*arr)
