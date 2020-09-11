
lst = []
lst = [1, 2, 3, 4]
lst = list(range(10))

print(lst)
print(*lst)

lst = [num for num in range(10) if num % 2 != 0]

print(lst)
print(len(lst))

lstA = [1, 2, 3, 4, 5]
lstB = lstA[0:len(lstA)]
# lstC = lstA[:]
lstC = lstA.copy()
lstD = lstA

lstD[0] = 666
lstC[1] = 999
print(lstA)
print(lstB)
print(lstC)
print(lstD)







# print(lst[:])
# print(lst[::2])
# print(len(lst))

