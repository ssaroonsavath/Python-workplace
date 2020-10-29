

'''
The goal of this function is to calculate the area of a circle. 

The function gets a radius from the user and then calculates the area.
'''

def circleArea():
    radius = input("What is the radius of your circle?")
    
    pi = 3.14
    squared = radius * radius 
    area = pi * squared
    print("The area is:" + area)
    return area 

'''
This function calculates the area of a rectangle. 
This function gets a height and width from the user and then calculates the area.
'''
def rectangleArea():
    height = input("What is the height of your rectangle?")
    width = input("What is the width of your rectangle?")
    
    area = height * width
    print(area)
    return area
