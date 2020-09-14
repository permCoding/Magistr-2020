# list( map(func , lst) )
# filter( )
# 

# import functools as ft
from functools import reduce

lst = list(range(100+1))

def get_sum(x, y):
    return x + y

# ft.reduce(lambda acc, next_item: acc + next_item, lst)
sum = reduce(lambda acc, cur: acc + cur, lst, 0)
print(sum)

print(reduce(get_sum, lst, 0))
