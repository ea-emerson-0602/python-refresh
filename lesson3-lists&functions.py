fruits=["apple","banana","cherry"]
numbers=[1,2,3,4,5]
mixed=["hello", 42, True]



print(fruits[0], fruits[-1])

fruits.append("grape")
fruits.insert(0, mixed)
fruits.pop(2)
for fruit in fruits:
    print (fruit)

for i in range(len(fruits)):
    print(fruits[i])

def greet(name):
    print(f"Hello, {name}")

greet("Aghogho")

def add(a,b):
    return a+b
result=add(3,8)
print(result)

def greet(name="guest"):
    print(f"Hello, {name}")

greet()
greet("Aghogho")