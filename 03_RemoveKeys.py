''' Python | Ways to remove a key from dictionary '''
mydict = {"Rohan" : 44, "Dharam" : 45, "Neel" : 49, "Vijay" : 69}

print(mydict)

del mydict['Vijay']
print(mydict)

mydict.pop('Neel')
print(mydict)