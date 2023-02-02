# DiceRoll
A Python class for simulating the rolling of dice.

## Attributes:
- sides (int): The number of sides of each dice.
- count (int): The number of dice to roll.
- throws (int): The number of times to roll the dice.
- throw_results (list): A list of the results of each throw, where each result
  is a list of integers representing the value of each dice.

## Methods:
- roll_dice: Rolls the dice the specified number of times and appends the results
  to the `throw_results` list.
- trim_results: Trims the `throw_results` list to keep only the last 100 results.
- print_results: Prints the results of each throw, including the total value of the
  dice, the number of dice rolled, and the value of each dice.
- get_input: Prompts the user for input and returns the input if it is within the
  specified range, otherwise it returns the default value.
- get_dice_input: Prompts the user for the number of dice, sides, and throws.
git 