class Carro: 
    def __init__(self):
        self.pass_: int = 0
        self.km: float = 0
        self.passMax: int = 2
        self.gas: int = 0
        self.gasMax: int = 100
    
    def enter(self):
        if self.pass_ < self.passMax: self.pass_ += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.pass_ > 0:
            self.pass_ -= 1
        else: 
            print("fail: nao ha ninguem no carro")

    def fuel(self, amount: int):
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if distance <= self.gas:
            self.gas -= distance
            self.km += distance
        else: 
            possible_distance = self.gas
            self.km += possible_distance
            self.gas = 0
            print(f"fail: tanque vazio apos andar {possible_distance:} km")

    def __str__(self):
        return f"pass: {self.pass_}, gas: {self.gas:}, km: {self.km}"
    
def main():
    car = Carro ()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "show":
            print(car)
        elif cmd == "enter":
            car.enter()
        elif cmd == "leave":
            car.leave()
        elif cmd == "fuel":
            car.fuel(int(args[1]))
        elif cmd == "drive":
            car.drive(int(args[1]))
        else:
            print("fail: coamndo invalido")

main()