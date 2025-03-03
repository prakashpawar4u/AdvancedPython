def lastOccurence(l, x):
    low = 0
    high = len(l)-1

    while low <= high:
        mid = (low+high)//2

        if l[mid] < x:
            low = mid + 1
        
        elif l[mid] > x:
            high = mid -1
        
        else:
            if mid == len(l) -1 or l[mid] != l[mid+1]:
                return mid
            else:
                low = mid +1
    return -1

l = [5, 10, 10, 10, 10, 20, 20]

print(lastOccurence(l, 20))

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
    



            
