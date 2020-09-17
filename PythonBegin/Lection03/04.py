class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "%5d\t%s" % (self.age, self.name)

lst = [Person('Иван', 22)]
men = Person('Август', 12)
lst.append(men)
lst.append(Person('Максим', 33))

for item in lst:
    print(item)

lst.sort(key = lambda item: item.name, reverse=True)

for item in lst:
    print(item)