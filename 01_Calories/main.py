"""Author: Daniel Röhrs"""
import os

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


if __name__ == "__main__":
    print(calories("01_calories/input.txt"))