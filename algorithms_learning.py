
# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)


# print(stack)

# x = stack.pop()

# print(x)

# print(stack)

# from collections import deque

# queue = deque()

# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)

# print(queue)
# x = queue.popleft()
# print(x)
# print(queue)


#hash table

# items1 = dict({"key1":1, "key2": 2, "key3": "three"})
# print(items1)

# items2 = {}
# items2["key1"] = 1
# items2["key2"] = 2
# items2["key3"] = 3

# items2["key2"] = "two"

# print(items2)

# for key, value in items2.items(): #funnction to print items
#     print("Key: ", key, " value: ", value)


#RECURSION#####################################################################

# def countdown(x):
#     if x == 0:
#         print("Done!")
#         return
#     else:
#         print(x, "...")
#         countdown(x-1)
#         print("foo")
        
# countdown(5)

# def power(num, pwr):
#     if pwr == 0:
#         return 1
#     else:
#         return num*power(num, pwr-1)
    

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num*factorial(num - 1)
    

# print("{} to the power of {} is {}".format(5,3,power(5,3)))
# print("{} to the power of {} is {}".format(1,5, power(1,5)))
# print("{}! is {}".format(4, factorial(4)))
# print("{}! is {}".format(0, factorial(0)))

#SORTING####################################################


# def bubbleSort(dataset):
    
#     for i in range(len(dataset)-1, 0, -1):
#         #print("i: ", i)
#         for j in range(i):
#             #print("j: ", j)
#             if dataset[j] > dataset[j+1]:
#                 temp = dataset[j]
#                 dataset[j] = dataset[j+1]
#                 dataset[j+1] = temp
    
#         print("Current State: ", dataset)
    
    

# def main():
#     list1 = [6,20,8,19,56,23,87,41,49,53]
#     bubbleSort(list1)
#     print("Result: ", list1)


# if __name__ == "__main__":
#     main()
## MERGE SORT
# items = [6,20,8,19,56,23,87,41,49,53]

# def mergesort(dataset):
#     if len(dataset) > 1:
#         mid = len(dataset) // 2
#         leftarr = dataset[:mid]
#         rightarr = dataset[mid:]
        
#         mergesort(leftarr)
#         mergesort(rightarr)
       
#         i = 0
#         j = 0
#         k = 0
        
#         while i < len(leftarr) and j < len(rightarr):
#             if leftarr[i] < rightarr[j]:
#                 dataset[k] = leftarr[i]
#                 i += 1
#             else:
#                 dataset[k] = rightarr[j]
#                 j += 1
#             k += 1    
         
#         while i < len(leftarr):
#             dataset[k] = leftarr[i]
#             i += 1
#             k += 1
            
#         while j < len(rightarr):
#             dataset[k] = rightarr[j]
#             j += 1
#             k += 1
                

# print(items)
# mergesort(items)
# print(items)

## QUICK SORT

# items = [6,20,8,19,56,23,87,41,49,53]

# def quickSort(dataset, first, last):
#     if first < last:
#         pivotIdx = partition(dataset, first, last)
        
#         quickSort(dataset, first, pivotIdx - 1)
#         quickSort(dataset, pivotIdx+1, last)


# def partition(datavalues, first, last):
#     pivotvalue = datavalues[first]
    
#     lower = first + 1
#     upper = last
    
#     done = False
#     while not done:
       
#         while lower <= upper and datavalues[lower] <= pivotvalue:
#             lower += 1
            
#         while datavalues[upper] >= pivotvalue and upper >= lower:
#             upper -= 1
        
#         if upper < lower:
#             done = True
#         else:
#             temp = datavalues[lower]
#             datavalues[lower] = datavalues[upper]
#             datavalues[upper] = temp
    
#     temp = datavalues[first]
#     datavalues[first] = datavalues[upper]
#     datavalues[upper] = temp
    
#     return upper



# print(items)
# quickSort(items, 0, len(items)-1)
# print(items)
    
#def find_item(item, itemList):
#     for i in range(0, len(itemList)):
#         if item == itemList[i]:
#             return i

#     return None




# print(find_item(87, items))
# print(find_item(250, items))


# def binarysearch(item, itemlist):
#     listsize = len(itemlist) - 1
    
#     lowerIdx = 0
#     upperIdx = listsize
    
#     while lowerIdx <= upperIdx:
        
#         midPt = (lowerIdx + upperIdx) // 2
        
#         if itemlist[midPt] == item:
#             return midPt
        
#         if item > itemlist[midPt]:
#             lowerIdx = midPt + 1
#         else:
#             upperIdx = midPt - 1

#     if lowerIdx > upperIdx:
#         return None


# print(binarysearch(23, items))
# print(binarysearch(87, items))
# print(binarysearch(250, items))




# items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
# items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


# def is_sorted(itemlist):
#     # for i in range(0, len(itemlist) - 1):
#     #     if(itemlist[i] > itemlist[i+1]):
#     #         return False
    
#     return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))
#     # return True


# print(is_sorted(items1))
# print(is_sorted(items2))

# use a hashtable to filter out duplicate items
# TODO: create a hashtable to perform a filter
# filter = dict()


# # TODO: loop over each item and add to the hashtable
# for key in items:
#     filter[key]  = 0

# # TODO: create a set from the resulting keys in the hashtable
# result = set(filter.keys())
# print(result)



# # define a set of items that we want to reduce duplicates
# items = ["apple", "pear", "orange", "banana", "apple",
#          "orange", "apple", "pear", "banana", "orange",
#          "apple", "kiwi", "pear", "apple", "orange"]


# counter = dict()

# for item in items:
#     if(item in counter.keys()):
#         counter[item] +=1
#     else:
#         counter[item] = 1

# print(counter)


# items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


# def find_max(items):
    
#     if len(items) == 1:
#         return items[0]
    
#     op1 = items[0]
#     print(op1)
#     op2 = find_max(items[1:])
#     print(op2)
#     if op1 > op2:
#         return op1
#     else:
#         return op2
    
    
    
# print(find_max(items))
    













































































