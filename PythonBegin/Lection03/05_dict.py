def get_parents(name):
    tpl = dct.get(name)
    if tpl != None:
        for item in tpl:
            if item != None:
                print(item)
                get_parents(item)


lst = [
    ("Карлсон", ("Миша", "Клава")),
    ("Миша" , ("Вова", "Света")),
    ("Клава", (None, "Оля"))
]

dct = dict(lst)
# print(dct.keys())
# print(dct.values())
# print(dct.get("Миша"))
name = "Карлсон"
get_parents(name)


