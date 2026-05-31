from itertools import permutations as perm, combinations as comb
from datetime import datetime, timedelta
import calendar
import time
import random as rd

#N1 -----------------------------------------

def possibilities(text):
    perms=[''.join(p) for p in perm(text)]

    total=[]
    for p in perms:
        total.append(p)

    return len(total), total


while True:
    user_input=input('Enter text: ')
    print(possibilities(user_input))

# N2------------------------------------------------

today=datetime.today()

samshabati=1
samshabatamde=(samshabati-today.weekday())%7

shemdegi=today+timedelta(days=samshabatamde)

print(shemdegi.date())

# N3 -------------------------------------------

while True:
    user_input=input("შეიყვანეთ წელი: ")

    if int(user_input)%4==0:
        print("წელი ნაკიანია")
    else:
        print("არ არის ნაკიანი წელი")

"""Calendar იმპორტით პირდაპირ .isleap(user_input)"""

# N4 --------------------------------------------

today = datetime.today()
year_end=datetime(today.year, 12, 31)

days_left=(year_end-today).days
weeks_left=days_left//7

print(weeks_left)

# N5 -----------------------------------

lst=[1, 2, 3, 4, 5]

for combo in comb(lst, 3):
    print(combo)

# N6 --------------------------------

s="XYZ"

for i in range(1, 4):
    for combo in comb(s, i):
        print(''.join(combo))


# N7 --------------------------------

num_to_pick=rd.randint(1, 20)
start = time.time()
limit = 5

while time.time() - start < limit:
    seconds = round(limit - (time.time() - start), 1)

    print(f"You have {seconds} seconds left.")

    guess = int(input("Enter a number between 1 and 20: "))

    if guess == num_to_pick:
        print(f"You win!!! The answer was {num_to_pick}")
        break
    else:
        print(f"You lose!! The answer was {num_to_pick}")

# N8 ---------------------------------------------------------------

start=datetime.now()

player1 = start + timedelta(seconds=rd.randint(5,20))
player2 = start + timedelta(seconds=rd.randint(5,20))

if player1<player2:
    print(f"player 1 wins in {player1.time()} seconds")
elif player2<player1:
    print(f"player 2 wins in {player2.time()} seconds")
else:
    print(f"it's a tie. both took {player1.time()} seconds")

# N9 -----------------------------------------------------------

user_birthday=input("enter your birthday(yyyy-mm-dd format): ")
bday=datetime.strptime(user_birthday,"%Y-%m-%d").date()
today=datetime.today().date()

next_year=bday.replace(year=today.year)

if next_year<today:
    next_year=next_year.replace(year=today.year+1)

days_left=(next_year-today).days
print(days_left)

# N10 --------------------------------------------------------

"""def generate_password():
    nums=[(rd.randint(1, 6)) for i in range(4)]

    password=''
    for i in nums:
        password+=str(i)
    return password"""

def generate_daily_password():
    rd.seed(datetime.today().toordinal())

    password = ""
    for _ in range(4):
        password += str(rd.randint(1, 6))

    return password

def password_guesser():
    nums = [(rd.randint(1, 6)) for i in range(4)]

    guess_password = ''
    for i in nums:
        guess_password += str(i)
    return guess_password

daily_password=generate_daily_password()


while True:
    guessed_password=password_guesser()

    if guessed_password == daily_password:
        print(f"computer has guessed the password.\n it was {daily_password}")
        break
    else:
        print(f"wrong password: {guessed_password}")
