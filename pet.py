class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 1
        print(f"{self.name} has eaten and feels happier!")

    def sleep(self):
        self.energy += 5
        if self.energy > 10:
            self.energy = 10
        print(f"{self.name} had a nice nap and feels refreshed!")

    def play(self):
        self.energy -= 2
        if self.energy < 0:
            self.energy = 0
        self.happiness += 2
        if self.happiness > 10:
            self.happiness = 10
        self.hunger += 1
        if self.hunger > 10:
            self.hunger = 10
        print(f"You played with {self.name}! So much fun!")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        return self.tricks if self.tricks else ["No tricks learned yet!"]

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
        print("------------------------\n")
