# Creating an empty list
my_list = []

# Adding to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Elements appended to my_list:", my_list)

# Inserting to index 1 on the list
my_list.insert(1, 15)
print("Value 15 inserted:", my_list)

# Extending my_list
ext_list = [50, 60, 70]
my_list.extend(ext_list)
print("Extended the list:", my_list)

# Removing the last element
my_list.pop()
print("Removed last element:", my_list)

# Sort my_list in ascending order
my_list.sort()

# Index of value 30
print("Index of value 30 is:", my_list.index(30))
