#!/usr/bin/python3.8

from typing import List, Tuple
import random
import sys

VectorStr = List[float] # VectorStr is the population
goal = ""

# Check if the solution is in the population
def checkSolutionInVectorStr(arrayStr: VectorStr) -> bool:
    for str in arrayStr:
        if (str == goal):
            return True
    return False

# Swap two characters in a string
def swapTwoRandomCharacterInString(str: str) -> str:
    i: int = random.randint(0, len(str) - 1)
    j: int = random.randint(0, len(str) - 1)
    arr = list(str)
    arr[i], arr[j] = arr[j], arr[i]
    return "".join(arr)

# Change one character randomly
def changeRandomlyOneCharacter(str: str) -> str:
    i: int = random.randint(0, len(str) - 1)
    arr = list(str)
    arr[i] = chr(random.randint(97, 122))
    return "".join(arr)

# Create Mutation with a probability of 10%
# You can upgrade this function to mutate with differents methods
def mutationOfTenPercent(str: str) -> str:
    if (random.random() < 0.1):
        if (random.random() < 0.5):
            return changeRandomlyOneCharacter(str)
        else:
            return swapTwoRandomCharacterInString(str) # Change one character randomly
    else:
        return str

# Get two strings with highest fitness
def getTwoStringWithHighestFitness(dictionnary: dict) -> Tuple[str, str]:
    highest: str = random.choice(list(dictionnary.keys()))
    secondHighest: str = random.choice(list(dictionnary.keys()))
    for str in dictionnary:
        if (dictionnary[str] > dictionnary[highest]):
            secondHighest = highest
            highest = str
        elif (dictionnary[str] > dictionnary[secondHighest]):
            secondHighest = str
    return (highest, secondHighest)

# Get all possibilities of crossing over two strings
# You can upgrade this function to more possibilities
def getAllPossibilitiesOfCrossingOverTwoStrings(str1: str, str2: str) -> VectorStr:
    possibilities: VectorStr = []
    for i in range(len(str1)):
        possibilities.append(str1[:i] + str2[i:])
    return possibilities

# Create a string with random characters with a length of len
def createStringWithRandomChars(len: int) -> str:
    string: str = ""
    for i in range(len):
        string += chr(random.randint(97, 122))
    return string

# Initial population
# Generate a population with a size of arrLength
def initPopulation(arrLength: int) -> VectorStr:
    arr: VectorStr = []
    
    for i in range(arrLength):
        arr.append(createStringWithRandomChars(len(goal)))
    return arr

# Calc the score of the string compared to the goal
# You can upgrade this fitness function to get a better result
def fitnessFunction(str: str) -> int:
    res: str = goal
    score: int = 0
    i: int = 0
    j: int = 0
    while i < len(res):
        j = 0
        while j < len(str):
            if (res[i] == str[j]):
                arr = list(str)
                arr[j] = '~'
                str = "".join(arr)

                arr = list(res)
                arr[i] = '-'
                res = "".join(arr)

                score += 1
            j += 1
        i += 1
    return score

# Calculate fitness for each string
def createDictionnaryWithFitness(arrayStr: VectorStr) -> dict:
    dictionnary: dict = {}
    for str in arrayStr:
        dictionnary[str] = fitnessFunction(str)
    return dictionnary

# Main function
def GeneticAlgorithm() -> VectorStr:
    nbGeneration: int = 0
    population: VectorStr = initPopulation(30)
    print("Initial population: " + str(population))
    dictionnary: dict = createDictionnaryWithFitness(population)
    while not checkSolutionInVectorStr(population):
        highest, secondHighest = getTwoStringWithHighestFitness(dictionnary)
        population = getAllPossibilitiesOfCrossingOverTwoStrings(highest, secondHighest)
        for i in range(len(population)):
            population[i] = mutationOfTenPercent(population[i])
        dictionnary = createDictionnaryWithFitness(population)
        nbGeneration += 1
        print("Population :", population)
    print("Solution found in " + str(nbGeneration) + " generations")
    return population

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
