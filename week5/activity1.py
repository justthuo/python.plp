# Base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def display_info(self):
        print(f"🦸 Name: {self.name}, Power: {self.power}, Level: {self.level}")

    def attack(self):
        print(f"{self.name} attacks using {self.power}!")

# Inherited class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def display_info(self):
        super().display_info()
        print(f"✈️ Flight Speed: {self.flight_speed} km/h")

    def attack(self):
        print(f"{self.name} dives from the sky with {self.power}!")

# Create objects
hero1 = Superhero("Shadow Ninja", "Invisibility", 5)
hero2 = FlyingSuperhero("Sky Falcon", "Wind Blast", 8, 300)

# Use methods
hero1.display_info()
hero1.attack()
print("---")
hero2.display_info()
hero2.attack()
