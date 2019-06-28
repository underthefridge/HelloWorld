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

 



