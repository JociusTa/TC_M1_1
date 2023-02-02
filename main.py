import random
from fastapi import FastAPI
app = FastAPI()
import csv


class DiceRoll:
    """
    A class for simulating the rolling of dice.

    Attributes:
    - sides (int): The number of sides of each dice.
    - count (int): The number of dice to roll.
    - throws (int): The number of times to roll the dice.
    - throw_results (list): A list of the results of each throw, where each result
      is a list of integers representing the value of each dice.

    Methods:
    - roll_dice: Rolls the dice the specified number of times and appends the results
      to the `throw_results` list.
    - trim_results: Trims the `throw_results` list to keep only the last 100 results.
    - print_results: Prints the results of each throw, including the total value of the
      dice, the number of dice rolled, and the value of each dice.
    - get_input: Prompts the user for input and returns the input if it is within the
      specified range, otherwise it returns the default value.
    - get_dice_input: Prompts the user for the number of dice, sides, and throws.
    """

    def __init__(self, sides=6, count=1, throws=6):
        self.sides = sides
        self.count = count
        self.throws = throws
        self.throw_results = []

    def roll_dice(self):
        """
        Rolls the dice the specified number of times and appends the results
        to the `throw_results` list.
        """
        for throw in range(self.throws):
            throw_result = []
            for dice in range(self.count):
                result = random.randint(1, self.sides)
                throw_result.append(result)
            self.throw_results.append(throw_result)

    def print_results(self):
        """
        Prints the results of each throw, including the total value of the
        dice, the number of dice rolled, and the value of each dice.
        """
        for i, throw_result in enumerate(self.throw_results):
            results_length = len(throw_result)
            print("Throw {}: {} ; {} dice were thrown, with each having {}".format(
                i + 1, sum(throw_result), results_length, throw_result))

    def dice_input_logic(self, default, prompt, low, high):
        """
        Prompts the user for input and returns the input if it is within the
        specified range, otherwise it returns the default value.

        Parameters:
        - default (int): The default value to use if the user input is invalid.
        - prompt (str): The prompt to display to the user.
        - low (int): The lower bound of the allowed input range.
        - high (int): The upper bound of the allowed input range.
        """
        while True:
            try:
                user_input = input(prompt)
                if user_input == "":
                    return default
                if user_input < low or user_input > high:
                    user_input = int(user_input)
                    raise ValueError
                return user_input
            except ValueError:
                print(f"Invalid input. Please enter a number between {low} and {high}.")

    def get_dice_input(self):
        """
        A function that takes user input to set the number of dice, sides and throws to be used in a dice game.
        """
        self.count = self.dice_input_logic(self.count, "Enter number of dice (1-5), [default 1]: ", 1, 5)
        self.sides = self.dice_input_logic(self.sides, "Enter number of sides (1-100): [default 6] ", 1, 100)
        self.throws = self.dice_input_logic(self.throws, "Enter number of throws (1 or more): [default 6]", 1, float('inf'))

dr = DiceRoll()
dr.get_dice_input()
results = dr.roll_dice()
dr.print_results()
