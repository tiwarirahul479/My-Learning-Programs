# # 1. Find two sum
# # def twoSum(nums, target):
# #     for left in range(len(nums)):
# #         for right in range(left+1, len(nums)):
# #             if ((nums[left] + nums[right]) == target):
# #                 return [left, right]

# # def twoSum(nums, target):
# #     for left in range(len(nums)):
# #         right = left + 1
# #         while right < len(nums):
# #             if nums[left]+nums[right] == target:
# #                 return [left, right]
# #             right += 1

# # best solution
# def twoSum(nums, target):
#     seen = {}  # value -> index
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in seen:
#             return [seen[complement], i]
        
#         seen[num] = i
            
# nums = [2,5,5,11]
# target = 10
# # nums = [2,7,11,15]
# # target = 9
# # nums = [0, 4, 3, 0]
# # target = 0
# print(twoSum(nums, target))


# 2. Add two numbers
# Definition for singly-linked list.
# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             total = val1 + val2 + carry
#             carry = total // 10

#             current.next = ListNode(total % 10)
#             current = current.next

#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy.next

# l1 = [2,4,3]
# for l in l1:
#     ListNode(l)
# l2 = [5,6,4]
# sol = Solution()
# print(sol.addTwoNumbers(l1, l2))


# 3. Find longest non-repeating character substring, using sliding window 
# algo:-
    # Take two pointers, left and right. Take one empty list or set. Take max_str_len = 0
    # Begin with left = right = 0. Iterate over the whole string by adding and comparing the elements on new list. Remember you right is moving in this stage.
    # When find the duplicate items in the new list, move the left pointer and remove the elements from your new list until you remove the duplicate.
    # Return finally the max of max_str_len and right - left + 1

# # code:-
# def find_longest_nonrepeating_substring(s):
#     left = 0
#     max_len = 0
#     substr_list = list()
#     sub_str = ""

#     for right in range(len(s)):
#         while s[right] in substr_list:
#             substr_list.remove(s[left])
#             left += 1

#         substr_list.append(s[right])
#         max_len = max(max_len, right - left + 1)

#         # non-repeating string 
#         if len(sub_str) < len(substr_list):
#             sub_str = "".join(substr_list)

#     return max_len, sub_str

# # s = "abcabcbb"
# s = "bbbbb"
# print(find_longest_nonrepeating_substring(s))



# 5. Find the longest palindromic sub-string
# def helpers(s, left, right):
#     while left >= 0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1

#     return s[left+1:right]

# def find_longest_palindromic_substring(s):
#     result = ""

#     for i in range(len(s)):
#         odd = helpers(s, i, i)
#         even = helpers(s, i, i+1)

#         result = max(odd, even, result, key=len)

#     return result

# # s = "abbba"
# s = "babad"
# print(find_longest_palindromic_substring(s))
