import operator

def part1():
    position = (0, 0)
    instr_map = {
        'forward': (1, 0),
        'up': (0, -1),
        'down': (0, 1),
    }

    for line in data():
        position = tuple(map(operator.add, position, tuple(int(line[1]) * x for x in instr_map[line[0]])))

    return position[0] * position[1]

def part2():
    aim = 0
    depth = 0
    pos = 0

    for line in data():
        val = int(line[1])
        match line[0]:
            case 'down':
                aim += val
            case 'up':
                aim += -(val)
            case 'forward':
                pos += val
                depth += val * aim

    return pos * depth

def data():
    return [line.rstrip().split(' ') for line in open('input.txt', 'r')]

if __name__ == '__main__':
    print(part1())
    print(part2())
