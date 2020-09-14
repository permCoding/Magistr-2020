list_A = ["AAA", "BBB", "CCC"]
list_B = list(range(100))

list_AB = list(zip(list_A, list_B))

print(list_AB)

# [('AAA', 0), ('BBB', 1), ('CCC', 2)]