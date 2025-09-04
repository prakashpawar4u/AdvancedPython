def isHappy_set(n:int) -> bool:
    def sum_of_squares(num: int) -> int:
        total = 0
        while num > 0: 
            digit = num % 10
            total += digit * digit
            num //= 10
        return total 
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum_of_squares(n)

    return True

print(isHappy_set(19))  # True

# def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
#     from collections import defaultdict
#     char_count = defaultdict(int)
#     left = max_len = 0
#     for right in range(len(s)):
#         char_count[s[right]] += 1

#         #sliding window
#         while len(char_count) > 2:
#             char_count[s[left]] -= 1
#             if char_count[s[left]] == 0:
#                 del char_count[s[left]]
#             left += 1

#             print(char_count)
#         max_len = max(max_len, right - left + 1)
#     return max_len 


# print(lengthOfLongestSubstringTwoDistinct("eceeebaaaaaaa"))


# def characterReplacement(s: str, k: int) -> int:
#     from collections import defaultdict

#     count = defaultdict(int)
#     max_count = 0
#     res = 0 
#     left = 0 

#     for right in range(len(s)):
#         count[s[right]] +=1
#         max_count = max(max_count, count[s[right]])

#         if (right- left + 1) - max_count > k:
#             count[s[left]] -= 1
#             left += 1

#         res = max(res, right -left + 1)

#     return res

# res = characterReplacement("AABABBA", 1)
# print(res)

# def longestSum(s: str) -> int:
#     start = 0
#     max_len = 0
#     char_map = {}
#     for end in range(len(s)):
#         char = s[end]
#         if char in char_map and char_map[char] >= start:
#             start = char_map[char] + 1
#         char_map[char] = end
#         max_len = max(max_len, end - start + 1)
#     return max_len


# res = longestSum("abcabcbb")
# print(res)
# s = "eceba"
# char_map = {}
# max_length = 1


# for end in range(len(s)):
#     char = s[end]
#     char_map[char]= end

#     if len(char_map) > 2:
#         del_char = min(char_map, key=char_map.get)
#         start = char_map[del_char] + 1
#         del char_map[del_char]
#     print("END=> ", end, char_map)
# max_length = max(max_length, end - start + 1)
# print(max_length)

# def minPairSum(nums):
#     # Since nums[i] is bounded (1 <= nums[i] <= 10^5), use counting sort
#     MAX_VAL = 10
#     count = [0] * (MAX_VAL + 1)

#     for num in nums:
#         count[num] += 1

#     left, right = 1, MAX_VAL
#     max_sum = 0

#     while left <= right:
#         # Move left pointer to next non-zero count
#         while left <= right and count[left] == 0:
#             left += 1
#         # Move right pointer to previous non-zero count
#         while left <= right and count[right] == 0:
#             right -= 1
#         if left > right:
#             break

#         # Pair left and right
#         pair_count = min(count[left], count[right])
#         if left == right:
#             pair_count //= 2  # Only half can be paired when values are equal

#         max_sum = max(max_sum, left + right)
#         count[left] -= pair_count
#         count[right] -= pair_count

#     return max_sum

# nums= [3,5,2,3]
# res = minPairSum(nums)
# print(res)

# from typing import List

# class Solution:
#     def trap(self, height):
#         left, right = 0, len(height) - 1
#         left_max, right_max = 0, 0
#         water = 0

#         while left < right:
#             if height[left] < height[right]:
#                 if height[left] >= left_max:
#                     left_max = height[left]
#                 else:
#                     water += left_max - height[left]
#                 left += 1
#             else:
#                 if height[right] >= right_max:
#                     right_max = height[right]
#                 else:
#                     water += right_max - height[right]
#                 right -= 1

#         return water
    
# if __name__ == "__main__":
#     # height = [4,2,0,3,2,5]
#     height = [0,1,0,2,1,0,1,3,2,1,2,1]


#     Sobj = Solution()
    
#     result = Sobj.trap(height)
#     print("Output:", result)

# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         MOD = 10**9 + 7

#         # Step 1: Sort the array to make min/max handling easier
#         nums.sort()

#         # Step 2: Precompute powers of 2 up to len(nums)
#         # This is to calculate number of combinations quickly
#         pow2 = [1] * len(nums)
#         for i in range(1, len(nums)):
#             pow2[i] = pow2[i - 1] * 2 % MOD

#         print(f"POW2 = {pow2}")

#         # Step 3: Use two pointers
#         left, right = 0, len(nums) - 1
#         result = 0

#         while left <= right:
#             # If the smallest and largest element sum is within target
#             if nums[left] + nums[right] <= target:
#                 # All subsets of elements between left and right are valid
#                 # Count = 2^(right - left)
#                 result += pow2[right - left]
#                 result %= MOD  # keep it under MOD
#                 left += 1
#             else:
#                 # If the sum is too big, move right pointer to try smaller max
#                 right -= 1

#         return result
    

# # Driver code
# if __name__ == "__main__":
#     # Example test case 1
#     nums = [3, 5, 6, 7]
#     target = 9
#     sol = Solution()
#     print("Output:", sol.numSubseq(nums, target))  # Expected output: 4

    # # Example test case 2
    # nums = [3, 3, 6, 8]
    # target = 10
    # print("Output:", sol.numSubseq(nums, target))  # Expected output: 6

    # # Example test case 3
    # nums = [2, 3, 3, 4, 6, 7]
    # target = 12
    # print("Output:", sol.numSubseq(nums, target))  # Expected output: 61


# def max_number_from_digits(s: str) -> int:
#     digit_count = [0] * 10
#     print("Before ::",digit_count)
#     for ch in s:
#         digit_count[int(ch)] += 1
#     print("Before ::",digit_count)
    
#     result = []
#     for digit in range(9, -1, -1):
#         print(i)



# inp = "34037"
# out = max_number_from_digits(inp)
# print(out)
# class MyQueue:
#     def __init__(self):
#         self.stack_in = []
#         self.stack_out = []

#     def push(self, x):
#         self.stack_in.append(x)

#     def pop(self):
#         self._transfer_if_needed()
#         return self.stack_out.pop()

#     def peek(self):
#         if not self.stack_out:
#             self._transfer_if_needed()
#         return self.stack_out[-1]

#     def empty(self):
#         return not self.stack_in and not self.stack_out

#     def _transfer_if_needed(self):
#         if not self.stack_out:
#             while self.stack_in:
#                 self.stack_out.append(self.stack_in.pop())

# q = MyQueue()
# q.push(10)
# q.push(20)
# print(q.peek())   # Output: 10
# print(q.pop())    # Output: 10
# print(q.empty())  # Output: False
# q.pop()
# print(q.empty())  # Output: True

# q.push(1)
# q.push(2)
# q.push(3)
# print(q.pop())  # 1
# q.push(4)
# print(q.pop())  # 2
# print(q.pop())  # 3
# print(q.pop())



# def minWindow(s: str, t: str) -> str:
#     if not s or not t:
#         return ""

#     t_count = Counter(t)  # Frequency map of characters in t
#     window_count = {}     # Current window character frequencies
#     have, need = 0, len(t_count)  # How many unique chars matched

#     res = [-1, -1]
#     res_len = float('inf')
#     l = 0  # Left pointer of window

#     for r in range(len(s)):  # r is the right pointer
#         char = s[r]
#         window_count[char] = window_count.get(char, 0) + 1

#         if char in t_count and window_count[char] == t_count[char]:
#             have += 1

#         while have == need:
#             # Update result if this window is smaller
#             if (r - l + 1) < res_len:
#                 res = [l, r]
#                 res_len = r - l + 1

#             # Shrink from the left
#             window_count[s[l]] -= 1
#             if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
#                 have -= 1
#             l += 1

#     l, r = res
#     return s[l:r+1] if res_len != float('inf') else ""

# print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
# print(minWindow("a", "a"))                # Output: "a"
# print(minWindow("a", "aa"))               # Output: ""

# def maxProduct(nums):
#     if not nums:
#         return 0

#     max_prod = min_prod = result = nums[0]

#     for num in nums[1:]:
#         if num < 0:
#             max_prod, min_prod = min_prod, max_prod

#         max_prod = max(num, max_prod * num)
#         min_prod = min(num, min_prod * num)

#         result = max(result, max_prod)

#     return result

# maxProduct([-2, 3, -4])

# # --------- DRIVER CODE ------------
# if __name__ == "__main__":
#     test_cases = [
#         ([2, 3, -2, 4], 6),
#         ([-2, 0, -1], 0),
#         ([0, 2], 2),
#         ([-2, 3, -4], 24),
#         ([2, -5, -2, -4, 3], 240)
#     ]

#     for i, (nums, expected) in enumerate(test_cases):
#         result = maxProduct(nums)
#         print(f"Test Case {i + 1}: {'Pass ✅' if result == expected else 'Fail ❌'} | Output: {result}, Expected: {expected}")


# #41 Longest Palindromic string 

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2:
#             return s

#         start, end = 0, 0

#         for i in range(len(s)):
#             # Try to expand from single character (odd-length)
#             len1 = self.expand_from_center(s, i, i)
#             # Try to expand from a pair of characters (even-length)
#             len2 = self.expand_from_center(s, i, i + 1)
#             max_len = max(len1, len2)

#             if max_len > end - start:
#                 # Update the start and end indices of longest palindrome
#                 start = i - (max_len - 1) // 2
#                 end = i + max_len // 2

#         return s[start:end + 1]

#     def expand_from_center(self, s, left, right):
#         # Expand while it's a palindrome
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return right - left - 1  # Length of palindrome


# s = Solution()

# # Positive cases
# print(s.longestPalindrome("babad"))  # "bab" or "aba"

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def partition(left, right):
#             pivot_idx = random.randint(left, right)
#             pivot = nums[pivot_idx]
            
#             # Move pivot to the end
#             nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
#             store_idx = left

#             for i in range(left, right):
#                 if nums[i] > pivot:
#                     nums[store_idx], nums[i] = nums[i], nums[store_idx]
#                     store_idx += 1

#             nums[store_idx], nums[right] = nums[right], nums[store_idx]
#             return store_idx

#         left, right = 0, len(nums) - 1
#         k_index = k - 1  # kth largest means index k-1 after sorting descending

#         while True:
#             pos = partition(left, right)
#             if pos == k_index:
#                 return nums[pos]
#             elif pos < k_index:
#                 left = pos + 1
#             else:
#                 right = pos - 1

# # nums = [3,2,1,5,6,4]
# # k = 2

# nums = [1]*1000000 + [2, 3, 4, 5,-5,-4,-3,-2,-1]
# k = 50000

# s = Solution()
# #print(s.findKthLargest([3,2,1,5,5,6, 6,4], 2)) 

# print(s.findKthLargest(nums, k)) 
# def max_number_from_digits(s: str) -> int:
#     digit_count = [0] * 10
#     for ch in s:
#         digit_count[int(ch)] += 1
#     result = []
#     for digit in range(9, -1, -1):
#         result.extend([str(digit)] * digit_count[digit])
#     return int(''.join(result))



# inp = "340447"
# out = max_number_from_digits(inp)
# print(out)

# print(nextGreaterElements(nums))  # Output: [4, 2, 4, -1, -1]
# Output: 9
    # # Test case 3 (target not found)
    # nums3 = [1, 2, 3, 4, 5]
    # target3 = 6

    # result3 = search(nums3, target3)
    # print(f"Target {target3} found at index: {result3}")  # Expected: -1


#from typing import List, Int, Set
#def find_pairs_with(nums:List[Int], k:Int)-> Set(tuple(int, int)):
# def find_pairs_with(nums, k):

#     pairs = set()
    
#     visited = set()
    
#     for num in nums:
#         complement = k - num
#         if complement in visited:
#             pairs.add((min(num, complement), max(num, complement)))
        
#         visited.add(num)
#     return pairs

# print(find_pairs_with({4, 5, 7, 8, 10}, 15))


# def find_pairs(nums: list[int], k: int) -> list[tuple[int, int]]:
#     seen = set()
#     pairs = []
    
#     for num in nums:
#         complement = k - num
#         if complement in seen:
#             pairs.append((complement, num))
#         seen.add(num)
    
#     return pairs

# # Example usage
# nums = [4, 5, 7, 8, 10]
# k = 15
# print(find_pairs(nums, k))

# from typing import List
# def divide(dividend, divisor):

#     #Wdge case: Division by zero
#     if divisor == 0 :
#         raise ValueError("Cannot divide by zero")
    
#     print(dividend, divisor)
#     negative = (dividend < 0) != (divisor < 0)


#     dividend = abs(dividend)
#     divisor = abs(divisor)


#     print(dividend, divisor)

#     quotient = 0 
#     while dividend >= divisor:
#         dividend -=divisor
#         quotient +=1

#     # Apply the negative sign if needed
#     if negative:
#         quotient = -quotient
#     return quotient
        
# dividend = 18
# divisor = 2
# result = divide(dividend, divisor)
# print(f"The result of {dividend} divided by {divisor} is: {result}")


# def climbStairs(n: int) -> int:
#     if n == 1:
#         return 1
#     prev2, prev1 = 1, 1

#     for i in range(2, n+1):
#         current = prev1 + prev2
#         prev2 = prev1
#         prev1 = current
#     return prev1


# n = 5
# climbStairs(n) 
# def majorityElement(nums):
#     candidate = None
#     count = 0
    
#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += (1 if num == candidate else -1)
    
#     return candidate
# s = nums = [2, 3, 2, 2, 2]
# print(majorityElement(s))
# def two_sum(nums, target):
#     # Initialize two pointers: one at the beginning, one at the end
#     left = 0
#     right = len(nums) - 1
    
#     while left < right:
#         current_sum = nums[left] + nums[right]
        
#         if current_sum == target:
#             return [nums[left], nums[right]]  # Found the pair
#         elif current_sum < target:
#             left += 1  # Move the left pointer to the right to increase the sum
#         else:
#             right -= 1  # Move the right pointer to the left to decrease the sum
    
#     return [] 

# nums = [1,2,3,4,6]
# target = 6
# print(two_sum(nums, target))



# def maxArea(height):
#     res = 0
#     l, r = 0, len(height) - 1  # Left and Right pointers

#     while l < r:
#         area = (r - l) * min(height[l], height[r])  # Corrected formula for area
#         res = max(res, area)  # Update the maximum area if needed

#         if height[l] < height[r]:  # Move the pointer pointing to the smaller height
#             l += 1
#         else:
#             r -= 1

#     return res


# height = [1, 7, 2, 5, 4, 7, 3, 6]
# print(maxArea(height))
# import time
# import threading

# # Simulate Testlines with status: Unlocked/Locked/Maintenance
# testlines = [
#     {"testline_id": "TL1", "status": "Unlocked"},
#     {"testline_id": "TL2", "status": "Unlocked"},
#     {"testline_id": "TL3", "status": "Unlocked"},
# ]

# # Simulating a list of jobs with priority (highest to lowest priority)
# jobs = [
#     {"job_name": "job1", "priority": 3},
#     {"job_name": "job2", "priority": 1},
#     {"job_name": "job3", "priority": 5},
#     {"job_name": "job4", "priority": 2},
#     {"job_name": "job5", "priority": 4},
# ]

# # Displaying the jobs before sorting
# print("Jobs before sorting:")
# for job in jobs:
#     print(f"Job Name: {job['job_name']}, Priority: {job['priority']}")

# # Sorting jobs based on priority (Highest to Lowest)
# sorted_jobs = sorted(jobs, key=lambda x: x["priority"], reverse=True)


# # Simulating job execution and locking testline
# def execute_job(job, testline):
#     print(f"Executing job '{job['job_name']}' on {testline['testline_id']}.")
#     time.sleep(3)  # Simulate job execution time
#     print(
#         f"Job '{job['job_name']}' executed on {testline['testline_id']} successfully."
#     )

#     # Mark testline as unlocked after job execution
#     testline["status"] = "Unlocked"
#     print(f"Testline {testline['testline_id']} is now Unlocked.")


# # Assign jobs to available testlines and run them on separate threads
# def assign_jobs_to_testlines():
#     job_index = 0  # To track which job we are assigning

#     def assign_job_to_testline(job, testline):
#         # Assign the highest priority job to the available testline
#         testline["status"] = "Locked"  # Lock the testline
#         print(
#             f"Assigning job '{job['job_name']}' to testline {testline['testline_id']}."
#         )
#         execute_job(job, testline)  # Simulate job execution

#     # Start the threads
#     threads = []
#     while job_index < len(sorted_jobs):
#         # Check for an available (Unlocked) testline
#         available_testline = None
#         for testline in testlines:
#             if testline["status"] == "Unlocked":
#                 available_testline = testline
#                 break

#         if available_testline:
#             # Assign the highest priority job to the available testline
#             job = sorted_jobs[job_index]
#             job_index += 1

#             # Create a thread to execute the job on the available testline
#             thread = threading.Thread(
#                 target=assign_job_to_testline, args=(job, available_testline)
#             )
#             threads.append(thread)
#             thread.start()
#         else:
#             print("No available testline. Waiting for a testline to become available.")
#             time.sleep(2)  # Wait before checking for available testlines again

#     # Wait for all threads to complete
#     for thread in threads:
#         thread.join()


# # Start the process of assigning jobs to testlines
# if __name__ == "__main__":
#     assign_jobs_to_testlines()


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashMap = {}
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in hashMap:
#                 return [hashMap[diff], i]
#             hashMap[n] = i
#         return []

# # Driver code
# if __name__ == "__main__":
#     solution = Solution()

#     # Test case 1
#     nums1 = [2, 7, 11, 15]
#     target1 = 9
#     print(solution.twoSum(nums1, target1))  # Output: [0, 1]

# def lastOccur(l, x):

#     low = 0
#     high = len(l) - 1

#     while low <= high:

#         mid = (low + high) // 2

#         if l[mid] < x:
#             low = mid + 1

#         elif l[mid] > x:
#             high = mid - 1

#         else:

#             if mid == len(l) - 1 or l[mid] != l[mid + 1]:
#                 return mid
#             else:
#                 low = mid + 1
#     return -1


# l = [5, 10, 10, 10, 10, 20, 20]

# print(10,lastOccur(l, 10))
# def hoarsePartition(arr, l, h):
#     pivot = arr[l]

#     i = l - 1
#     j = h + 1

#     while True:

#         i = i + 1
#         while arr[i] < pivot:
#             i = i + 1

#         j = j - 1
#         while arr[j] > pivot:
#             j = j - 1

#         if i >= j:
#             return j

#         arr[i], arr[j] = arr[j], arr[i]


# def qSort(arr, l, h):
#     if l < h:
#         p = hoarsePartition(arr, l, h)
#         qSort(arr, l, p)
#         qSort(arr, p + 1, h)


# arr = [8, 4, 7, 9, 3, 10, 5]

# qSort(arr, 0, 6)

# print(*arr)

# def lomutoPartition(arr, l ,h):
#     pivot = arr[h]
#     i = l -1
#     for j in range(l, h):
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     #print(arr, "value of i: ", i)
#     arr[i+1], arr[h] = arr[h], arr[i +1]
#     return i + 1

# arr = [10, 80, 30, 90, 50, 70]
# lomutoPartition(arr, 0, 5)
# print(*arr)


# def mergeSubarray(a, low, mid, high):
#     left = a[low:mid+1]
#     right = a[mid+1:high + 1]

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

# a = [10,15,20,40,8,11]
# low = 0
# high = len(a)

# mid = (low + high) //2
# sor = mergeSubarray(a, low, mid, high)
# print(f"Sorted array is :{a}")
# def insertionSort(l):
#     for i in range(1, len(l)):
#         x = l[i]
#         j = i-1

#         while j >=0 and x < l[j]:
#             l[j+1] = l[j]
#             j = j-1

#         l[j+1] = x

# l = [20, 5, 40, 60, 10, 30]
# print(f"Before sorting: {l}")

# insertionSort(l)
# print(*l)

# print(f"After sorting: {l}")

# def nextGretaerElem(nums):
#     stack = []
#     n = len(nums)
#     result = [-1] * n

#     for i in range(n):
#         while stack and nums[stack[-1]] < nums[i]:
#             result[stack.pop()]=nums[i]

#         stack.append(i)
#     return result

# nums = [2, 1, 2, 4, 3]
# print(nextGretaerElem(nums))  # Output: [4, 2, 4, -1, -1]


# def nextGreaterElements(nums):
#     n = len(nums)
#     result = [-1] * n  # Initialize the result list with -1's
#     stack = []  # This will store the indices of elements for which we are finding the next greater element

#     # Traverse the array twice to simulate circular nature
#     for i in range(2 * n):
#         # Element index in the range [0, n-1]
#         num = nums[i % n]

#         # While the stack is not empty and the current element is greater than the element at the index in the stack
#         while stack and nums[stack[-1]] < num:
#             index = stack.pop()  # Pop the index of the element from the stack
#             result[index] = num  # Update the result with the next greater element

#         # Push the current index to the stack (only for the first iteration for each element)
#         if i < n:
#             stack.append(i)

#     return result

# # Example usage
# nums = [2, 1, 2, 4, 3]
# print(nextGreaterElements(nums))  # Output: [4, 2, 4, -1, -1]

# def maxSubArray(nums: List[int]) -> int:
#         maxSub = nums[0]
#         curSum = 0

#         for n in nums:
#             if curSum < 0:
#                 curSum = 0
#             curSum +=n
#             maxSub = max(maxSub, curSum)
#         return maxSub

# nums = [-2,1,-3,4,-1,2,1,-5,4]
# maxSubArray(nums)


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
