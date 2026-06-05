import random as rd
#N1 -----------------------

def char_generator(string):
    for char in string:
        yield char

#N2 --------------------------

arr = [1, 2, 3,4,5,6,7,8,9]

while True:
    num = int(input("Enter index: "))

    try:
        print(arr[num])
    except IndexError:
        print("out of range")

#N3 -----------------------------------

def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"გამოძახება - {count}")
        return func(*args, **kwargs)

    return wrapper

@counter
def say():
    print("hi")

say()
say()

#N4 -------------------------------------------------------

questions = {
    "5 + 7": 12,
    "9 * 4": 36,
    "20 - 8": 12,
    "18 / 3": 6,
    "2 ** 5": 32
}

total = 0

with open("game.log", "a") as f:
    for q, ans in questions.items():
        user_answer = input(f"{q} = ")

        if user_answer == str(ans):
            total += 10
            f.write(f"{q} = {user_answer} | correct, +10 points\n")
        else:
            f.write(f"{q} = {user_answer} | incorrect, 0 points\n")
            total += 0

print(f"you got {total} points")

#N5 -----------------------------------

def generate_game():
    signs = ["rock", "paper", "scissors"]

    return rd.choice(signs)

count = 3
comp_wins = 0
user_wins = 0
with open("rock.log", "a") as f:
    while count > 0:
        user_input = input("pick rock, paper, or scissors: ").lower()
        comp_input=generate_game()
        if user_input == "rock" and comp_input == "scissors":
            user_wins += 1
            print("you win!")
            f.write(f"computer chose {comp_input} | user chose {user_input} | user won!\n")
        elif user_input == "paper" and comp_input == "rock":
            user_wins += 1
            print("you win!")
            f.write(f"computer chose {comp_input} | user chose {user_input} | user won!\n")
        elif user_input == "scissors" and comp_input == "paper":
            user_wins += 1
            print("you win!")
            f.write(f"computer chose {comp_input} | user chose {user_input} | user won!\n")
        elif user_input == comp_input:
            print("it's a draw")
            f.write(f"computer chose {comp_input} | user chose {user_input} | it was a tie!\n")
        else:
            comp_wins += 1
            print("you lose")
            f.write(f"computer chose {comp_input} | user chose {user_input} | computer won\n")

        count -= 1

    if comp_wins > user_wins:
        print(f"computer won with {comp_wins} points")
        f.write(f"computer won with {comp_wins} points\n")
    elif comp_wins < user_wins:
        print(f"user won with {user_wins} points")
        f.write(f"user won with {user_wins} points\n")
    else:
        print(f"both had {user_wins} points")
        f.write(f"both had {user_wins} points, it's a draw\n")

#N7 ----------------------------------------------------------------------------------

def dice():
    nums = [1, 2, 3, 4, 5, 6]

    return rd.choice(nums)

while True:
    gamer1 = dice()
    gamer2 = dice()

    if gamer1 == gamer2:
        print(f"both players have same dice ({gamer1})")
        continue
    elif gamer1 > gamer2:
        print(f"first player won({gamer1} vs {gamer2})\n")
        ans = input(f"would you like to play again? (y/n)")
        if ans == "y":
            continue
        elif ans == "n":
            print(f"game has finished")
            break
    elif gamer2 > gamer1:
        print(f"second player won({gamer2} vs {gamer1})\n")
        ans = input(f"would you like to play again? (y/n)")
        if ans == "y":
            continue
        elif ans == "n":
            print(f"game has finished")
            break

#N8 ---------------------------------------------------------

def word_picker():
    word_list = ['myth', 'titan', 'right', 'velvet', 'maximum', 'bridge', 'rabbit', 'system', 'disorder', 'fear']

    word1 = rd.choice(word_list)
    word2 = rd.choice(word_list)

    return word1, word2

def slicer(word1, word2):
    lst1 = list(word1)
    indices = rd.sample(range(len(lst1)), 2)

    for i in sorted(indices, reverse=True):
        lst1.pop(i)

    result1 = "".join(lst1)

    lst2 = list(word2)
    indices = rd.sample(range(len(lst2)), 2)

    for i in sorted(indices, reverse=True):
        lst2.pop(i)

    result2 = "".join(lst2)

    return result1, result2


while True:
    words = word_picker()
    correct_word1=words[0]
    correct_word2=words[1]

    new_word_list=slicer(words[0], words[1])
    first_word = new_word_list[0]
    second_word = new_word_list[1]

    user_input1=input(f"first word is {first_word} | take a guess: ")
    user_input2=input(f"second word is {second_word} | take a guess: ")

    points = 0
    if user_input1.lower() == correct_word1.lower():
        points += 1
    if user_input2.lower() == correct_word2.lower():
        points += 1

    if points == 2:
        print(f"you won!")
    elif points == 1:
        print(f"you got 50% | the words were ({correct_word1}) | ({correct_word2})")
    else:
        print(f"you lost | the words were ({correct_word1}) | ({correct_word2})")

    break