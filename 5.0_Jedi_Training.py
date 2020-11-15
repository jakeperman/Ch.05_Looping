  #Sign your name:________________
import random
'''
 1. Make the following program work.
   '''

print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x

print("The total is:", total)

  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2, 102, 2):
    print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i = 10
while i in range(0, 11):
    print(i)
    i += -1






'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
print(random.randrange(1, 11))





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total = 0
neg = 0
pos = 0
zer = 0
for i in range(7):
    x = int(input("Enter a number: "))
    if x < 0:
        neg += 1
    elif x > 0:
        pos += 1
    else:
        zer += 1
    total = total + x

print("The total is: ", total)
print("You entered ", pos, " positive numbers")
print("You entered ", neg, "negative numbers")
print("You entered ", zer, "zeroes")
