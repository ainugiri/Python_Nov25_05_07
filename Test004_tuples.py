l1 = list()
print(l1)

# tuples: ()
# allow duplicates, access with index(ordered)
t1 = tuple()
print(t1)

t1 = (1,2,3,'Giri', True, 2.131)
print(t1)
print(t1[3])

# at the index 2, value is 3. Change it to 'Python'
# t1[2] = "Python" ---> tuple' object does not support item assignment

templist = list(t1)
templist[2] = "Python"
t1 = tuple(templist)
print("Tuple starts and end with ( ): ",t1)

templist = list(t1)


print("List starts and end with [  ]: ",templist)

print(*t1)