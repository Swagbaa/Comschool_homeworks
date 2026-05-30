#N1

# from itertools import permutations as perm
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

# N2

# from datetime import datetime, timedelta
#
# today=datetime.today()
#
# samshabati=1
# samshabatamde=(samshabati-today.weekday())%7
#
# shemdegi=today+timedelta(days=samshabatamde)
#
# print(shemdegi.date())

# N3

while True:
    user_input=input("შეიყვანეთ წელი: ")

    if int(user_input)%4==0:
        print("წელი ნაკიანია")
    else:
        print("არ არის ნაკიანი წელი")

"""Calendar იმპორტით პირდაპირ .isleap(user_input)"""