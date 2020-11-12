#Programmes for practice:
#1. User se 2 input lo and check karo ki agar 1st input bada hai to useke liye message show karo otherwise second ke liye message show karo.
'''
var = input('\nenter the 1 st number : ')
temp = input('\nenter the 2 nd number : ')
if (var > temp):
    print('\n1st no. is greater')
elif (temp > var):
    print('\n2nd no. is greater')    
else:    
    print('INCORRECT')
'''    
'''
2. Ek shoping list banao, aur iske bad me check karo ki shoping list me who iteam hai ya nahi hai jo tum shop par jane ke bad shopkeeper se puch rahe ho. Iske liye product varaible create karna and then check karna hai.
Agar item list me hai then shopkeeper se uska price pucho?
Then agar price acceptable hain means yes or not wala case?
Then item ko purchase karo and show item bill, jisme ki-
    1. Item purchase date
    2. Item order number
    3. Item Price
    4. Item name
Included ho. Is ouput ko representative way me show karna hai.
'''
'''
3. user se name recive karna hai aur check karna hai ki agar user name
 me koi value deta hai to name print ho otherwise: 
please enter your name ka message show ho.
'''
name = input('please enter the name: ')
if bool(name) == True:
    print(name)
else:
    print('please enter the name')
'''
4. Program bana hai ki jisme 3 alag-alag number user se lene hai aur ye following condtion bana hai:
    a. agar first value greater hai then first user win
    b. agar second value greater then second user win
    c. same for thired user
    d. agar sabhi ke number same hai then tie ka message
    e. agar koi number galt enter hua to uska message
    f. sath me winer user ke liye ek alag se grand message aap ke tarike se jo bhi best output show kara sako.
'''
yaf = int(input('please enter 1st the number : '))
sar = int(input('please enter 2nd the number :'))
ram = int(input('please entre 3rd the number : '))
if (yaf > sar) and (yaf > ram):
    print('the first user wins')
elif (sar > yaf) and (sar > ram): 
    print('the second user wins')  
elif (ram > yaf) and (ram > sar):
    print('the third user wins')
elif (yaf == sar) or (yaf == ram) or (sar == yaf) or (sar == ram) or (ram == yaf) or (ram == sar):
    print('its a tie')        
else:
    print('wrong name')
'''
5. Ek friend list bana hai aur agar uske sath me condtion lagana hai ki:
    a. User kisi bhi random friend ko check karna chata hai ki kya wo party me hai ya nahi. Uski madad karo ye check karne me. 
    b. Agar friend party me nahi hai then User usko party me add karna cahta hai. Uski madad karo uske friend ko party me add karne ke liye.
    c. User, jis friend ko serach kar raha hai agar wo present hai to user ko uske bare me batao.
    e. User ek friend ko party se nikalna chata hai uski madad karo. Aur jab wo friend se nikal jaye to user ko batao ki wo friend party se gaya.
Note: In question ke liye aap ko apne hisab se soch kar program karna hai aur ye sare question ke liye abhi tak jo padha hai unhi ka use karna hai.
'''
people_party = ['ravi','lora','serena','selena','joe']
print(people_party)
check = input('please enter the name of the friends in party :')
if check in people_party:
    print('yes')
elif check not in people_party:
    print('no')
    people_party.append(check)
    print(people_party)
    print('your friend added in the party')
else:
    print('sorry cannot be done')

delete_friend = str(input('please let me know whether you want to remove anyone from the party(yes/no) : '))
which_friend = str(input('please enter the name of the friend whom you want to remove from the list?? : '))  
if delete_friend=='yes':
    print('ok')
    people_party.remove(which_friend)
    print('successfully process finished,',which_friend,'has been removed')
    print(people_party)
else:
    print('nobody will be removed from the list')

    


