#MYLIST IS A VARIABLEIN WHICH WE ARE GOING TO PERFORM METHODS
mylist=['ram','sita','meeta']
mylist.insert(1,'vani')#this method will insert "vani" at 1 index value
mylist.remove('ram')#it will remove "ram from the list"
mylist.pop()#it will remove the last character
mylist.sort()#it will sort all the characters in alphabetical form
mylist.reverse()#it will reverse the order
print(mylist.index('sita'))#it will tell the index value of 'sita'
python=mylist.copy()#it shift the characters from mylist to python
print(mylist)
print(python)
python.pop(-1)#it will pop the character at the -1 index
new=['jasmine','serena','taylor']
python.extend(new)#it will extend mylist by adding the characters in
#variable new
print(python)
