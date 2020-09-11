st = set()
st.add(1)
st.add(2)

print(*st)

st = {1, 2, 3, 4}
st.add(1)
st.add(1)
st.add(9)
print(*st)

st_a = {1, 3, 5}
st_b = {2, 4, 6}
# st_a.remove(9)
# st_a.discard(9)
print(st_a)
st_c = st_a.union(st_b)
print(st_c)