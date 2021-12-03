def part1():
    binary = data()
    gamma = ''

    for i in range(len(binary[0])):
        gamma += '1' if sum([int(x[i]) for x in binary]) > (len(binary) / 2) else '0'

    return int(gamma, 2) * (int(gamma, 2) ^ 0xFFF)

def part2():
    binary_ox = binary_c0 = data()

    for i in range(len(binary_ox[0])):
        common_digit_ox = '1' if sum([int(x[i]) for x in binary_ox]) >= (len(binary_ox) / 2) else '0'
        common_digit_c0 = '1' if sum([int(x[i]) for x in binary_c0]) >= (len(binary_c0) / 2) else '0'

        binary_ox = [x for x in binary_ox if x[i] == common_digit_ox or len(binary_ox) == 1]
        binary_c0 = [x for x in binary_c0 if x[i] != common_digit_c0 or len(binary_c0) == 1]

    return int(binary_ox[0], 2) * int(binary_c0[0], 2)

def data():
    return [line.rstrip() for line in open('input.txt', 'r')]

if __name__ == '__main__':
    print(part1())
    print(part2())
