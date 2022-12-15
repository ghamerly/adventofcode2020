import re

def parseOne(tokens):
    s = int(tokens[0])
    lastOp = None
    for x in tokens[1:]:
        if x in '+-*':
            lastOp = x
        elif lastOp == '+':
            s += int(x)
        elif lastOp == '-':
            s -= int(x)
        elif lastOp == '*':
            s *= int(x)
        else:
            assert False

    return s

s = 0
with open('18.in') as f:
    for line in f:
        tokens = list(filter(None, re.split(r'(\(|\)|[0-9]+|[-+*])|\s', line.strip())))

        stack = [[]]

        for t in tokens:
            if t == '(':
                stack.append([])
            elif t == ')':
                val = parseOne(stack.pop())
                stack[-1].append(str(val))
            else:
                stack[-1].append(t)

        s += parseOne(stack.pop())

    print('sum =', s)

