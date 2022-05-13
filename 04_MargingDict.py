''' Merging two Dictionaries '''

d1 = {'Rohan':44, 'Tanmay':45}
d2 = {'Neel':49, 'Vijay':69}


# Using Update

d2.update(d1)

print(d2)

# Using **

d2 = {'Neel':49, 'Vijay':69}

ans2 = {**d1,**d2}
print(ans2)