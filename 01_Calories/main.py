"""Author: Daniel Röhrs"""
import os
from collections import deque

def calories(input: str) -> int:
    result = 0

    with open(input, 'r') as file:
        stack = []
        for line in file:
            if line == "\n":
                result = max(sum(stack), result)
                stack.clear()
            else:
                stack.append(int(line))

    return result

def topNCalories(input: str, n: int = 3) -> list[int]:
    with open(input, 'r') as file:
        results = []
        stack = []
        for line in file:
            if line == "\n":
                calSummed = sum(stack)
                stack.clear()
                results.append(calSummed)
            else:
                stack.append(int(line))

    return sorted(results, reverse=True)[:n]


if __name__ == "__main__":
    print(calories("01_calories/input.txt"))
    top3=topNCalories("01_Calories/input.txt", 3)
    print(top3, sum(top3))