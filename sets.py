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
'''
Question:
1. How many words in Oxford dictionary?
ans)Oxford Dictionary has 273,000 headwords;
171,476 of them being in current use, 47,156 being obsolete words
and around 9,500 derivative words included as subentries.

2. diff b/w pop and remove?
ans)pop
The pop() function takes either no parameter or the index value as its parameter.
When no parameter is given, this function pops() the last element and returns it.
When you explicitly supply the index value, the pop() function pops the required elements and returns it.

remove
The remove() function, on the other hand, is used to remove the value 
where we do not need the removed value to be returned. This function 
takes the element value itself as the parameter. If you give the index value in the
 parameter slot, it will throw an error.

3. why pop method is not good for set?
This in-built function of Python helps to pop out elements from a set just like
the principal used in the concept while implementing Stack. This method 
removes a random element from the set and returns the removed element. 
Unlike, a stack a random element is popped off the set. This is one of the
basic functions of the set and accepts no arguments. The return value is
the popped element from the set. Once the element is popped out of the set,
the set loses the element and it is updated to a set without the element.


4. diff b/w remove and discard method?
ans)The discard() method in Python removes a specified element from the Set.
The remove() method raises an error when the specified element doesn't exist in 
the given set, however the discard() method doesn't raise any error if the specified 
element is not present in the set and the set remains unchanged.


5. diff b/w union and update method?
ans)It is very similar to union() method, with difference is that where union() method
create and return a new set, containing all the elements ( distinct ) present in all the iterables,
update() method updates the set on which this method is called with all the distinct elements present
in all the iterables.
'''









