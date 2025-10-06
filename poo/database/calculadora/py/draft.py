class Calculadora:
    def __init__(self, batteryMax: int):
        self.battery: int = 0
        self.batteryMax: int = batteryMax
        self.display: float = 0.0

    def charge(self, value: int):
        self.battery += value
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def spend_battery(self) -> bool:
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return False
        self.battery -= 1
        return True
    
    def sum(self, a: float, b: float):
        if not self.spend_battery():
            return
        self.display = a + b

    # ADICIONADO: O método div, que estava faltando.
    def div(self, a: float, b: float):
        if b == 0:
            print("fail: divisao por zero")
            return
        if not self.spend_battery():
            return
        self.display = a / b

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"

def main():
    calc = None
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "init":
            calc = Calculadora(int(args[1]))
        elif calc is None:
            print("fail: calculadora nao iniciada")
        elif cmd == "show":
            print(calc)
        elif cmd == "charge":
            calc.charge(int(args[1]))
        elif cmd == "sum":
            calc.sum(float(args[1]), float(args[2]))
        elif cmd == "div":
            calc.div(float(args[1]), float(args[2]))
        else:
            print("fail: comando invalido")

main()