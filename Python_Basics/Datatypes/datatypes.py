eid=101
esal=45000.45
ename='Rahul'
avail = False
c=10+20j
loc=['Wayanad','New Delhi','Banglaore'] #mutable
color=('R','B','G')  #mutable
eids={101,102,103,104} #mutable
emp={
    'id':101,
    'name':"Rahul Gandhi"
} #mutable
b = bytes([100,110,120,130])
ba=bytearray([100,110,120,130]) #mutable
fz=frozenset([101,102,103])
r = range(10)

def add():
    pass

print(type(eid))
print(type(ename))
print(type(esal))
print(type(avail))
print(type(c))
print(type(loc))
print(type(color))
print(type(eids))
print(type(emp))
print(type(b))
print(type(ba))
print(type(fz))
print(type(r))
print(type(add()))


