# CREATE LIST AND EDIT LIST
movies=["300", "Stranger Things", "Game of thrones", "Lord of the Rings"]
new_movies=["Breaking Bad", "Final Destination"]
movies.extend(new_movies)
movies.pop(0)
movies[-1]="inception"
print(movies)


# CREATE LIST OF INTEGERS WITHIN A FIXED RANGE
integers=list(range(10,21))
print(integers)

# SUM NUMBERS IN A LIST
sum=0
for i in integers:
    sum+=i
print(sum)

# MULTIPLY NUMBERS IN A LIST
product=1
for i in integers:
    product*=i
print(product)

#CHECK IF LIST NUMBER ITEM IS EVEN OR ODD
for x in range(1,51):
    if x%2==0:
        print(x)


# REVERSE STRING
normal=input("Type in a string and i will work my magic:")
reversed=""
index=len(normal)-1
while index>=0:
    reversed+=normal[index]
    index-=1
print(reversed)


#MULTIPLIER FUNCTION
def multiply(a,b):
    return a*b

first=int(input("Write a number:"))
second =int(input("Write another number: "))

print(f"The products of your numbers is: {multiply(first, second)}")


# EVEN OR ODD FUNCTION
def is_even(a):
    if a%2==0:
        print(f"The number {a} is an even number")
        return True
    else:
        print(f"The number {a} is an odd number")
        return False

true_or_false=int(input("Give me a number, I will tell you if it is even or not: "))
print(is_even(true_or_false))


# SUM AND PRODUCT FUNCTION
def find_sum_and_product(a):
    sum = 0
    products = 1
    for i in a:
        sum+=i
        products*=i
    print(f"Sum={sum}, product={products}")
list=[1,2,3,4,5]
find_sum_and_product(list)


# USER INPUT TO POPULATE A LIST
grades=[]
limit=0
while limit>=0:
    grade=(int(input("Write the grade in number")))
    if grade<0:

        break
    grades.append(grade)
print(grades)


# FUNCTION TO FIND HIGHEST NUMBER IN LIST
def highest_grade(grades):
    max_grade = grades[0]
    for grade in grades:
        if grade >= max_grade:
            max_grade = grade
    return max_grade
print(f"Highest grade: {highest_grade(grades)}")


# FUNCTION TO FIND LOWEST NUMBER IN LIST
def lowest_grade(grades):
    min_grade=grades[0]
    for grade in grades:
        if grade <= min_grade:
            min_grade=grade
    return min_grade
print(f"Lowest grade: {lowest_grade(grades)}")


# FUNCTION TO FIND AVERAGE OF LIST
def average_grades(grades):
    sum =0
    for grade in grades:
        sum+=grade
    return sum/len(grades)
print(f"Average grade: {average_grades(grades)}")


# EDITING LIST IN DESCENDING ORDER
descending_grades=sorted(grades, reverse=True)
print(f"The grades in descending order is: {descending_grades}")
