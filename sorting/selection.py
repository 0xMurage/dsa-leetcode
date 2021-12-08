
"""
Given unsorted list, 
sort it using selection sort algorithm

- Do not create new data structure i.e. lists, tuples, or dictionaries


For each element
    - Initialize a variable x as index zero. It will keep track of last sorted index value
    - Find the smallest number starting from the index of variable x
    - Swap the smallest number found with  that in index x
    - Increment x  
    - If x == len(list)- 1 return, else loop through from step 2 above

"""

def selectionSort(list):
    sortedIndex = 0
    l =len(list)
    while(True):
        if sortedIndex == l:
            return list
        
        min=list[sortedIndex]
        minIndex= sortedIndex
        for i in range(sortedIndex,l):
            if min> list[i] or min == list[i]:
                min = list[i]
                minIndex = i

        list[minIndex] = list[sortedIndex]
        list[sortedIndex] = min
        sortedIndex+=1


"""
My naive solution:
- create an empty stack to hold sorted items



"""

print(selectionSort([3,9,1,10,2,2,1]))
assert selectionSort([3,9,1,10,2,2,1]) == [1,1,2,2,3,9,10]
assert selectionSort([10,2,4,5,9,8,3,6]) == [2,3,4,5,6,8,9,10]

print(selectionSort([3,9,1,10,2,2,1,1]))


"""
Starting from index i:
 - check any element k that is smaller than n[i]
 - if found, swap n[i] with k
 - increment the index i
 - loop above until at last element

"""
