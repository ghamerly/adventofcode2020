import re
import sys

priority = {
        '*': 1,
        '+': 0,
        '(': 100
        }

def applyOp(operands, operators):
    op = operators.pop()
    b = operands.pop()
    a = operands.pop()
    if op == '+':
        operands.append(a + b)
    elif op == '*':
        operands.append(a * b)

s = 0
with open('18.in') as f:
    for line in f:
        tokens = list(filter(None, re.split(r'(\(|\)|[0-9]+|[-+*])|\s', line.strip())))

        operands = []
        operators = []

        for t in tokens:
            if t in ('+', '*'):
                while operators and priority[operators[-1]] < priority[t]:
                    applyOp(operands, operators)
                operators.append(t)
            elif t == '(':
                operators.append(t)
            elif t == ')':
                while operators[-1] != '(':
                    applyOp(operands, operators)
                operators.pop()
            else:
                operands.append(int(t))

        while operators:
            applyOp(operands, operators)

        assert not operators
        assert len(operands) == 1
        s += operands[0]
        print(operands, operators)

print(s)
