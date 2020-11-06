biodata ={
    'vaani' : {
        'course' : 'python',
        'mobile' : 9899898932,
    },
    'poorva' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
    'seeta' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
    'geeta' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
    'meeta' : {
        'name' : 'poorva',
        'course' : 'ai',
        'mobile' : 9899898932,
    },
}
biodata.popitem()
biodata.pop('vaani')
keys=['mobile','subjcet']
values=[97685949,'maths']
print(biodata.fromkeys(keys,values))
print(biodata.setdefault('hello'))
biodata['hello']=456
print(biodata.get('seeta'))
print(biodata.update( ))
print(biodata)
