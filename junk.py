from typing import List
def maxSubArray(nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum +=n 
            maxSub = max(maxSub, curSum)
        return maxSub

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)


# def printUnion(a,b):
#     i = j = 0 
#     while(i<len(a) and j<len(b)):
#         if (i>0 and a[i]==a[i-1]):
#             i = i + 1
#         elif (j>0 and b[j]==b[j-1]):
#             j = j + 1
#         elif(a[i] < b[j]):
#             print(a[i], end=" ")
#             i = i+1
#         elif (a[i] > b[j]):
#             print(b[j], end=" ")
#             j = j+1
#         else:
#             print(a[i], end=" ")
#             i = i+1
#             j = j+1
#     while (i<len(a)):
#         if(i>0 and a[i]!=a[i-1]):
#             print(a[i], end=" ")
#         i = i+1
#     while (j <len(b)):
#         if (j > 0 and b[j]!= b[j-1]):
#             print(b[j], end=" ")
#         j = j+1           


# a = [3,5,8]
# b = [2,8,9,10,15]
# printUnion(a,b)
# def merge(a, low, mid, high):
#     left = a[low:mid + 1]
#     right = a[mid + 1:high + 1]

#     i = j = 0
#     k = low

#     while i < len(left) and j < len(right):

#         if left[i] < right[j]:
#             a[k] = left[i]

#             k += 1
#             i += 1
#         else:
#             a[k] = right[j]
#             k += 1
#             j += 1

#     while i < len(left):
#         a[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         a[k] = right[j]
#         j += 1
#         k += 1


# def mergeSort(arr, l, r):
#     if r > l:
#         m = (r + l) // 2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)


# arr = [10, 5, 30, 15, 7]
# print(f"Before Merge Sort: {arr}")

# mergeSort(arr, 0, 4)
# print(*arr)
# def mergeSort(l1, l2):
#     res = []
#     m = len(l1)
#     n = len(l2)
#     i , j = 0, 0

#     while i < m and j < n:
#         if l1[i] < l2[j]:
#             res.append(l1[i])
#             i = i + 1
#         else:
#             res.append(l2[j]) 
#             j = j+1
#     while i<m:
#         res.append(l1[i])
#         i = i + 1
#     while j< n:
#         res.append(l2[j])
#         j = j + 1      
#     return res     
# l1 = [10,15]
# l2 = [5,6,6,30,40]
# print(mergeSort(l1,l2))


# def selectionSort(l):
#     n = len(l)
#     for i in range(n):
#         min_ind = i
#         for j in range(i + 1, n):
#             if l[j] < l[min_ind]:
#                 print(f"condition satisfies {j}")
#                 min_ind = j
#         # l[min_ind], l[i] = l[i], l[min_ind]

#         if min_ind != i:
            
#             l[min_ind], l[i] = l[i], l[min_ind]
#     return l

# l = [20,5,40,60,30,80]
# selectionSort(l)
# print(l)
# def lastOccurence(l, x):
#     low = 0
#     high = len(l)-1

#     while low <= high:
#         mid = (low+high)//2

#         if l[mid] < x:
#             low = mid + 1
        
#         elif l[mid] > x:
#             high = mid -1
        
#         else:
#             if mid == len(l) -1 or l[mid] != l[mid+1]:
#                 return mid
#             else:
#                 low = mid +1
#     return -1

# l = [5, 10, 10, 10, 10, 20, 20]

# print(lastOccurence(l, 20))

# def firstOccurence(l, n, x):
#     low = 0
#     high = n - 1
#     while(low<=high):
#         mid=(low+high)//2
#         if x > arr[mid]:
#             low = low + 1
#         elif x < arr[mid]:
#             high = mid -1
#         else:
#             if mid==0 or arr[mid-1] != arr[mid]:
#                 return mid
#             else:
#                 high=mid-1
#     return -1


# arr = [1,10,10,10,20,20,40]
# x = 10
# print(firstOccurence(arr,len(arr),x))
# def bSearch(l, key, low, high):
#     if low > high:
#         return -l 
    
#     mid = (low + high)//2
#     if l[mid] == key:
#         return mid
#     elif l[mid] < key:
#         return bSearch(l, key, mid+1 , high)
#     else:
#         return bSearch(l, key, low, mid-1)

# def bSearchMain(l, x):
#     return bSearch(l, x, 0, len(l) - 1)


# l = [10, 20, 30, 40, 50, 60]
# print(bSearchMain(l, 40))
# def binSearch(l, key):
#     low = 0
#     high = len(l)-1

#     while low <=high:
#         mid = (low+high)//2
#         if l[mid]==key:
#             return mid
#         elif l[mid]<key:
#             low = mid + 1
#             print(f"key {key} is in right side ")
#         else:
#             high = mid - 1
#             print(f"key {key} is in left side ")
#     return -1


# l = [10,20,30,40,50,60]
# print(binSearch(l, key=40))

# # Bubble sort
#
# def bubblesort(l):
#     """ sorts the list
#
#     :type l: bytearray.
#     """
#     n = len(l)
#     for i in range(n - 1):
#         swapped = False
#         for j in range(n - i - 1):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#                 swapped = True
#             if not swapped:
#                 return
#
#
# l = [5, 8, 6, 2, 1]
# print(f"Before Sorting ::{l}")
# bubblesort(l)
# print(f"After Sorting ::{l}")

# def selection(l):
#     n = len(l)
#     for i in range(n-1):
#         min_ind = i
#         for j in range(i+1,n):
#             if l[j] < l[min_ind]:
#                 min_ind = j
#         l[min_ind], l[i] = l[i], l[min_ind]
#
# l = [5, 8, 6, 2, 1]
# print(f"Before Sorting ::{l}")
# selection(l)
# print(f"After Sorting ::{l}")

# def insertion(l):
#     n = len(l)
#
#     for i in range(1,n):
#         x = l[i]
#         j = i -1
#
#         while j>=0 and x < l[j]:
#             l[j+1]=l[j]
#             j = j-1
#         l[j+1]= x
# l = [20, 5, 40, 60, 10, 30]
# print(f"Before Sorting ::{l}")
# insertion(l)
# print(f"After Sorting ::{l}")

# def mergesort(a,b):
#     res = []
#     m = len(a)
#     n = len(b)
#     i = 0
#     j = 0

#     while i < m and j < n:
#         if a[i] < b[j]:
#             res.append(a[i])
#             i = i+1

#         else:
#             res.append(b[j])
#             j = j+1

#     while i < m:
#         res.append(a[i])
#         i = i + 1
#     while j < n:
#         res.append(b[j])
#         j = j + 1
#     return res


# b = [2,5,7,9,11,13]
# a = [4,6,8]

# print(f"Before Sorting ::{a} {b}")
# sor = mergesort(a,b)
# print(f"After Sorting ::{sor}")


# Nth Node from end of linked list

# Recursive Reverse a linked list


# class Node:
#     def __init__(self, data):
#         self.key = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node

#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = new_node

#     def reverseList(self, curr, prev= None):
#         if curr == None:
#             return prev
        
#         next = curr.next
#         curr.next = prev
 
#         #Recursively reverse the rest of the list
#         return self.reverseList(next, curr)
        
#     def printlist(self):
#         curr = self.head
#         while curr:
#             print(curr.key, end=" ->")
#             curr = curr.next
#         print("None")
    

#     def reverse(self):
#         # Start the reversal process from the head of the list
#         self.head = self.reverseList(self.head)




# # Create a LinkedList
# ll = LinkedList()
# # Insert nodes into the linked list while maintaining the sorted order
# ll.append(10)
# ll.append(20)
# ll.append(20)
# ll.append(30)
# ll.append(30)
# ll.append(30)


# # Print the linked list to see the sorted result
# print("Sorted Linked List:")
# ll.printlist()
# ll.reverse()
# ll.printlist()
    



            
