#!/usr/bin/python3.8

from typing import List, Tuple
import random
import sys

VectorStr = List[float] # VectorStr is the population
goal = ""

# Check if the solution is in the population
def checkSolutionInVectorStr(arrayStr: VectorStr) -> bool:
    pass

# Swap two characters in a string
def swapTwoRandomCharacterInString(str: str) -> str:
    pass

# Change one character randomly
def changeRandomlyOneCharacter(str: str) -> str:
    pass

# Create mutation with a probability of 10%
# A mutation is a random modification of the string
# It can be a swap of two characters, a change of one character or a random character, a revert string etc. per example
def mutationOfTenPercent(str: str) -> str:
    pass

# dictionnary is a dictionnary with the string (word) as key and the fitness as value
# Return a tuple with both words with highest fitness
def getTwoStringWithHighestFitness(dictionnary: dict) -> Tuple[str, str]:
    pass

# Get all possibilities of crossing over two strings
# Generate population with 'all possibilities' of crossing over two strings
# For example: if the two strings are "abc" and "def"
# The possibilities are: 'ade' or 'fab' or 'cde' or 'bdf' etc.
def getAllPossibilitiesOfCrossingOverTwoStrings(str1: str, str2: str) -> VectorStr:
    pass

# Create a string with random characters with a length of len
def createStringWithRandomChars(len: int) -> str:
    pass

# Initial population
# Generate a population with a size of arrLength
def initPopulation(arrLength: int) -> VectorStr:
    pass

# Calc the score of the string compared to the goal
# The score is the number of characters that are the same per example
def fitnessFunction(str: str) -> int:
    pass

# Calculate fitness for each string
# Generate a dictionnary with the string/word as key and the fitness as value
def createDictionnaryWithFitness(arrayStr: VectorStr) -> dict:
    pass

# Main function
# Return the final population
def GeneticAlgorithm() -> VectorStr:
    pass
    # Initial population
    # Compute fitness for each string
    # Until the population has converged to the goal
        # Select two strings with the highest fitness
        # Create a new population with all possibilities of crossing over two strings
        # Mutate the new population
        # Compute fitness for each string
    # Display final population

# Check if string has only alphabetic characters
def hasOnlyAlphabeticCharactersInLowerCase(str: str) -> bool:
    return str.isalpha() and str.islower()

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        if (hasOnlyAlphabeticCharactersInLowerCase(sys.argv[1])):
            goal = sys.argv[1]
            print("The goal : " + str(goal))
            GeneticAlgorithm()
            exit(0)
        else:
            print("Please enter a string composed only with characters in lower case.")
            exit(84)
    else:
        print("Please enter the goal as the first argument")
        exit(84)
