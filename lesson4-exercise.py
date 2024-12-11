car={
    "brand":"Koenigsegg",
    "model":"Agera",
    "year":2015,
    "price":500000,
}

print(car["brand"])
car["price"]=600000

car["color"]="black"

car.pop("year")
print(car)
for detail in car:
    print(detail, car[detail])

for key, value in car.items():
    print(key, value)

fruits_string="apple banana apple orange banana apple"
fruits=fruits_string.lower().split()
word_count={}
for fruit in sorted(fruits):
    if fruit in word_count:
        word_count[fruit]+=1
    else:
        word_count[fruit]=1
print(word_count)

cars={
    "brand":"Koenigsegg",
    "model":"Agera",
    "year":2015,
    "price":500000,
}
