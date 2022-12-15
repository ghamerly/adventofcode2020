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
            results[head].add(''.join(x))

def match_11(productions, sub):
    # 42 31 | 42 11 31
    eleven_pattern = re.compile('^(' + '|'.join(productions[42]) + ')(.*)(' + '|'.join(productions[31]) + ')$')

    print(f'match_11: {sub}')

    if sub == '':
        return True

    m = eleven_pattern.match(sub)
    if m:
        return match_11(productions, m.group(2))
    
    return False

def match_0(productions, line):
    # 8 11

    s = line
    p = re.compile('^(' + '|'.join(productions[8]) + ')(.+)')

    m = p.match(s)
    while m:
        x, y = m.groups()
        assert x + y == s
        if match_11(productions, y):
            return True
        s = s[len(m.group(1)):]
        m = p.match(s)

    return False

total = 0

with open('19.in') as f:
    rules = {}
    terminals = {}
    productions = {}

    for line in f:
        line = line.strip()
        #print(line)
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

        else:
            if match_0(productions, line):
                total += 1
            pass

    print(total)

