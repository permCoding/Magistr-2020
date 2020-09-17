n = int(input())

# способ 1
# b = bin(n)[2:]
# k = b.count('1')
# bin_max = '1'*k + '0'*(len(b)-k) 

# print(int(bin_max, base=2))

# способ 2
b = bin(n)[2:]
lst = list(b)
print(int(''.join(reversed(sorted(lst))), 2))



# lst.sort()
# new_lst = sorted(lst)