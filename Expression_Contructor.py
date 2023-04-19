import itertools

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

O = {'+':7, '-':3, '*':5, '/':1}
P = {'+':lambda x,y:x+y,
     '-':lambda x,y:x-y,
     '*':lambda x,y:x*y,
     '/':lambda x,y:x/y}

def postfix_search(rest, stk, N):
    if len(stk) >= 2:
        y = (v2, r2) = stk.pop()
        x = (v1, r1) = stk.pop()
        for opr in O:
            if O[opr] > 0 and not (opr == '/' and v2 == 0):
                stk += [(P[opr](v1, v2), '('+r1+opr+r2+')')]
                O[opr] -= 1
                if postfix_search(rest, stk,N): return 1
                O[opr] += 1
                stk.pop()
        stk += [x, y]
    elif not rest:
        v, r = stk[0]
        if v == N: print(f"{r} = {N}")
        return v == N
    for x in list(rest):
        rest.remove(x)
        stk += [x]
        if postfix_search(rest, stk,N):
            return True
        stk.pop()
        rest += [x]

nums = [10,2,10]
target = 100
use_all = False
L = nums
N = target

postfix_search(list(zip(L, map(str, L))), [], N)
result = find_expression(nums, target, use_all)
print(f"{result[0]} = {result[1]}")
