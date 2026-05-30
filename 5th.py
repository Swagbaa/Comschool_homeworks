#N1
from itertools import permutations as perm

def possibilities(text):
    perms=[''.join(p) for p in perm(text)]

    total=[]
    for p in perms:
        total.append(p)

    return len(total), total


while True:
    user_input=input('Enter text: ')
    print(possibilities(user_input))