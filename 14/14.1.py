import re

with open('14.in') as f:

    memory = {}

    p = re.compile(r'mem\[([0-9]+)\] = ([0-9]+)')

    for line in f:
        line = line.strip()

        if line.startswith('mask = '):
            mask = line[7:]
            assert len(mask) == 36
            mask_set = 0
            mask_clear = 0

            for b in mask:
                mask_set <<= 1
                mask_clear <<= 1
                if b != '0':
                    mask_clear |= 1
                if b == '1':
                    mask_set |= 1
        else:
            m = p.match(line)
            address = int(m.group(1))
            value = int(m.group(2))

            masked_value = (value | mask_set) & mask_clear

            memory[address] = masked_value

    print(sum(memory.values()))
