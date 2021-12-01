def part1():
    sonar = data()

    return sum([1 if y > x else 0 for x, y in zip(sonar, sonar[1:])])

def part2():
    sonar = data()

    return sum([1 if (b + c + d) > (a + b + c) else 0 for a, b, c, d in zip(sonar, sonar[1:], sonar[2:], sonar[3:])])

def data():
    return [int(line.rstrip()) for line in open('input.txt', 'r')]

if __name__ == '__main__':
    print(part1())
    print(part2())
