# store a value
# data type
# int, string, char, float, double
# allocate the memory, what kind of data

# dynamic binding

# memorylocation -> container -> store -> access with name -> variable name

name = 'Python'
# variablename = value

# python dynamic binding

x = 1
print(name)
print(x)

print("Name of the program", "String2")

print("Name of the program :", "name")
print("Name of the program :", name)

# string, int, float
print(type(name))
print(type(x))
x = 1.113
print(type(x))
x = True
print(type(x))
x = 4 + 2j
print(type(x))


a = 10
b = 20
c = 21
print(a,b,c)

a, b,  c = 1001, 2001, 3001
print(a,b,c)

a = b = c = 'Python'
print(a,b,c)

l1 = ['collection', 'of ', 'element', 12, 2.6, True]
print(type(l1))

print(l1)

for i in l1:
    print(i)


l2 = []
print(l2)

l3 = list()
print(l3)

l1 = [1,1,1,1,2,2,4,5,1,2,13,1,4141,25,1,212,1,2,5435]
print(l1)

print("Total length of the list l1 is",len(l1))
x = len(l1)
print("Total length of the list l1 is ", x)
print(f"Total length of the list l1 is x ")
print(f"Total length of the list l1 is {x} ")



print(f"Name of the training program is {name} and It starts on {x}")

l1 = [12,23,45,56,67,78,89]
print(l1)
# to add at the end
l1.append(112)
print(l1)
l1.insert(5, 102)
print(l1)

print(l1.pop())
print(l1)
# print(l1.pop())
# print(l1)
# print(l1.pop())
# print(l1)
# print(l1.pop())
# print(l1)

l1 = [0,1,2,3,4,5,6]
print(l1)
# del l1[3]
print(l1)

# del l1
# print(l1)

l2 = ['A','B','C']

print(l1)
print("len(l1)",len(l1))
l1.append(l2)
print(l1)
print("len(l1)",len(l1))
l1.pop()
l1.extend(l2)
print(l1)
print("len(l1)",len(l1))



l1 = [1,1,1,1,2,2,4,5,1,2,13,1,4141,25,1,212,1,2,5435]
print(l1)

l1.sort(reverse=True)
print(l1)

l1 = [1,2,3]
l2 = ['A','B','C']
l3 = l1 + l2
print(l3)

l4 = list()
for x in l1:
    l4.append(x)
for x in l2:
    l4.append(x)
print(l4)