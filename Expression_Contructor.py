import itertools
import math

def find_expression(numbers, target, use_all=False):
    combinations = []
    for i in range(2, len(numbers) + 1):
        combinations += itertools.permutations(numbers, i)

    closest = None

    for c in combinations:
        if use_all and len(c) != len(numbers):
            continue

        operators = list(itertools.product(['+', '-', '*', '/'], repeat=len(c) - 1))

        for o in operators:
            expression = ''
            for i in range(len(c) - 1):
                expression += str(c[i]) + o[i]
            expression += str(c[-1])

            try:
                value = eval(expression)
            except ZeroDivisionError:
                continue

            if value == target:
                return (expression, value)

            if closest is None or abs(target - value) < abs(target - closest[1]):
                closest = (expression,value)
    return closest

nums = [10,5,2,10]
target = 100
use_all = False

result = find_expression(nums, target, use_all)
print(f"Result: {result[0]} = {result[1]}")
