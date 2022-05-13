''' Sort Python Dictionaries by Key or Value 
 - Using Lambda Function
 - Using Item Getter
'''

'''
sorting using the lambda function and using “sorted()” inbuilt function.
'''

myList = [
    {
        'name':'rohan',
        'age':20
    },
    {
        'name':'tanmey',
        'age':21
    },
    {
        'name':'neel',
        'age':18
    },
    {
        'name':'abc',
        'age':25
    }
]

print(sorted(myList, key = lambda i: i['age']))
print(sorted(myList, key = lambda i: i['name']))

'''
It takes keys of dictionaries and converts them into tuples. It reduces overhead and is faster and more efficient.
'''

from operator import itemgetter

print(sorted(myList, key = itemgetter('age')))
print(sorted(myList, key = itemgetter('name')))