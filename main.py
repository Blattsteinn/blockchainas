
def hash_function(_array_of_bits):
    modulo = 2 ** 256 - 189
    calculated_number: int = 1

    temporary_sum: int = 1
    temporary_index: int = 0
    bit_duo = []
    print(_array_of_bits)
    for i, _bit in enumerate(_array_of_bits):

        if (i + 1) % 8 == 0:
            calculated_number *= temporary_sum
            calculated_number %= modulo

            bit_duo = []
            temporary_sum = 1
            temporary_index = 0


        if _array_of_bits[i] == 0:
            temporary_sum *= 67429 ** (temporary_index+1)
        else:
            temporary_sum *= 91997 ** (temporary_index+1)

        if i >= 6 and (i % 6 == 0 or i % 6 == 1):
            bit_duo.append(_array_of_bits[i])

        if len(bit_duo) == 2:
            if bit_duo == [0, 0]: temporary_sum *= 410079252992648349570025508981
            if bit_duo == [0, 1]: temporary_sum *= 728730155706782142465312831289
            if bit_duo == [1, 1]: temporary_sum *= 233246422214829721422450466691
            if bit_duo == [1, 0]: temporary_sum *= 820249177872665494536846925429

        temporary_sum %= modulo
        print(temporary_sum)

    return calculated_number

if __name__ == "__main__":

    while True:
        word_to_hash = input("Enter the word you want to hash: ")
        #word_to_hash = 'moo'

        array_of_bits = []

        encoded_text = word_to_hash.encode('utf-8')
        for letter in encoded_text:
            byte_form = format(letter, '08b')
            for bit in byte_form:
                array_of_bits.append(int(bit))


        number_received = hash_function(array_of_bits)
        hex_value = format(number_received, "x")
        print(hex_value)