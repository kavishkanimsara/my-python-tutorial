####################################################################################
## list in python
# list is a collection of items in a particular order
# list is defined by square brackets []

# list can contain any type of data
customers = ['Alice', False, 'Charlie', 1.4 , 1 , {'name': 'Bob' , 'age': 25}]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list[1:5])  # print elements from index 1 to 4
print(my_list[1:5:2])  # print elements from index 1 to 4 with step 2
print(my_list[::2])  # print elements with step 2

# list is mutable, means we can change the items in the list
my_list[1] = 20  # change the value of index 1 to 20


# list methods
my_list.append(11)  # add 11 at the end of the list
my_list.extend([1, 2, 3])  # add multiple elements at the end of the list
my_list.insert(1, 100)  # insert 100 at index 1
my_list.remove(100)  # remove 100 from the list
my_list.pop()  # remove the last element from the list
my_list.pop(1)  # remove element at index 1
my_list.clear()  # remove all elements from the list

my_list.index(2)  # return the index of 2
my_list.count(2)  # return the number of 2 in the list
my_list.sort()  # sort the list
my_list.reverse()  # reverse the list
my_list.copy()  # return a copy of the list

len(my_list)  # return the length of the list
max(my_list)  # return the maximum value of the list
min(my_list)  # return the minimum value of the list
sum(my_list)  # return the sum of the list



#####################################################################################

# Tuple
# tuple is similar to list but it is immutable
# tuple is defined by parentheses ()

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

my_tuple.insert(1, 100)  # this will give an error because tuple is immutable

###################################################################################
# Set
# set is a collection of unique elements
# set is defined by curly braces {}
# set can contain any type of data
# set is unordered, means the items in the set do not have a specific order
# set is mutable

my_set = {1 ,  3}
print(my_set)
my_set = {1, 1,1}


## set methods
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.union(b))  # return a set containing all the elements of both a and b 
print(a.intersection(b))  # return a set containing the common elements of both a and b
print(a.difference(b))  # return a set containing the elements of a that are not in b


