# In python a list is a built in data structure used to store an oredered, mutable collection of items.
# Lists are defined by enclosing a comma-separated sequence of items in square brackets [].

#example of a list
nums = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']

# Lets Mix those two lists
mix = [nums+fruits]
print(mix)

# lets try append 
nums.append(54)
print('we have appended the 54 at last of our list',nums)

# Lets try insert a number in between list 
nums.insert(1,69)
print('we have inserted the value 69 at the 1 index number of our list',nums)

#lets remove some values 
nums.remove(4)
print('we have removed some elements from here',nums)

# Lets try pop
nums.pop(2)
print('WE poped one element out of List' , nums)

# Lets try to add multiple values at same time 
nums.extend([45,63,34,54,78,120])
print('here wee can add multiple elements in our list ',nums)

# lets sort this list

nums.sort()
print('Here we get our sorted list : ',nums)

# lets reverse this list 

nums.reverse()
print('We have reversed the list using .reverese method : ',nums)


# lets find minimum & maximum value of this list 

minval = min(nums)
print('here we got our minimum value from list ',minval)
maxval= max(nums)
print('here we got our maximum value from list ',maxval) 

#lets do sum on list

sumval = sum(nums)
print('This is the sum of our given list : ',sumval)