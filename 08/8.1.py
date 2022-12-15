with open('8.in') as f:
    instructions = []
    for line in f:
        cmd, offset = line.split()
        instructions.append((cmd, int(offset)))

    executed = [False] * len(instructions)

    pc = 0
    acc = 0

    while not executed[pc]:
        executed[pc] = True
        cmd, offset = instructions[pc]
        if cmd == 'nop':
            pc += 1
        elif cmd == 'acc':
            pc += 1
            acc += offset
        elif cmd == 'jmp':
            pc += offset
            assert 0 <= pc < len(instructions)

    print(acc)
