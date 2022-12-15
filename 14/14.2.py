import re

def enumerate_address(mask_any, i, address):
    if i == len(mask_any):
        yield address
        return

    bit = 1 << mask_any[i]

    a = address & (((1 << 36) - 1) ^ bit)
    yield from enumerate_address(mask_any, i + 1, a)

    a = address | bit
    yield from enumerate_address(mask_any, i + 1, a)

with open('14.in') as f:
    memory = {}

    p = re.compile(r'mem\[([0-9]+)\] = ([0-9]+)')

    for line in f:
        line = line.strip()

        if line.startswith('mask = '):
            mask = line[7:]
            assert len(mask) == 36
            mask_set = 0
            mask_any = []

            for i, b in enumerate(mask):
                mask_set <<= 1
                if b == 'X':
                    mask_any.append(35 - i)
                if b == '1':
                    mask_set |= 1
            #print(f'mask       = {mask}')
            #print(f'mask_set   = {mask_set} = {mask_set:b}')
        else:
            m = p.match(line)
            address = int(m.group(1))
            value = int(m.group(2))

            masked_address = address | mask_set

            #print(f'original address = {address} = {address:b}, masked_address = {masked_address} = {masked_address:b}')
            #print(f'mask_any = {mask_any}, mask = {mask}')
            for a in enumerate_address(mask_any, 0, masked_address):
                #print(f' >> masked address = {a} = {a:b}')
                memory[a] = value

    print(sum(memory.values()))
