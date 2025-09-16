class Towel: 
    def __init__(self, color: str, size: str):
        self.color: str = color 
        self.size: str = size
        self.wetness: int = 0

    def str (self):
        return f"color: {self.color}, tam:{self.size}, hum:{self.wetness}"

toalha = Towel("green", "G") #objetos
towel = Towel ("red","P")
outra = towel
towel.color = "blue"
outra.color = "blue"


print(toalha.color)
toalha.color = "white"
print(toalha.color)
print(toalha.size)
print(toalha.wetness)