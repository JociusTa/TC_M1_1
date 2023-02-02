import random

class DiceRoll:
    def __init__(self, sides, count, throws):
        self.sides = sides
        self.count = count
        self.throws = throws
        self.throw_results = []

    def roll_dice(self):
        for throw in range(self.throws):
            throw_result = []
            for dice in range(self.count):
                result = random.randint(1, self.sides)
                throw_result.append(result)
            self.throw_results.append(throw_result)
            self.trim_results()

    def trim_results(self):
        if len(self.throw_results) > 100:
            throw_results.pop(0)

    def print_results(self):
        for i, throw_result in enumerate(self.throw_results):
            results_length = len(throw_result)
            print("Throw {}: {} ; {} dice were thrown, with each having {}".format(
                i + 1, sum(throw_result), results_length, throw_result))

    def get_input(self, default, prompt, low, high):
        while True:
            try:
                user_input = input(prompt) or default
                user_input = int(user_input)
                if user_input < low or user_input > high:
                    raise ValueError
                return user_input
            except ValueError:
                print(f"Invalid input. Please enter a number between {low} and {high}.")

    def get_dice_input(self):
        self.count = self.get_input(self.count, "Enter number of dice (1-5): ", 1, 5)
        self.sides = self.get_input(self.sides, "Enter number of sides (1-100): ", 1, 100)
        self.throws = self.get_input(self.throws, "Enter number of throws (1 or more): ", 1, float('inf'))


dr = DiceRoll(sides=99, count=6, throws=3)
dr.get_dice_input()
results = dr.roll_dice()
dr.print_results()