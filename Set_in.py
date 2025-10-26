# Creating a set 
fruits = {"apple","banana","cherry"}
print(fruits)

# Sets using "set()" Constructor
list = set([1,24,5,67,8,90])
print(list)

#Basic Concepts
# Add & Remove the elements
fruits.add("Mango")
fruits.remove("cherry")
print(fruits)

#Union sets (Combine Sets)(a|b)
a = {1,2,4,5,8,9}
b = {1,5,10,22,23,45,67}
print(a.union(b))               # Or you can also use  print(a|b)

# Intersection Sets(Common Sets) (a & b)
print(a.intersection(b))        # or you can also use   print(a & b)

# Symmetric Difference Sets(elements not common a^b )
print(a.symmetric_difference(b))    # or you can also use   print (a^b)
