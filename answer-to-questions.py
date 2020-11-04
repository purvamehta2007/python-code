'''
Q-1)WHAT IS METRICS?
ANS)METRICS IS AN ARRANGEMENT INTO ROWS AND COLUMNS IN RECTANGULAR FORM

Q-2)WHAT ARE THE DIFFERENT METHODS ARRAY?
ANS)
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

Q-3)WHAT IS THE DIFFERENCE BETWEEN POP AND POPITEM IN DICTIONARY?
pop method                                     popitem method
1.it takes the key as an                     1.it doesn't take the key as an
argument to delete the specified               argument to delete the specified key 
key value pair.                                value pair.

2.the syntax of pop()method is               2.the syntax of popitem()method is k, v=dictionary_name
dictionary_name.pop(key,default)                popitem()

3.it returns the popped value,if the         3.it returns the popped key value pair
element exists,=.Otherwise returns default 
value. 
'''
var = (20,25,35,67,89,100)
print(type(var))
print(var[:-1])
print(var[-1:])
print(var[0:])
print(var[0:9])
print(var[0:-1])