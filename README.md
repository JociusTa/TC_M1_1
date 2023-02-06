# Summary
  The goal of this project was to create a dice rolling porgram, which had to 
  support user inputs for dice sides, number of throws and number of dice that should be thrown.
  The question had several requirements:

## Mandatory
- The solution should support from 1 to 5 dice. [ Developed in the main branch]
- The dice can have from 1 to 100 sides. [Developed in the main branch]
- The solution should be able to simulate throwing the dice one or more times, returning the values of the dice. [Developed in the main branch]
- The solution needs to store the information about the last 100 throws. [Skipped]
- The solution should be properly documented. [Both docstrings and README.md updated]
- Provide suggestions about how your solution can be improved. [The solution should have a way to choose from api or use input, storing throws should also be developped.]

## Optional
- Write unit tests for code.[Implemented in the advanced features branch]
- Create a web API for your module. [Implemented in the advanced features branch, seperate script added to post the input]
- Expand your solution to support weighted dice. [Not added]
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
- print_results: Prints the results of each throw, including the total value of the
  dice, the number of dice rolled, and the value of each dice.
- get_input: Prompts the user for input and returns the input if it is within the
  specified range, otherwise it returns the default value.
- get_dice_input: Prompts the user for the number of dice, sides, and throws. 
##Usage
To use the DiceRoll class, create an instance of the class and call the get_dice_input method to set the number of dice, sides, and throws. Then call the roll_dice method to simulate the dice rolls, and finally call the print_results method to view the results.

- dr = DiceRoll()
- dr.get_dice_input()
- dr.roll_dice()
- dr.print_results()