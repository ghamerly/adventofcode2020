tree = {}

with open('7.in') as f:
    for line in f:
        container, tail = line.strip().split(' bags contain ')
        contained = [c[:c.rfind(' ')] for c in tail[:-1].split(', ')]
        #print()
        #print(line.strip())
        if contained == ['no other']:
            contained = []
        #print(container, contained)

        for c in contained:
            c = c[c.find(' ')+1:]
            tree[c] = tree.get(c, set()) | {container}

    #print(tree)

    ans = set()

    frontier = {'shiny gold'}
    while frontier:
        #print(f'frontier: {frontier}')
        new_frontier = set()
        for c in frontier:
            #print(f'c = {c}, {tree.get(c)}')
            for d in tree.get(c, []):
                new_frontier.add(d)
                ans.add(d)

        frontier = new_frontier

    #print(ans)
    assert 'shiny gold' not in ans
    print(len(ans))
