# 1. collections.namedtuple()
# from collections import namedtuple

# n = int(input())
# col_name_raw = input().split()
# print(*col_name_raw)
# col_name = [j for j in col_name_raw if j != ""]

# stu_marks = []
# for i in range(n):
#     mrk_input_raw = input().split()
#     mrk_input = [j for j in mrk_input_raw if j != ""]
#     stu_marks.append(mrk_input)

# result = sum([int(m[col_name.index("MARKS")]) for m in stu_marks]) / n
# print(f"{result:.2f}")

# # alternative code
# from collections import namedtuple

# N = int(input())
# fields = input().split()
# SHEET = namedtuple('SHEET', fields)
# total = 0
# for _ in range(N):
#     fields = input().split()
#     SHEET1 = SHEET(*fields)
#     total += int(SHEET1.MARKS)

# print(f"{total/N: .2f}")

# # 2. Print the item_name and net_price in order of its first occurrence.
# from collections import OrderedDict

# ordered_dictionary = OrderedDict()
# n = int(input())

# for i in range(n):
#     prod_name, price = input().rsplit(" ", 1)
#     if prod_name in ordered_dictionary.keys():
#         ordered_dictionary[prod_name] += int(price)
#     else:
#         ordered_dictionary[prod_name] = int(price)

# for key, vals in ordered_dictionary.items():
#     print(key,vals)

# # 3. itertools.combinations
# from itertools import combinations

# s, k = input().split()

# s = sorted(s)

# final_combi = []
# for j in range(1, int(k)+1):
#     all_combi = ["".join(c) for c in list(combinations(s, j))]
#     final_combi.extend(all_combi)

# for i in final_combi:
#     print(i)


# # 4. time delta problem
# import datetime

# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     format = "%a %d %b %Y %H:%M:%S %z"
#     time1 = datetime.datetime.strptime(t1, format)
#     time2 = datetime.datetime.strptime(t2, format)

#     print((time1 - time2).total_seconds())
#     return str(int(abs((time1 - time2).total_seconds())))

#     # my attempted code
#     # day_name1, date1, month1, year1, full_time1, tz1 = t1.split()
#     # day_name2, date2, month2, year2, full_time2, tz2 = t2.split()

#     # hour1, minute1, second1 = full_time1.split(":")
#     # hour2, minute2, second2 = full_time2.split(":")

#     # mon1 = datetime.datetime.strptime(month1, "%b").month
#     # mon2 = datetime.datetime.strptime(month2, "%b").month

#     # sign = 1 if tz1.startswith('+') else -1
#     # hours = int(tz1[1:3])
#     # minutes = int(tz1[3:5])
#     # offset1 = datetime.timezone(sign * datetime.timedelta(hours=hours, minutes=minutes))

#     # sign = 1 if tz2.startswith('+') else -1
#     # hours = int(tz2[1:3])
#     # minutes = int(tz2[3:5])
#     # offset2 = datetime.timezone(sign * datetime.timedelta(hours=hours, minutes=minutes))

#     # time1 = datetime.datetime(year=int(year1), month=int(mon1), day=int(date1), hour=int(hour1), minute=int(minute1), second=int(second1), tzinfo=offset1)
#     # time2 = datetime.datetime(year=int(year2), month=int(mon2), day=int(date2), hour=int(hour2), minute=int(minute2), second=int(second2), tzinfo=offset2)

#     # res = time1 - time2

#     # return res.seconds

# t = int(input())

# for t_itr in range(t):
#     t1 = input()

#     t2 = input()

#     delta = time_delta(t1, t2)


# # 5. Incorrect Regex
# import re

# def solve(regex):
#     try:
#         if re.search(r'(\*|\+|\?){2,}', regex):
#             return False
#         re.compile(regex)
#         return True
#     except re.error:
#         return False
    

# n = int(input())

# for _ in range(n):
#     regex = input()   
#     print(solve(regex))

# # 6. Word Order
# n = int(input())
# word_list = [input() for i in range(n)]

# word_dict = {}

# for word in word_list:
#     if word_dict.get(word):
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1

# print(len(word_dict.keys()))
# vals = list(word_dict.values())
# final_vals = list(map(str, vals))
# print(" ".join(final_vals))

# 7. Compress the string    
# import itertools
# # [k, list(g) for k, g in groupby('AAAABBBCCDAABBB')] 
# s = input()

# for k, g in itertools.groupby(s):
#     print(f"({k}, {len(list(g))})", end=" ")

# alternate solution:-
# def groupby_custom(s):
#     l_group = []
#     l_key = []
#     count = 1

#     for ind, i in enumerate(s):
#         if ind+1 < len(s) and s[ind+1] == s[ind]:
#             count += 1
#         else:
#             l_group.append([i] * count)
#             l_key.append(i)
#             count = 1

#     return zip(l_key, l_group)

# s = list(input())

# for k, group in groupby_custom(s):
#     print(f"({len(list(group))}, {k})", end=" ")

# 8. combination with replacement
# from itertools import combinations_with_replacement

# s, k = input().split()

# combinations = list(combinations_with_replacement(sorted(s), int(k)))

# for combi in combinations:
#     print("".join(combi))

# # 9. Iterable and Iterator
# from itertools import combinations 
# n = int(input())
# s = input().split()
# k = int(input())

# all_combinations = list(combinations(s, k))

# a_count = 0
# for combi in all_combinations:
#     if "a" in combi:
#         a_count += 1

# result = a_count/len(all_combinations)
# print(f"{result:.6f}")

# # 10. collections-dequeue problems
# from collections import deque

# n = int(input())
# d = deque()

# for _ in range(n):
#     try:
#         data = input().split()
#         if data[0] == "append":
#             d.append(int(data[1]))
#         elif data[0] == "pop":
#             d.pop()
#         elif data[0] == "popleft":
#             d.popleft()
#         elif data[0] == "appendleft":
#             d.appendleft(int(data[1]))
#     except:
#         pass

# for i in d:
#     print(i, end=" ")

# # 11. Company logo
# # s = list(input())
# # s_dict = {}
# # s.sort()
# # for i in s:
# #     if s_dict.get(i):
# #         s_dict[i] += 1
# #     else:
# #         s_dict[i] = 1

# # val = list(s_dict.items())

# # for i in range(len(val)):
# #     for j in range(len(val)):
# #         if j < (len(val) - 1) and val[j][1] < val[j+1][1]:
# #             val[j+1], val[j] = val[j], val[j+1]

# # for k, v in val[0:3]:
# #     print(f"{k} {v}")

# from collections import Counter

# s = input().strip()
# print(Counter(s))
# for ch, freq in Counter(s).most_common(3):
#     print(f"{ch} {freq}")

# # 12. set-union problem
# n_eng = int(input())
# eng_roll = input().split()
# n_french = int(input())
# french_roll = input().split()

# result = set(eng_roll) | set(french_roll)
# print(len(result))

# # 13. Piling up
# test_cases = int(input())
# for i in range(test_cases):
#     no_of_cube = int(input())
#     cube = list(map(int, input().split()))

#     v_cube = []
#     if not v_cube:
#         v_cube.append(max(cube[0], cube[-1]))
#         if cube[0] >= cube[-1]:
#             cube.pop(0)
#         else:
#             cube.pop()

#     try:
#         for j in range(no_of_cube):
#             if v_cube[-1] >= max(cube[0], cube[-1]):
#                 v_cube.append(max(cube[0], cube[-1]))
#                 if cube[0] >= cube[-1]:
#                     cube.pop(0)
#                 else:
#                     cube.pop()
#             else:
#                 print("No")
#                 break
#     except Exception as e:
#         pass

#     if not cube:
#         print("Yes")

# # 14. Palindrome triangle using one for-loop and print statement
# # first solution
# n = int(input())
# s = ""
# for i in range(1, n+1):
#     print(f"{s}{i}{s[::-1]}")
#     s += str(i)

# # second solution
# n = int(input())
# val = 0
# for i in range(n):
#     res = 10 ** i
#     val += res
#     print(val ** 2)

# # third solution
# for i in range(int(input())):
#     print(sum(map(lambda x: 10 ** x, range(i+1))) ** 2)

# # 15. Maximize it!
# from itertools import product 

# def get_final_result(values, m):
#     final_res = 0
#     for vals in product(*values):
#         temp = 0
#         for val in vals:
#             temp += val ** 2
#         temp = temp % m

#         if temp > final_res:
#             final_res = temp
#     return final_res

# k, m = input().split()
# n_list = []

# for i in range(int(k)):
#     n = list(map(int, input().split()))
#     n_list.append(n[1:])

# result = get_final_result(n_list, int(m))
# print(result)

# # 16. Triangle quest - 1
# for i in range(1, int(input())):
#     print(sum(map(lambda x: 10 ** x, range(i))) * i)

# 17. Hacker-rank logo
# n = int(input())
# text = 'H'

# # first top pyramid
# for i in range(1, (2*n)+1, 2):
#     print((i*text).center(2*n, " "))

# # upper middle part
# for i in range(1, n+2):
#     print(" "*((n)//2) + (n*text) + " "*(n*3) + (n*text))

# # middle part
# for i in range((n+1)//2):
#     print(" "*((n)//2) + (n*text) + text*(n*3) + (n*text))

# # lower middle part
# for i in range(1, n+2):
#     print(" "*((n)//2) + (n*text) + " "*(n*3) + (n*text))

# # final inverted pyramid
# for i in range((2*n)-1, 0, -2):
#     print(" "*(n*4) + (i*text).center(2*n, " "))

# # 18. set difference operation
# eng_n = input()
# eng_roll_list = set(input().split())
# french_n = input()
# french_roll_list = set(input().split())

# print(len(eng_roll_list.difference(french_roll_list)))

# # 19. Integer comes in all sizes
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# res = (a ** b) + (c ** d)
# print(res)

# print((2 ** 63) - 1)

# # 20. The Captain's Room
# k = int(input())
# room_list = input().split()

# room_dict = {}

# for r in room_list:
#     if room_dict.get(r):
#         room_dict[r] += 1
#     else:
#         room_dict[r] = 1

# for key, val in room_dict.items():
#     if val == 1:
#         print(key)
#         break

# # 21. set mutations
# a = int(input())
# set_a = set(map(int, input().split()))

# n = int(input())
# for i in range(n):
#     command_name, nn = input().split()
#     set_n = map(int, input().split())
#     getattr(set_a, command_name)(set_n)
    
# print(sum(set_a))

# # 22. python check subset
# test_cases = int(input())
# for i in range(test_cases):
#     a_ele = int(input())
#     set_a = set(map(int, input().split()))
#     b_ele = int(input())
#     set_b = set(map(int, input().split()))
    
#     print(set_a.issubset(set_b))

# # 23. Valid transactions - Sliding Window (Two Pointers)
# def max_valid_transactions(initial_balance, transactions):
#     left = 0
#     balance = initial_balance
#     max_len = 0

#     for right in range(len(transactions)):
#         balance += transactions[right]

#         while balance < 0 and left <= right:
#             balance -= transactions[left]
#             left += 1

#         max_len = max(max_len, right - left + 1)

#     return max_len, left

# bal = int(input("Initial Balance: "))
# txn = map(int, input("Transactions: ").split())
# print(max_valid_transactions(bal, list(txn)))


# # 24. complex number problem - medium
# import math

# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
        
#     def __add__(self, no):
#         real = self.real + no.real
#         imgi = self.imaginary + no.imaginary
#         return Complex(real, imgi)
        
#     def __sub__(self, no):
#         real = self.real - no.real
#         imgi = self.imaginary - no.imaginary
#         return Complex(real, imgi)
        
#     def __mul__(self, no):
#         real_part = (self.real * no.real) - (self.imaginary * no.imaginary)
#         imaginary_part = (self.real * no.imaginary) + (self.imaginary * no.real)
#         return Complex(real_part, imaginary_part)

#     def __truediv__(self, no):
#         real = ((self.real * no.real) + (self.imaginary * no.imaginary)) / (no.real**2 + no.imaginary**2)
#         imaginary = ((self.imaginary * no.real) - (self.real * no.imaginary)) / (no.real**2 + no.imaginary**2)
#         return Complex(real, imaginary)

#     def mod(self):
#         return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


# 25. 
