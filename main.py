import random

throw_results = []
class DiceRoll:
    def __init__(self, sides=6, count=1, throws=2):
        self.sides = sides
        self.count = count
        self.throws = throws
    def roll_dice(self):
        for throw in range(self.throws):
            throw_result = []
            for dice in range(self.count):
                result = random.randint(1, self.sides)
                throw_result.append(result)
            throw_results.append(throw_result)
            self.trim_results()
    def trim_results(self):
        if len(throw_results) > 100:
            throw_results.pop(0)
    def print_results(self):
        for i, throw_result in enumerate(throw_results):
            print("Throw {}: {}".format(i + 1, throw_result))

dr = DiceRoll(sides=6, count=2, throws=3)
results = dr.roll_dice()
dr.print_results()