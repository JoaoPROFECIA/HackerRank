#  Shopping Cart

import math
import os
import random
import re
import sys



class Item:
    # Implement the Item here
    def __init__(self, n='', p=0):
        self.name = n
        self.price = p
    
    def give_item(self, name, price):
        return name, price


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self, name0='', price0=0):
        self.nameI = name0
        self.priceI = price0
        self.name_list = []
        self.price_list = []
    
    def call_Item(self, nameI, priceI):
        nout, pout = Item.give_item(self, nameI, priceI)
        return nout, pout
    
    #  Append items to the cart
    def add(self, nameI, priceI):
        nout, pout = self.call_Item(nameI, priceI)
        
        self.name_list = self.name_list + [nout]
        print('Your cart contains: ', self.name_list)
        
        self.price_list = self.price_list + [pout]
        return self.name_list, self.price_list
    
    def total(self):
        tot_out = sum(self.price_list)
        print('Total shopping cart: ', tot_out)
        print(tot_out)
        return tot_out
        
    def num_of_cartitems(self):
        num_items = len(self.name_list)
        print('Total shopping cart items: ', num_items)
        print(num_items)
        return num_items
    

        
obj = ShoppingCart()
n_list, p_list = obj.add('nuts', 2)
n_list, p_list = obj.add('crackers', 3)
n_list, p_list = obj.add('juice', 3)
obj.total()
obj.num_of_cartitems()
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
