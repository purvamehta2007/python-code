tuples = (67,78,90,45)
x = list(tuples)#we changed tuple to list
print(type(x))#it will print the type list
x.insert(1,49)#it will insert 49 at the index 1
x.append(99)#it will add 99
x.remove(90)#it will remove 90 from the list
x.pop()#it will remove the no. at the last  
x.pop(3)#it will remove the no. at index 3
x.append(99)
x.append(100)
x.append(86)
x.append(87)
print(x.index(78))#it will tell the index of 78
print(x)
yup = tuple(x)#it will change the list into tuple
print(yup)
print(type(yup))

