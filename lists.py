myList = ["banana", "apple", "cherry"]
print(myList)

myList2 = list()
print(myList2)

myList3 = [5, True, "apple", "apple"]
print(myList3)

print(myList[2])
print(myList[-1])

for x in myList:
    print(x)

if "banana" in myList:
    print('Yes')
else:
    print('No')

print(len(myList3))

myList.append("lemon")
myList.insert(1, "blueberry")
print(myList)

# removing all element
myList.pop()
myList.remove("cherry")

# Delete all item
myList.clear()

myList3.reverse()

myList.sort()
new_list = sorted(myList)  #sorted method

myListNum = [0] * 5
print(myListNum)

myListNum2 = [1, 2, 3]
new_num_list = myListNum + myListNum2