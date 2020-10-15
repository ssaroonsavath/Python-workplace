
''' The goal of this function is to calculate the volume 
of an object, when the user inputs height, width, and depth.

The function should print the sentence plus the volume and return 
the volume. 
'''

def volumeCalculator(height,width,depth):
    area = height * width 
    volume = depth * area 
    sentence = "The volume of this object is:"
    print(sentence + volume)
    return volume



'''
The goal of this function is to calculate the total of an order after tax and shipping 
The function should be print and return the total
'''

def shippingAndTax(subTotal):
    shipping = 10 
    tax = .10 
    
    taxTotal = subTotal * tax
    total = subTotal + taxTotal + shipping 
    print("The total is: + total")
    return total




'''
The goal of this function is to calculate the total 
of an order after tax and shipping 
The function should print and return the total
'''

def circleArea(radius):
    pi = 3.14 
    area = pi * squared 
    print("The area is:" + area)
    return area





