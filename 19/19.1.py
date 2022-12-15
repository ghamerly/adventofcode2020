import itertools
import re
import sys

def gen_all(rules, results, head):
    if head in results:
        return

    print(f'gen_all for {head}')

    results[head] = set()

    for rule in rules[head]:
        p = []
        for k in rule:
            if type(k) is int:
                gen_all(rules, results, k)
                p.append(results[k])
            else:
                p.append(k)
            
        for x in itertools.product(*p):
            #print(f'{head}: {x}')
            results[head].add(''.join(x))

#def parse(s, rules, terminals):
#    table = [[[terminals[si]] for si in s]]
#    print(f'initial: {table}')
#    for i in range(1, len(s)):
#        print(i)
#        table.append([[] for _ in s])
#        for j in range(len(s) - i):
#            for k in range(i):
#                a = table[i-k-1][j]
#                b = table[k][j+i-k]
#                for ai in a:
#                    for bi in b:
#                        #print(i, j, k, ai, bi)
#                        if (ai, bi) in rules:
#                            table[i][j].extend(rules.get((ai, bi)))
#
#        print(table[-1])
#
#    if table[-1][0]:
#        return True
#    return False


total = 0

with open('19.in') as f:
    rules = {}
    terminals = {}
    productions = {}

    for line in f:
        line = line.strip()
        print(line)
        if not line:
            gen_all(rules, productions, 0)
            continue

        if ':' in line:
            head, tail = line.split(': ')
            tails = tail.split(' | ') 

            head = int(head)
            rules[head] = []

            for t in tails:
                if '"' in t:
                    rules[head].append((t[1],))
                else:
                    rules[head].append(tuple(map(int, t.split())))

        elif line in productions[0]:
            total += 1

    print(total)

