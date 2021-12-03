def part1():
    binary = data()
    gamma, epsilon = '', ''
    mask = 0xFFF

    for i in range(len(binary[0])):
        gamma += '1' if sum([int(x[i]) for x in binary]) > (len(binary) / 2) else '0'

    return int(gamma, 2) * (int(gamma, 2) ^ mask)

def part2():
    binary = data()
    oxygen, carbon = 0, 0

    oxygen = get_common_digit(binary, True)
    carbon = get_common_digit(binary, False)

    return int(oxygen, 2) * int(carbon, 2)

def get_common_digit(binary, even):
    target_char, invert_char = ('1', '0') if even else ('0', '1')

    for i in range(len(binary[0])):
        common_digit = target_char if sum([int(x[i]) for x in binary]) >= (len(binary) / 2) else invert_char
        binary = [x for x in binary if x[i] == common_digit]

        if len(binary) == 1: return binary[0]

def data():
    return [line.rstrip() for line in open('input.txt', 'r')]

if __name__ == '__main__':
    print(part1())
    print(part2())
