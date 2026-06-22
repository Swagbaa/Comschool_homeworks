#N1

# maze = [
#     ["S", ".", "#", ".", "."],
#     ["#", ".", "#", ".", "#"],
#     [".", ".", ".", ".", "."],
#     ["#", "#", "#", ".", "#"],
#     [".", ".", ".", ".", "E"]
# ]
#
# row = 0
# col = 0
#
# while True:
#     move = input("l/r/u/d: ")
#
#     new_row = row
#     new_col = col
#
#     if move == "l":
#         new_col -= 1
#     elif move == "r":
#         new_col += 1
#     elif move == "u":
#         new_row -= 1
#     elif move == "d":
#         new_row += 1
#     else:
#         print("Invalid move.")
#         continue
#
#     if new_row < 0 or new_row >= len(maze) or new_col < 0 or new_col >= len(maze[0]):
#         print("Can't move outside the maze.")
#         continue
#
#     if maze[new_row][new_col] == "#":
#         print("Can't move there.")
#         continue
#
#     row = new_row
#     col = new_col
#
#     print(f"Current position: ({row}, {col})")
#
#     if maze[row][col] == "E":
#         print("You escaped the maze!")
#         break

#N2 -----------------------------------------------------------------------------------

# class Character:
#     def __init__(self, name, hp, attack):
#         self.name = name
#         self.hp = hp
#         self.attack = attack
#
#     def __str__(self):
#         return f"{self.name} | HP: {self.hp} | Attack: {self.attack}"
#
#     def attack_skill(self, other):
#         other.hp -= self.attack
#
#     def is_alive(self):
#         return self.hp > 0
#
#
# class Giant(Character):
#     def __init__(self):
#         super().__init__("Giant", 700, 150)
#
#
# class Speedy(Character):
#     def __init__(self):
#         super().__init__("Speedy", 320, 349)
#
#
# class Achilles(Character):
#     def __init__(self):
#         super().__init__("Achilles", 1, 1000)
#
# class RubberGuy(Character):
#     def __init__(self):
#         super().__init__("RubberGuy", 600, 200)
#
# class PyMaster(Character):
#     def __init__(self):
#         super().__init__("PyMaster", 450, 450)
#
#
# class Skill:
#     def __init__(self, name, hp_b, attack_b):
#         self.name = name
#         self.hp_b = hp_b
#         self.attack_b = attack_b
#
#     def apply_skill(self, character):
#         character.hp+=self.hp_b
#         character.attack+=self.attack_b
#
#
# fireball = Skill("Fireball", 50, 200)
# freeze = Skill("Freeze", 100, 100)
# shield = Skill("Shield", 300, 0)
#
# available_skills = {
#     "fireball": fireball,
#     "freeze": freeze,
#     "shield": shield
# }
#
#
#
# character_classes = {
#     "Giant": Giant,
#     "Speedy": Speedy,
#     "Achilles": Achilles,
#     "RubberGuy": RubberGuy,
#     "PyMaster": PyMaster
# }
#
# while True:
#     choice1 = input("Choose character (Giant, Speedy, Achilles, RubberGuy, PyMaster): ").strip()
#
#     if choice1 in character_classes:
#         player1 = character_classes[choice1]()
#         print(f"You chose {player1}")
#         break
#
#     print("Invalid character. Try again.\n")
#
#
# while True:
#     skill_choice1 = input("Choose skill (fireball, freeze, shield): ").lower().strip()
#
#     if skill_choice1 in available_skills:
#         available_skills[skill_choice1].apply_skill(player1)
#         print(f"{player1.name} learned {available_skills[skill_choice1].name}")
#         print(player1)
#         break
#
#     print("Invalid skill. Try again.\n")
#
#
# while True:
#     choice2 = input("Choose character (Giant, Speedy, Achilles, RubberGuy, PyMaster): ").strip()
#
#     if choice2 in character_classes:
#         player2 = character_classes[choice2]()
#         print(f"You chose {player2}")
#         break
#
#     print("Invalid character. Try again.\n")
#
#
# while True:
#     skill_choice2 = input("Choose skill (fireball, freeze, shield): ").lower().strip()
#
#     if skill_choice2 in available_skills:
#         available_skills[skill_choice2].apply_skill(player2)
#         print(f"{player2.name} learned {available_skills[skill_choice2].name}")
#         print(player2)
#         break
#
#     print("Invalid skill. Try again.\n")
#
# while player1.is_alive() and player2.is_alive():
#
#     player1.attack_skill(player2)
#     print(player2)
#
#     if not player2.is_alive():
#         print(f"\n{player1.name} wins!")
#         break
#
#     player2.attack_skill(player1)
#     print(player1)
#
#     if not player1.is_alive():
#         print(f"\n{player2.name} wins!")
#         break

#N3 ---------------------------------------------------------------------------------

class Transport:
    def __init__(self, name, fuel, speed, capacity):
        self.name = name
        self._fuel = fuel
        self.speed = speed
        self.capacity = capacity

    def __str__(self):
        return self.name

    def move(self, distance):
        pass

class Bus(Transport):
    def __init__(self):
        super().__init__("Bus", 200, 70, 50)

    def move(self, distance):
        self._fuel -= distance * 0.2

        if self._fuel <= 0:
            self._fuel = 0
            print("Bus has stopped (no fuel)")
        else:
            print(f"Bus moved {distance}km, fuel left: {self._fuel}")

class Car(Transport):
    def __init__(self):
        super().__init__("Car", 150, 200, 4)

    def move(self, distance):
        self._fuel -= distance * 0.1

        if self._fuel <= 0:
            self._fuel = 0
            print("Car has stopped (no fuel)")
        else:
            print(f"Car moved {distance}km, fuel left: {self._fuel}")

class Bike(Transport):
    def __init__(self):
        super().__init__("Bike", 0.1, 30, 2)

    def move(self, distance):
        print("Bike doesn't use fuel in this model.")

car1=Car()
bus1=Bus()
bike1=Bike()

car1.move(1000)
car1.move(100)
car1.move(399)