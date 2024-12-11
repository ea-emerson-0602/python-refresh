"""for i in range(1,7):
    if i == 6:continue
    elif i ==5:break
    print(i)

counter=1
while counter <=5:
    counter+=1
    print(counter)

for char in "python":
    if char=="t":break
    print(char)

colours=["red","blue", "yellow"]
for colour in colours:
    print(colour)
    """

age=int(input("What is your age?"))
if age < 13:print("You are a child")
elif age>12 and age<20:print("You are a teenager")
else:print("You are an adult")

for i in range(1, 20):
    print(i)

number = 1
while number <20 :
    number+=1
    if int(number>1) and number%2!=0:
        print(number)

word=input("What is your chosen word?")
for letter in word:
    print(letter)

total_sum=0
number=-1
while number:

    special_number = int(input("Choose a random number:"))
    if special_number==number:
        print(total_sum)
        break

    else:
        total_sum+=special_number