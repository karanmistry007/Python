a="MISSISSIPPI"
dict={"M":0,"I":0,"S":0,"P":0}
for i in a:
    if  i == 'M':
        dict['M']=dict['M']+1
    elif  i == 'I':
        dict['I']=dict['I']+1
    elif  i == 'S':
        dict['S']=dict['S']+1
    elif  i == 'P':
        dict['P']=dict['P']+1

print(dict)