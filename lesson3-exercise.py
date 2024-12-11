
# BASIC LOOP OPERATIONS
fav_colors=["red", "blue","black","gray","purple"]
fav_colors.append("brown")
# fav_colors.insert(1,"cyan")
fav_colors[1]="cyan"
fav_colors.pop()
print(fav_colors)

# LOOPING THROUGH LISTS
numbers_list=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(numbers_list)):
    numbers_list[i]*=2
print(numbers_list)

doubled_list=[number*2 for number in numbers_list]
print(doubled_list)

# FUNCTIONS
def greet_user(name):
    print(f"Hello, {name}")

greet_user(input("What is your name? "))

def square(a):
    return a**2
result=square(int(input("Think of a number, and I'll square it: ")))

print(f"Your number squared is: {result}")




# CHALLENGE
# function to find the largest number in a list
def find_max(numbers):
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num
numbers=[2,1,5,3,6,9,1]

print(max(numbers))
print(f"The largest number is: {find_max(numbers)}")