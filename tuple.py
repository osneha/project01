print("")
print("Tuple example")
tuple = 'John', 'Green', '3.3'
print(tuple)
print(tuple[1])
tuple += ('Csis','Maryville')
print(tuple)
print("")

print("Student tuple example")
student_tuple = ('Amanda', [98, 85, 87])
first_name, grades = student_tuple
number1, number2, number3 = grades
print(student_tuple)
print(first_name)
print(grades)
print(number1)
print(number2)
print(number3)
print("")

# fig05_01.py
print("Displaying a bar chart")
numbers = [19, 3, 15, 7, 11]
print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')

print("")

print("example using list slicing")
num = list(range(1,16))
print(num)
print(num[1:len(num):2])
num[5:10] = [0] * len(num[5:10])
print(num)
num[5:] = []
print(num)
num[:] = []
print(num)
print("")

print("example using del")
delNum = list(range(0,10))
print(delNum)
del delNum[0:3]
print(delNum)
print("")

print("example using function/items")
def modify_elements(items):
    for i in range(len(items)):
        items[i] *=2

funcNum = [10,3,7,1,9]
modify_elements(funcNum)
print(funcNum)
print("")

print("example using sort/orders")
orderNum = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(orderNum, "#unsorted")
orderNum.sort()
print(orderNum, "#sorted") 
orderNum.sort(reverse=True)
print(orderNum, "#reversed")
print("")

print("example of lexigraphical order")

foods = ['cookies', 'pizza', 'grapes', 'apple', 'steak', 'bacon' ]
print(foods, "#unsorted")
foods.sort
print(foods, "#sorted")
print("")

print("example of in and not in list-index-function")

another_Num = [3, 7, 1, 4, 2, 8, 5, 6]
if 1000 in another_Num:
    print("true")
else:
    print("False")

if 5 in another_Num:
    print("true")
else:
    print("False")







