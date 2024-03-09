# Write a python program to create a list of 10 elements and print the 5th element of the list, replace the second integer with 40, create a new list by slicing the first 5 elements and add 62 at the back and insert value 10 at index 3, remove value 40 and print the deleted element, sort the list in ascending order and reverse the order of the list.

lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lists[5])
lists[1] = 40
print(lists)
sublists = lists[:5]
print(sublists)
lists.append(62)
print(lists)
lists.insert(3, 10)
print(lists)
rem = lists.pop(1)
print(rem)
print(lists)
lists.sort()
print(lists)
lists.reverse()
print(lists)