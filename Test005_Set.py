s1 = set()
# list []
# tuple ()
# set {}
print(s1)
s1 = {101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 102,103,104,105,111,112,113,114,115,101, 102,103,104,105,111,112,113,114,115}
print(s1)


chess = {1,2,3,4,8,11,13,18}
tennis = {1,2,3,7,8,9,18,19,20}
football ={2,4,6,8,10,12,14,16,18,20}

print("Chess alone" , chess - tennis - football)
print("Tennis alone" , tennis - football - chess)
print("Football alone" , football - chess - tennis)

print("Chess and Tennis - not football", chess.intersection(tennis)-football)
print("Football and Tennis - not chess", football.intersection(tennis)-chess)
print("Football and Chess - not Tennis", football.intersection(chess)-tennis)

l1 = [1,23,4]
s2 = set(l1)
print(s2)


