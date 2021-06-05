

c = [-45, 6, 0, 72, 1543]

print(c)
print(c[0])
print(c[4])
print(len(c))
print(c[-1])
#print(c[100]) Throws error
print(c[0]+c[1]+c[2])

a_list = []
for number in range(1,6):
    a_list += [number]
print(a_list)

list1 = [10, 20, 30]
list2 = [40, 50]

concatenate_list = list1 + list2
print(concatenate_list)

for i in range(len(concatenate_list)):
    print(f'{i}: {concatenate_list[i]}')

a = [1,2,3]
b = [1,2,3]
c = [1,2,3,4]

if a == b:
    print("True")
if a == c:
    print("True")
else: 
    print("False")
if a<c :
    print("True")
if c>=b :
    print("True")




