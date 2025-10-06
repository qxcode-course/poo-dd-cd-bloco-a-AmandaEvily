class Animal: 
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound 
        self.age: int = 0

    def grow(self, amount: int) -> None:
        self.age += amount
        if self.age >= 4:
            print(f"warning: {self.species} morreu")

    def growMax(self) -> int:
        if self.age > 4:
            self.age = 4
        return 4
    
    def makeSound(self) -> None:
        if self.age == 0:
            print("---")
        elif self.age >= 4:
            print("RIP")
        else:
            print(self.sound)
            
    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

def main():
    animal = Animal("","")
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "show":
            print(animal)
        elif args[0] == "grow":
            amount: int = int(args[1])
            animal.grow(amount)
            animal.growMax()
        elif args[0] == "noise":
            animal.makeSound()

main()    