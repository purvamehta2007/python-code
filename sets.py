#methods in python
s = {3,5,4,8,10,32}
t = {3,5,4,8,6,2}
print(type(s))
print(s.union(t))
print(s.intersection(t))
print(s.issubset(t))
print(t.issuperset(s))
print(s.symmetric_difference(t))
print(s.difference(t))
print(t.difference(s))
s.add(7)
print(s)

#programmes given by sir

#2.Set bana hain and set ko clear karna hain then usko delete kar dena hai.
temp = {'python','java','c+','R'}
print(temp.clear())
print(temp)
del temp




