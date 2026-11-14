import inflect
p = inflect.engine()

names = []
name = "abc"

while name != "":
    name = input("names: ")
    names.append(name)
    print(names)

names.pop() 
print("Adieu, adieu, to " + p.join(names))