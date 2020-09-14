lst = [('AAA', 66), ('BBB', 1), ('CCC', 2)]

sorting_list = sorted(lst, key = lambda item: item[1], reverse=True)

print(sorting_list)