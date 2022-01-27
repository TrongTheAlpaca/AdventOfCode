# PREAMBLE
with open("input") as f:
    code = f.readline()  # D2FE28



# PART 1
# code = '8A004A801A8002F478'  # version sum = 16
# code = '620080001611562C8802118E34'  # version sum = 12
# code = 'C0015000016115A2E0802F182340'  # version sum = 23
# code = 'A0016C880162017C3686B18A3D4780'  # version sum = 31


# PART 2
# code = 'C200B40A82'  # finds the sum of 1 and 2, resulting in the value 3.  # OKI
# code = '04005AC33890'  # finds the product of 6 and 9, resulting in the value 54.  # OKI
# code = '880086C3E88112'  # finds the minimum of 7, 8, and 9, resulting in the value 7.
# code = 'CE00C43D881120'  # finds the maximum of 7, 8, and 9, resulting in the value 9. # OKI
# code = 'D8005AC2A8F0'  # produces 1, because 5 is less than 15.
# code = 'F600BC2D8F'  # produces 0, because 5 is not greater than 15.
# code = '9C005AC2F8F0' # Produces 0, because 5 is not equal to 15.
# code = '9C0141080250320F1802104A08'  # produces 1, because 1 + 3 = 2 * 2.

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
# binary = bin(int(code, 16))[2:]
# binary = hex_to_bin[binary[0]] + binary[1:]

binary = ''.join([hex_to_bin[c] for c in code])
print(binary)
versions = []
index = 0


def extract(n_digits: int):
    global index
    digits = binary[index:index + n_digits]
    index += n_digits
    return digits


def proceed() -> int:
    global index
    global binary
    print("Current:", binary[index:])
    version = int(extract(3), 2)
    versions.append(version)
    type_id = int(extract(3), 2)

    if type_id == 4:
        print('LITERAL VALUE!')
        packet_content = ''
        while True:
            sub_packet = extract(5)
            packet_content += sub_packet[1:]
            if sub_packet[0] == '0':
                return int(packet_content, 2)

    else:
        print('OPERATOR!')

        length_type_id = int(extract(1))
        print('Length_type_id', length_type_id)

        subpacket_length = -1
        if length_type_id == 0:
            print('LEN15:', len(binary[index:]))
            if len(binary[index:]) < 15:
                print("LONGER!")
                print("\t", binary[index:])
                binary += '0' * (15 - len(binary[index:]))
                print("\t", binary[index:])
            subpacket_length = int(extract(15), 2)
        else:
            print('LEN11:', len(binary[index:]))
            if len(binary[index:]) < 11:
                print("LONGER!")
                print("\t", binary[index:])
                binary += '0' * (11 - len(binary[index:]))
                print("\t", binary[index:])
            subpacket_length = int(extract(11), 2)

        print("Subpacket Length =", subpacket_length)

        if type_id == 0:
            print("SUM")
            value = 0
            if length_type_id == 0:
                current_index_delta = index
                while (index - current_index_delta) < subpacket_length:
                    x = proceed()
                    value += x
            else:
                for i in range(subpacket_length):
                    value += proceed()

            return value

        elif type_id == 1:
            print("PRODUCT")
            value = 1
            if length_type_id == 0:
                current_index_delta = index
                while (index - current_index_delta) < subpacket_length:
                    x = proceed()
                    print('\t', x)
                    value *= x
            else:
                for i in range(subpacket_length):
                    x = proceed()
                    print('\t', x)
                    value *= x

            return value

        elif type_id == 2:
            print("MINIMUM")
            numbers = []
            if length_type_id == 0:
                current_index_delta = index
                while (index - current_index_delta) < subpacket_length:
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            else:
                for i in range(subpacket_length):
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            return min(numbers)

        elif type_id == 3:
            print("MAXIMUM")
            numbers = []
            if length_type_id == 0:
                current_index_delta = index
                while (index - current_index_delta) < subpacket_length:
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            else:
                for i in range(subpacket_length):
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            return max(numbers)

        elif type_id == 5:
            print("GREATER THAN")
            numbers = []
            if length_type_id == 0:
                current_index_delta = index
                while (index - current_index_delta) < subpacket_length:
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            else:
                for i in range(subpacket_length):
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            return 1 if numbers[0] > numbers[1] else 0

        elif type_id == 6:
            print("LESS THAN")
            numbers = []
            if length_type_id == 0:
                current_index_delta = index
                while (index - current_index_delta) < subpacket_length:
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            else:
                for i in range(subpacket_length):
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            return 1 if numbers[0] < numbers[1] else 0

        elif type_id == 7:
            print("EQUAL")
            numbers = []
            if length_type_id == 0:
                current_index_delta = index
                while (index - current_index_delta) < subpacket_length:
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            else:
                for i in range(subpacket_length):
                    x = proceed()
                    print('\t', x)
                    numbers.append(x)
            return 1 if numbers[0] == numbers[1] else 0

        else:
            raise NotImplementedError

    print('END:', binary[index:])


# print(sum(versions))  # PART 1: 991 is correct!
print("FINAL:", proceed())
