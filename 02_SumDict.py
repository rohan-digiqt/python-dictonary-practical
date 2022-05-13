''' Python program to find the sum of all items in a dictionary '''


def sum(myDict):
    lis = []
    for i in myDict:
        # print(myDict[i])
        lis.append(int(myDict[i]))
    ans = sum(lis)
    print(ans)

a = {
    'n1':10,
    'n2':20,
    'n3':30
}

sum(a)

