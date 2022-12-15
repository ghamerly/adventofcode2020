
def search(t, c, ans):
    print(c)

    if c not in t:
        print('* base')
        return 1

    if c not in ans:
        ans[c] = 1
        for count, bagname in t[c]:
            ans[c] += count * search(t, bagname, ans)

    print(f'c => {ans[c]}')

    return ans[c]


tree = {}

with open('7.in') as f:
    for line in f:
        container, tail = line.strip().split(' bags contain ')
        contained = [c[:c.rfind(' ')] for c in tail[:-1].split(', ')]
        if contained == ['no other']:
            contained = []

        tree[container] = []
        for c in contained:
            count, bagname = c.split(' ', 1)
            count = int(count)
            tree[container].append((count, bagname))

   #for k in tree:
   #    print(k, tree[k])

    #print()

    print(search(tree, 'shiny gold', {}) - 1)

