# я не стал использовать collection, не хочу что-то усложнять в пустую, наверное я голандец)
# использую collection либо в дз4 либо в дз6, там где они действительно нужны
letter_to_digit = {
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f'
}


def hex_to_decimal(hex_digit: list):
    decimal_digit = 0
    for index, i in enumerate(hex_digit[::-1], 0):
        if str(i).isdigit():
            decimal_digit += int(i) * 16 ** index
        else:
            if not i.lower() in letter_to_digit:
                print('You enter incorrect digit')
                exit(0)
            decimal_digit += letter_to_digit[i.lower()] * 16 ** index
    return decimal_digit


def decimal_to_hex(decimal_digit):
    hex_digit = []
    while decimal_digit != 0:
        if decimal_digit % 16 > 9:
            hex_digit.append(letter_to_digit[decimal_digit % 16].upper())
        else:
            hex_digit.append(decimal_digit % 16)
        decimal_digit //= 16
    return ''.join(map(str, hex_digit[::-1]))


if __name__ == '__main__':
    first_hex, second_hex = map(list, input('Input two hex numbers through whitespace - ').split())
    summ = hex_to_decimal(first_hex) + hex_to_decimal(second_hex)
    multiple = hex_to_decimal(first_hex) * hex_to_decimal(second_hex)

    print(f'Sum of {"".join(first_hex)} + {"".join(second_hex)} = {decimal_to_hex(summ)} ')
    print(f'Multiple of {"".join(first_hex)} * {"".join(second_hex)} = {decimal_to_hex(multiple)} ')
