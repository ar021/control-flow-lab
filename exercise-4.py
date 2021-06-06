# exercise-04 What kind of Triangle?

print('Enter the lengths of three side of a triangle:')
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a == b == c:
    print(f'A triangle with sides of {a}, {b} & {c} is a equalateral triangle')
elif a == b or a  == c:
    print(f'A triangle with sides of {a}, {b} & {c} is a isosceles triangle')
else:
    print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
