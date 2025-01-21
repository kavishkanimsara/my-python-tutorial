
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