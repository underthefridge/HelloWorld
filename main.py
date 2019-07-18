# Section 2. Basics

print("Hello World1")
print("Hello World2")
print("Hello World3")
print("Hello World4")
print("Hello World5")
print("Hello World6")
print("Hello World7")
print("Hello World8")
print("Hello World9")
print("Hello World10")


# 2.7 Variables & Variable Types

var1 = 500
var2 = 45.68
var3 = "Hello world"

a = b = c = 7

print (var1)
print (a)
print (b)
print (c)

print (var3)
print (var3[0])
print (var3[0:4])
print (var3[1:])

# 2.8 Lists

awesomeList = ["Hello", 45, "World", 4.5]

print (awesomeList * 8)
print (awesomeList + awesomeList)
print (awesomeList[3])
print (awesomeList[0:2])
print (awesomeList[0])
print (awesomeList[0:2])


# 2.9 Tuples

awesomeList = ["Hello", 45, "World", 4.5]

print (awesomeList * 8)
print (awesomeList + awesomeList)
print (awesomeList[3])
print (awesomeList[0:2])
print (awesomeList[0])
print (awesomeList[0:2])

awesomeList[3] = 6

print (awesomeList[3])


awesomeTuple = ("Hello", 45, "World", 4.5)

print (awesomeTuple * 8)
print (awesomeTuple + awesomeTuple)
print (awesomeTuple[3])
print (awesomeTuple[0:2])
print (awesomeTuple[0])
print (awesomeTuple[0:2])

# awesomeTuple[3] = 6
# print (awesomeTuple[3]) wont work because 'tuple' object does not support item assignment !

# 2.10 Dictionary

dictionary = {}
dictionary[1] = "Item1"
dictionary[2] = "Item2"
dictionary[3] = "Item3"
dictionary["Hello"] = "Item4"

print (dictionary[1])
print (dictionary[2])
print (dictionary[3])
print (dictionary["Hello"])

# ! nie mieszać różnych typów danych bo będzie wpierdol, tako rzecze Kmaku !

print (dictionary.values())
print (dictionary.keys())

newDicitonary = {1:"Item1", 2:"Item2", 3:"Item3"}

print (newDicitonary)

# 2.11 Data Type Conversion

var1 = 6.7

print (var1)
print (int(var1))

# 2.12 Arithmetic Operators

print (5 + 6)
print (5 - 6)
print (5 * 6)
print (5 / 6)

print (5 % 6)
print (9 % 4)
# 4 mieści się 2 razy w 9 = 8, 9-8=1

print (5**2)
# ** - potęgowanie

print (17//3)

# 2.13 Comparison Operators

print (5 == 5)
print (5 != 5)
print (5 > 6)
print (5 < 6)
print (5 >= 6)
print (5 <= 6)

# 2.14 Assignment Operators

var1 = 6 + 7
print (var1)

var1 = var1 + 5
print (var1)

var1 += 5
print (var1)

# 2.15 Bitwise Operators

var1 = 13   # 1101
var2 = 5    # 0101
#   13      1101
#   5       0101       
#           ----
#   AND     0101 (5)

print (var1 & var2)

#   13      1101
#   5       0101       
#           ----
#   OR      1101 (13)

print (var1 | var2)

#   13      1101
#   5       0101       
#           ----
#   XOR     1101 (8)

print (var1 ^ var2)

#   13                  1101     
# Ones Complement       0010 (2)

print (~var1)

# Binary shift left
print (var1 << 1)

# Binary shift right
print (var1 >> 1)


var1 = True
var2 = True
var3 = False
var4 = False

# AND logical operator
print ("AND logical operator")
print (var1 and var2)
print (var1 and var3)
print (var3 and var4)

# OR logical operator
print ("OR logical operator")
print (var1 or var2)
print (var1 or var3)
print (var3 or var4)

# NOT logical operator
print ("NOT logical operator")
print (not(var1))
print (not(var3))
print (not(var1 and var2))

#2.17 Membership Operators

string1 = "Hello World"

print ('H' in string1)
print ('Z' in string1)

print ('H' not in string1)
print ('Z' not in string1)

# 2.18 Identity Operators

var1 = 10
var2 = 10
var3 = 8

# IS Operator
print (var1 is var2)
print (var1 is var3)

# IS NOT Operator
print (var1 is not var2)
print (var1 is not var3)

# 2.19 Operator Precedence

# ** --> square
var1 = 5 ** 2 + 7
var2 = 5 + 7 ** 2

print (var1)
print (var2)

# 2.20 Decision Making / Conditional statements

var1 = 500

if (var1 == 500):
    print ("Var1 is equal to 500")
else:
    print ("No it does not equal a valid value")

if (var1 == 400):
    print ("Var1 is equal to 500")
else:
    print ("No it does not equal a valid value")

# can be in brackets or not - it doesn't really matter in this case

if var1 == 300:
    print ("Var1 is equal to 500")
else:
    print ("No it does not equal a valid value")

var1 = 500

if var1 == 500:
    print ("Var1 is equal to 500")
elif var1 == 400:
    print ("Var1 is equal to 400")
else:
    print ("No it does not equal a valid value")

if 500 == 500:
    print ("Yes")
else:
    print ("No")

if 400 == 500:
    print ("Yes")
else:
    print ("No")

if (var1 > 50):
    print ("Var1 is greater than 50")

# 2.21 Loops

var1 = "Hello World"
var2 = 100

for character in var1:
    print (character)

while (var2 < 110):
    print ("Less than 110")
    var2 += 1
else:
    print ("Not less than 110")

# 2.22 Loop Control Statements

var1 = "Hello World"

for character in var1:
    if character == " ":
        print ("There was a space, oh no")
        #cosiecosiecosiestao
        break
    print (character)

for character in var1:
    if character == " ":
        print ("There was a space, lets skip this iteration")
        #cosiecosiecosiestao
        continue
    print (character)

for character in var1:
    if character == " ":
        pass
        print ("Passing this over")
    print (character)

# 2.23 Numbers

import math

num1 = 5

print (math.exp(5))
print ( math.sqrt(5))
print (math.sin(math.pi/2))

# sprawdzam

# num1 = 5
# print (int(math.exp(5))

# a jednak nie

# 2.24 Strings

string1 = "will I ever understand dis?"

print (string1)
print (string1[0])
print (string1[0:4])

print (string1[:6] + ",bro?")

string2 = "I dunno"

print ("Hello \n World")

    # n is for starting from a new line

string3 = string1 + " " + string2
print (string3)

var1 = "Hello"
var2 = "World"

print ("%s this is the best %s" % (var1, var2))

ipsum = """We need to get all stakeholders up to speed and in the right place 
mobile friendly we need a recap by eod, cob or whatever comes first yet hard stop, so work. 
Killing it. Peel the onion single wringable neck low-hanging fruit. Spinning our wheels 
low-hanging fruit, onward and upward, productize the deliverables and focus on the bottom
line drink from the firehose, nor manage expectations we're ahead of the curve on that one 
and product management breakout fastworks. Viral engagement can you slack it to me?, 
but big boy pants yet rehydrate the team and we need more paper UI back of the net. 
Run it up the flag pole we need to future-proof this. Root-and-branch review action item. 
We need to button up our approach product management breakout fastworks thought shower, 
so if you could do that, that would be great so hard stop golden goose. We need to leverage our synergies.
Run it up the flagpole, ping the boss and circle back we need to button up our approach yet show pony, 
for today shall be a cloudy day, thanks to blue sky thinking, we can now deploy our new ui to the cloud on your plate, 
yet this proposal is a win-win situation which will cause a stellar paradigm shift, and produce a multi-fold increase in deliverables."""

print (ipsum)

# source: officeipsum.com/index.php

var4 = "yo Dawg"
print (var4.capitalize())

for x in range(10):
    print(x)
else:
    print("Is it working?")

for x in range(1, 10):
    for y in range(1, 10):
        print(x * y)
    else:
        print("still not working?")

for x in range(0, 3):
    print("\n")
    for y in range(0,3):
        print(x * y, end=" ")