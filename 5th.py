from itertools import permutations as perm, combinations as comb
from datetime import datetime, timedelta
import calendar

#N1 -----------------------------------------
#
# def possibilities(text):
#     perms=[''.join(p) for p in perm(text)]
#
#     total=[]
#     for p in perms:
#         total.append(p)
#
#     return len(total), total
#
#
# while True:
#     user_input=input('Enter text: ')
#     print(possibilities(user_input))

# N2------------------------------------------------

# today=datetime.today()
#
# samshabati=1
# samshabatamde=(samshabati-today.weekday())%7
#
# shemdegi=today+timedelta(days=samshabatamde)
#
# print(shemdegi.date())

# N3 -------------------------------------------

# while True:
#     user_input=input("შეიყვანეთ წელი: ")
#
#     if int(user_input)%4==0:
#         print("წელი ნაკიანია")
#     else:
#         print("არ არის ნაკიანი წელი")
#
# """Calendar იმპორტით პირდაპირ .isleap(user_input)"""

# N4 --------------------------------------------

# today = datetime.today()
# year_end=datetime(today.year, 12, 31)
#
# days_left=(year_end-today).days
# weeks_left=days_left//7
#
# print(weeks_left)

# N5 -----------------------------------

lst=[1, 2, 3, 4, 5]

for combo in comb(lst, 3):
    print(combo)