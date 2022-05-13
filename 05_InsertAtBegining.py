''' Insertion at the beginning in Ordered Dict '''

# Using OrderedDict.move_to_end() 

from collections import OrderedDict

ord_dict = OrderedDict([('Rohan',44),('Tanmay',55)])

ord_dict.update({'Neel':49})

ord_dict.move_to_end('Neel', False)

print(str(ord_dict))