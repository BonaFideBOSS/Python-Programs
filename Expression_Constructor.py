from itertools import combinations, product, zip_longest
from functools import lru_cache


class Solutions:
    def __init__(self, numbers):
        self.all_numbers = numbers
        self.size = len(numbers)
        self.all_groups = self.unique_groups()

    def unique_groups(self):
        all_groups = {}
        all_numbers, size = self.all_numbers, self.size
        for m in range(1, size + 1):
            for numbers in combinations(all_numbers, m):
                if numbers in all_groups:
                    continue
                all_groups[numbers] = Group(numbers, all_groups)
        return all_groups

    def walk(self):
        for group in self.all_groups.values():
            yield from group.calculations


class Group:
    def __init__(self, numbers, all_groups):
        self.numbers = numbers
        self.size = len(numbers)
        self.partitions = list(self.partition_into_unique_pairs(all_groups))
        self.calculations = list(self.perform_calculations())

    def __repr__(self):
        return str(self.numbers)

    def partition_into_unique_pairs(self, all_groups):
        if self.size == 1:
            return
        numbers, size = self.numbers, self.size
        limits = (self.halfbinom(size, size // 2),)
        unique_numbers = set()
        for m, limit in zip_longest(range((size + 1) // 2, size), limits):
            for numbers1, numbers2 in self.paired_combinations(numbers, m, limit):
                if numbers1 in unique_numbers:
                    continue
                unique_numbers.add(numbers1)
                group1, group2 = all_groups[numbers1], all_groups[numbers2]
                yield (group1, group2)

    def perform_calculations(self):
        if self.size == 1:
            yield Calculation.singleton(self.numbers[0])
            return
        for group1, group2 in self.partitions:
            for calc1, calc2 in product(group1.calculations, group2.calculations):
                yield from Calculation.generate(calc1, calc2)

    @classmethod
    def paired_combinations(cls, numbers, m, limit):
        for cnt, numbers1 in enumerate(combinations(numbers, m), 1):
            numbers2 = tuple(cls.filtering(numbers, numbers1))
            yield (numbers1, numbers2)
            if cnt == limit:
                return

    @staticmethod
    def filtering(iterable, elements):
        elems = iter(elements)
        k = next(elems, None)
        for n in iterable:
            if n == k:
                k = next(elems, None)
            else:
                yield n

    @staticmethod
    @lru_cache()
    def halfbinom(n, k):
        if n % 2 == 1:
            return None
        prod = 1
        for m, l in zip(reversed(range(n + 1 - k, n + 1)), range(1, k + 1)):
            prod = (prod * m) // l
        return prod // 2


class Calculation:
    def __init__(self, expression, result, is_singleton=False):
        self.expr = expression
        self.result = result
        self.is_singleton = is_singleton

    def __repr__(self):
        return self.expr

    @classmethod
    def singleton(cls, n):
        return cls(f"{n}", n, is_singleton=True)

    @classmethod
    def generate(cls, calca, calcb):
        if calca.result < calcb.result:
            calca, calcb = calcb, calca
        for result, op in cls.operations(calca.result, calcb.result):
            expr1 = f"{calca.expr}" if calca.is_singleton else f"({calca.expr})"
            expr2 = f"{calcb.expr}" if calcb.is_singleton else f"({calcb.expr})"
            yield cls(f"{expr1} {op} {expr2}", result)

    @staticmethod
    def operations(x, y):
        yield (x + y, "+")
        if x > y:
            yield (x - y, "-")
        if y > 1 and x > 1:
            yield (x * y, "x")
        if y > 1 and x % y == 0:
            yield (x // y, "/")


def countdown_solver(target, numbers):
    try:
        target = int(target)
        unsorted_numbers = (int(n) for n in numbers)
        numbers = tuple(sorted(unsorted_numbers, reverse=True))
    except (IndexError, ValueError):
        print("You must provide a target and numbers!")
        return

    solutions = Solutions(numbers)
    smallest_difference = target
    bestresults = []
    for calculation in solutions.walk():
        diff = abs(calculation.result - target)
        if diff <= smallest_difference:
            if diff < smallest_difference:
                bestresults = [calculation]
                smallest_difference = diff
            else:
                bestresults.append(calculation)
    output(target, smallest_difference, bestresults)


def output(target, diff, results):
    print(f"\nThe closest results differ from {target} by {diff}. They are:\n")
    for index, calculation in enumerate(results, start=1):
        print(f"[{index}] {calculation.result} = {calculation.expr}")


def program():
    query = input("Please enter a target number and a list of numbers: ").split(" ")
    target = query[0]
    numbers = query[1:]
    countdown_solver(target, numbers)
    run_again()


def run_again():
    check_again = input("\nDo you want to run the program again? [Y/N]")

    if check_again.upper() == "Y":
        program()
    elif check_again.upper() == "N":
        print("Closing the program.")
    else:
        run_again()


intro = """
    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
    |         COUNTDOWN SOLVER a.k.a EXPRESSION CONSRUCTOR          |
    |                                                               |
    | Usage:                                                        |
    | >> TARGET_NUMBER LIST_OF_NUMBERS                              |
    |                                                               |
    | Example:                                                      |
    | >> 150 6 10 9 6 5                                             |
    |     ^  ----^-----                                             |
    |   Target Numbers                                              |
    |                                                               |
    |_______________________________________________________________|
"""
print(intro)
program()
