names = "Nimish, Chavan"
print(names[0:6])
print(len(names))
# len function is used to calculate length of string

nm = "harry"
print(nm[-4:-2])

#diffrent string methods
#note : strings are immutable
a = "rock !!! "
print(a.upper())  #convert string to upper case
print(a.lower())  #convert string to lower case
print(a.replace("rock" , "john"))
print(a.split(" "))
print(nm.count("r"))
print(a.find("c"))