# PREAMBLE
with open("input") as f:
    code = f.readline()  # D2FE28

# code = '38006F45291200'
# code = '04005AC33890'
# code = '8A004A801A8002F478'  # version sum = 16
# code = '620080001611562C8802118E34'  # version sum = 12
# code = 'C0015000016115A2E0802F182340'  # version sum = 23
# code = 'A0016C880162017C3686B18A3D4780'  # version sum = 31

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

# flag = True
while len(binary[index:]) > 6:

    print('\nBEGINNING:', binary[index:])
    version = int(extract(3), 2)
    versions.append(version)
    type_id = int(extract(3), 2)
    print("Version:", version)
    print("Type_id:", type_id)

    if type_id == 4:
        print('LITERAL VALUE!')

        packet_content = ''
        while True:
            sub_packet = extract(5)
            packet_content += sub_packet[1:]
            if sub_packet[0] == '0':
                break

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
    print('END:', binary[index:])

print(sum(versions))  # PART 1: 991 is correct!
