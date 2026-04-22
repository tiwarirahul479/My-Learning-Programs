# # 1. Find two sum
# # input = [2,7,11,15], target = 9
# # output = [0,1] --> index which returns the target sum

# def find_two_sum(nums, target):
#     num_dict = {}

#     for idx, num in enumerate(nums):
#         diff = target - num

#         if diff in num_dict:
#             return [num_dict[diff], idx]

#         num_dict[num] = idx

# nums = [2,7,11,15]
# target = 9
# print(find_two_sum(nums, target))



# 2. Maximum sub-array sum
# input = [-2,1,-3,4,-1,2,1,-5,4]
# output = 6  --> [4,-1,2,1] this sub-array returns the max sum

# brute force
# def find_subarray_max_sum(arr):
#     m_sum_list = []
#     for i in range(len(arr)):
#         m_sum = arr[i]
#         for j in arr[i+1:]:
#             m_sum += j
#             m_sum_list.append(m_sum)

#     return max(m_sum_list)

# def find_subarray_max_sum(nums):
#     current = max_sum = nums[0]

#     for num in nums[1:]:
#         current = max(num, current + num)
#         max_sum = max(max_sum, current)

#     return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(find_subarray_max_sum(arr))



# 3. Longest Substring Without Repeating Characters
# input = "abcabcbb"
# output = 3  ---> this is the substring "abc"

# def find_longest_substring(s):
#     max_sum = 0
#     left = 0
#     substring_list = []

#     for right in range(len(s)):
#         while s[right] in substring_list:
#             substring_list.remove(s[left])
#             left += 1

#         substring_list.append(s[right])
#         max_sum = max(max_sum, right -left +1)

#     return max_sum

# s = "abcabcbb"
# print(find_longest_substring(s))



# Need to study this logic and concept
# 4. Reverse a Linked List
# input = 1 → 2 → 3 → 4 → None
# output = 4 → 3 → 2 → 1 → None

# def reverseList(head):
#     prev = None
#     curr = head

#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt

#     return prev



# 6. Valid Parentheses
# input = "()[]{}"
# output = True , Open brackets are closed by the same type and in the correct order

# def valid_parantheses(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in mapping:
#             top = stack.pop() if stack else '#'
#             if mapping[char] != top:
#                 return False
#         else:
#             stack.append(char)

#     return not stack

# s = "({}[]){}"
# print(valid_parantheses(s))



# 7. Array unpacking
# input = [[3], [9, 20], [15, 7]]
# output = [3,9,20,15,7]

# def array_unpacking(arr):
#     sub_array = []
#     for idx, a in enumerate(arr):
#         if isinstance(a, list):
#             temp_arr = array_unpacking(a)
#             sub_array.extend(temp_arr)
#         else:
#             sub_array.append(a)

#     return sub_array

# arr = [[3], [9, 20], [15, [7, 6]]]
# print(array_unpacking(arr))



# 8. Find the second highest in array
# input = [20,50,40,80,60,90]
# output = 80

# def find_third_highest(arr):
#     first, sec, third = 0,0,0
#     for a in arr:
#         if a > first:
#             third = sec
#             sec = first
#             first = a
#         elif a > sec:
#             third = sec
#             sec = a
#         elif a > third:
#             third = a

#     return first, sec, third

# arr = [10,15,20,13,80,45,24,90]
# print(find_third_highest(arr))



# 9. Group Anagrams
# input = ["eat","tea","tan","ate","nat","bat"]
# output = [['eat','tea','ate'], ['tan','nat'], ['bat']]

# def group_anagrams(arr):
#     anagram_dict = {}
#     for a in arr:
#         a_sorted = "".join(sorted(a))
#         if a_sorted not in anagram_dict:
#             anagram_dict[a_sorted] = [a]
#         else:
#             anagram_dict.get(a_sorted).append(a)

#     return list(anagram_dict.values())

# arr = ["eat","tea","tan","ate","nat","bat"]
# print(group_anagrams(arr))



# 10. Reverse integer
# If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
# Input: x = 123
# Output: 321

# def reverse_integer(num):
#     rev_num = 0
#     sign = -1 if num < 0 else 1
#     num = abs(num)

#     while num != 0:
#         unit_place = num%10
#         num = num//10

#         rev_num = rev_num * 10 + unit_place

#     lower_limit = -(2 ** 31) 
#     upper_limit = (2 ** 31) - 1

#     if not lower_limit < (sign * rev_num) < upper_limit:
#         return 0
    
#     return sign*rev_num

# num = -123
# print(reverse_integer(num))



# 11. Zigzag Conversion
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# def zigzag_conversion(s, rows):
#     zigzag_dict = {}
#     key = 1
#     rev = False

#     for i in s:
#         if key not in zigzag_dict:
#             zigzag_dict[key] = [i]
#         else:
#             zigzag_dict.get(key).append(i)

#         if key < rows and not rev:
#             key += 1
#         else:
#             key -= 1
#             rev = True
#             if key == 1:
#                 rev = False

#     res = zigzag_dict.values()
#     zigzag_str = ""
#     for r in res:
#         zigzag_str += "".join(r)

#     return zigzag_str


# s = "PAYPALISHIRING"
# rows = 3

# print(zigzag_conversion(s, rows))



# 12. Integer to roman
# def integer_to_roman(num):
#     roman_hash = {
#         1000: 'M',
#         900: 'CM',
#         500: 'D',
#         400: 'CD',
#         100: 'C',
#         90: 'XC',
#         50: 'L',
#         40: 'XL',
#         10: 'X',
#         9: 'IX',
#         5: 'V',
#         4: 'IV',
#         1: 'I',
#     }

#     roman = ''

#     for n, val in roman_hash.items():
#         while num >= n:
#             roman += val
#             num -= n

#     return roman

# num = 46
# print(integer_to_roman(num))



# 13. 1-D array rotation
# def rotate_array(arr, k):
#     i = 1
#     while i <= k:
#         ele = arr.pop()
#         arr.insert(0, ele)
#         i += 1

#     return arr

# arr = [1,2,3,4,5]
# k = 2
# print(rotate_array(arr, k))



# 14. 2-D array rotation
# input = [[1,2,3], [4,5,6], [7,8,9]]
# output = [[7,4,1], [8,5,2], [9,6,3]]

# def rotate_2d_array(arr):
#     rot_arr = []

#     while len(arr[0]) >= 1:
#         temp_arr = []
#         for a in range(len(arr)-1,-1,-1):
#             if arr[a]:
#                 temp_arr.append(arr[a][0])
#                 arr[a].remove(arr[a][0])

#         rot_arr.append(temp_arr)

#     return rot_arr

# optimal way
# def rotate_2d_array(arr):
#     n = len(arr)

#     print(f"=11=={arr=}")
#     # Step 1: Transpose
#     for i in range(n):
#         for j in range(i, n):
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

#     print(f"=22=={arr=}")
#     # Step 2: Reverse each row
#     for row in arr:
#         row.reverse()

#     print(f"=33=={arr=}")
#     return arr

# arr = [[1,2,3], [4,5,6], [7,8,9]]
# # arr = [[5]]
# print(rotate_2d_array(arr))



# 15. Binary Sementics Question
# input = [2,7,5,8,9]
# output = [27,75,58,89,92]

def make_the_output(arr):
    temp_arr = []

    # for i in range(len(arr)):
    #     if i <= len(temp_arr) - 2:
    #         res = str(arr[i]) + str(arr[i+1])
    #         temp_arr.append(int(res))

    #     if i == len(temp_arr):
    #         res = str(arr[i]) + str(arr[0])
    #         temp_arr.append(int(res))

    for i in range(len(arr)):
        pair = int(str(arr[i]) + str(arr[(i + 1) % len(arr)]))
        temp_arr.append(pair)

    return temp_arr

arr = [2,7,5,8,9]
print(make_the_output(arr))
