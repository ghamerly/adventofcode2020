def simulate(instructions):
    executed = [False] * len(instructions)

    pc = acc = 0

    while 0 <= pc < len(instructions) and not executed[pc]:
        executed[pc] = True
        cmd, offset = instructions[pc]
        if cmd == 'nop':
            pc += 1
        elif cmd == 'acc':
            pc += 1
            acc += offset
        elif cmd == 'jmp':
            pc += offset

    if pc == len(instructions):
        return acc

    return False

with open('8.in') as f:
    instructions = []
    for line in f:
        cmd, offset = line.split()
        instructions.append([cmd, int(offset)])

    other = { 'nop': 'jmp', 'jmp': 'nop' }

    for i in range(len(instructions)):
        if instructions[i][0] in ('nop', 'jmp'):
            #print(instructions[i])
            instructions[i][0] = other[instructions[i][0]]
            #print(instructions[i])
            ans = simulate(instructions)
            #print(i, ans)
            if ans is not False:
                print(ans)
            instructions[i][0] = other[instructions[i][0]]

