class Fishbread:
    def __init__(self, type, price):
        self.type = type
        self.price = price
        self.total = 0

    def sell(self):
        print(f"{self.type}을 {self.price}에 팔았습니다.")
        self.total += self.price

슈크림 = Fishbread("슈크림붕어빵", 1000)

슈크림.sell()
슈크림.sell()
슈크림.sell()
슈크림.sell()
print(슈크림.total)