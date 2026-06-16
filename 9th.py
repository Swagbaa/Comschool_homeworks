import random as rd
#N1 -------------------------------------------------------

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

class Mage(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def attack(self, other):
        if isinstance(other, Archer):
            print(f"{self.name} attacked {other.name}, {self.name} won")
        else:
            print(f"{self.name} attacked {other.name}, {other.name} won")


class Warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def attack(self, other):
        if isinstance(other, Mage):
            print(f"{self.name} attacked {other.name}, {self.name} won")
        else:
            print(f"{self.name} attacked {other.name}, {other.name} won")

class Archer(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def attack(self, other):
        if isinstance(other, Warrior):
            print(f"{self.name} attacked {other.name}, {self.name} won")
        else:
            print(f"{self.name} attacked {other.name}, {other.name} won")


player1=Archer("archer", 10, 12)
player2=Warrior("warrior", 12, 12)

player1.attack(player2)

#N2 ---------------------------------------------------------

class Monster:
    names=["Fluffy", "Cupcake", "Garlock the galactic destroyer",
           "Puck", "Pochita", "Demiurge", "Ainz", "Primordial one",
           "Jung", "Shinobu"
           ]
    index=0

    def __init__(self, name, monster_type, power):
        self.name = name
        self.monster_type = monster_type
        self.power = power

    @classmethod
    def create_from_level(cls, level):
        name=cls.names[cls.index]
        cls.index+=1

        if level<=7:
            return cls(name, "assistant", 5)
        elif level<=15:
            return cls(name, "guardian", 10)
        elif level<=50:
            return cls(name, "first one", 30)

    def __str__(self):
        return f"{self.name} | {self.monster_type} | power: {self.power}"


monsters=[]

for level in range(1, 40, 4):
    monsters.append(Monster.create_from_level(level))

for m in monsters:
    print(m)

#N3 -----------------------------------------------------------------

class SlotMachine:
    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def generate_numbers(numbers):
        return rd.choice(numbers)

    @classmethod
    def from_difficulty(cls, level):
        if level == 1:
            return cls([1, 2, 3, 4])
        elif level == 2:
            return cls([1, 2, 3, 4, 5])
        elif level == 3:
            return cls([1, 2, 3, 4, 5, 6])

    def play(self):
        first=self.generate_numbers(self.numbers)
        second=self.generate_numbers(self.numbers)
        third=self.generate_numbers(self.numbers)

        print(first, second, third)

        if first==second==third:
            print("You win")
        else:
            print("You lose")

play1=SlotMachine.from_difficulty(1)
play2=SlotMachine.from_difficulty(2)
play3=SlotMachine.from_difficulty(3)

play1.play()
play2.play()
play3.play()

#N4 ------------------------------------------------

class Hero:
    def __init__(self, health, score):
        self.__health = health
        self.__score = score

    @staticmethod
    def random_event():
        return rd.choice(["health", "score"])

    @classmethod
    def from_name(cls,name):
        hero=cls(100, 0)
        hero.name=name
        return hero

    def play(self):
        game=Hero.random_event()

        if game=="health":
            self.__health-=rd.randint(1,10)
            print(f"you got {self.__health} health left")
        elif game=="score":
            self.__score+=rd.randint(1,10)
            print(f"you got {self.__score} score")

        print(f"health = {self.__health} | score = {self.__score}")

    def alive(self):
        return self.__health > 0

class SuperHero(Hero):
    def __init__(self, name, power):
        super().__init__(100, 0)
        self.name = name
        self.power = power


hero=SuperHero("<NAME>", "<POWER>")
while hero.alive():
    hero.play()

#N5 ------------------------------------------------------------------

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self, cards):
        self.__cards = cards

    @classmethod
    def create_deck(cls):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K"]

        cards = []

        for suit in suits:
            for rank in ranks:
                cards.append(Card(rank, suit))

        return cls(cards)

    @staticmethod
    def shuffle(cards):
        rd.shuffle(cards)

    def deal(self):
        hand = []

        for i in range(5):
            hand.append(self.__cards.pop(0))

        return hand

deck = Deck.create_deck()

Deck.shuffle(deck._Deck__cards)

player_hand = deck.deal()

print("Player cards:")

for card in player_hand:
    print(card)

ranks=[]

for card in player_hand:
    ranks.append(card.rank)

if len(ranks)==len(set(ranks)):
    print("Player has the same rank")
else:
    print("Player has different ranks")