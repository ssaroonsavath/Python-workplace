'''
Created on Jan 20, 2021

@author: ITAUser

boolean/comparison + logical operator + boolean/comparison

logical operator + boolean/comparison

simplifies to boolean

and 
or 
not
'''

#True      #True
4 == 4 and 5 == 5 
#True    

#False     #False   
2 == 4 and 5 == 5
#False


2 == 4 or 5 ==5 
#True

username = "savannah"
password = "mjw11343"

boolean = (username == "savannah") and (password == "mjw11343")

print(boolean)

2 < 3 or 5 < 10 
#True 

4 < 3 or 5 < 10 
#True 

4 < 3 or 3 < 2 
#False 

not 3 == 3 
#False 

not 4 == 5 
#True 

True and True 
#True 

True and False 
#False

print(False and False )