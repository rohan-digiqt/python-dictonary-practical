''' Sort Dictionary key and values List '''


''' Using Sorted '''

mydict = {"Rohan" : [44], "Dharam" : [45], "Neel" : [49], "Vijay" : [69]}

ans = {}

# y = sorted(mydict)
# print(y)

for key in sorted(mydict):
    ans[key] = sorted(mydict[key])
print(ans)

''' Using dictionary comprehension + sorted() '''

ans2 = {key : sorted(mydict[key]) for key in sorted(mydict)}  
print(ans2)