'''
Q-1)WHAT IS METRICS?
ANS)METRICS IS AN ARRANGEMENT INTO ROWS AND COLUMNS IN RECTANGULAR FORM

Q-2)WHAT ARE THE DIFFERENT TYPES ARRAY?
ANS)
 ONE DIMENSIONAL ARRAY :A one-dimensional array (or single dimension array) is a type of linear array. Accessing its elements involves a
single subscript which can either represent a row or column index.
As an example consider the C declaration int anArrayName[10]; which declares a one-dimensional array of ten integers.

MULTI DIMENSIONAL ARRAY :The two-dimensional array can be defined as an array of arrays. The 2D array is organized as matrices which can be represented 
as the collection of rows and columns.However, 2D arrays are created to implement a relational database lookalike data structure.(used to create games)

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

Q-4)WHAT IS ARRAY?
ANS)array are mostly immutable data structure whose length cannot be changed once created and the mutable array is called list.
'''
var = (20,25,35,67,89,100)
print(type(var))
print(var[:-1])
print(var[-1:])
print(var[0:])
print(var[0:9])
print(var[0:-1])
