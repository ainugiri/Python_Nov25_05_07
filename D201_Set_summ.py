s1 = {1,2,3,4,5,5,1}
print(s1)
s1.remove(5)
s1.add(55)
print(s1)
s2 = s1.copy()
s1.clear()
print("set s1",s1)
print("set s2",s2)

s2.remove(55)
print(s2)

s2.discard(55)
# s2.remove(55)
print(s2.pop())
print(s2)

newset1 = {'A',"B","C"}
s1.update(newset1)
s1.update(s2)
print(s1)