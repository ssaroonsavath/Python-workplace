
'''
def [nameOfFunction](parameter):
    code block
    return [variable/data]
    
start with letter 
camel casing 
any length, but short as possible
no key words
'''

'''
This function takes in two integer parameters and adds them together. Then,
it returns the sum of the parameters. 

parameters:two integer variables
function purpose: sums the parameters together
return: a integer sum of the parameters
'''

def sumTwoNums(numOne, numTwo):
    sum = numOne + numTwo
    return sum 

'''
This function takes a list parameter and prints out the contents of the list.
It doesn't return anything.
'''
def printList(list):
    for x in list:
        print(x)
    return 
'''
syntax error
'''
ef printList(list)
for x in list:
        print(x)
    return 


x = 2
y = 3
num = sumTwoNums(x, y)
print(num)


a = ["string", "string", "string"]
printList(a)

b = [True, False, True, False]
printList(b)





















