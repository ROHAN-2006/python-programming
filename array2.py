fruits=["apple","banana","cherry"]
cars=["bmw","volvo","ford"]
fruits.append("orange")

x=fruits.copy()
print(x)

x=fruits.count("orange")
print(x)

fruits.extend(cars)
print(fruits)

x=fruits.index("cherry")
print(x)

fruits.pop(1)
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

fruits.remove("cherry")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)