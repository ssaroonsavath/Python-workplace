
#1) Declare a variable set to 4. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 1.

x = 4
while(x < 0):
    print(x)
    x -= 1
#2) Declare a variable set to 14. Make a while loop that prints the variable 
#    you just created and increments the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 20.

i = 14
while(i < 0):
    print(i)
    i -= 20


#3) Declare a variable set to 55. Make a while loop that prints the variable 
#   you just created. Then make an if statement that makes the loop break when
#   the variable is equal to 50. 

b = 55
while(b < 0):
    print(b)
    if(b == 50):
        break

'''For Loops'''
#4) Create a list named sports. Put three sports into the list. Create
#   a for loop that prints each sport in the list

sports = ["Baseball", "Basketball", "Volleyball"]

for x in sports:
    print(x)


#5) Create a for loop that loops through each letter in a string of one of your
#   favorite songs. Each iteration should print should a letter of the word. 

song = "Life goes on"

for x in song:
    print(x)


#6) Create a list named movies. Put five of your favorite movies into the list.
#   However, make sure one of the movies is Avatar. 
#   Create a for loop that iterates over the list. In the loop print the movie
#   being looped over, but create an if statement that breaks out of the 
#   loop if it is Avatar.


movies = ["Train of Busan", "Avatar", "Rush Hour 2", "Om Shanti Om", "The Man From Nowhere"]

for x in movies:
    print(x)
    if(x == "Avatar"):
        break
        

