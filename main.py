
def hash_function(_array_of_bytes):
    MOD = 2 ** 256 - 189  # Large prime for reduction
    calculated_number: int = 1
    for _array_of_bits in _array_of_bytes:
        bit_duo = []
        temporary_sum: int = 1

        for j in range(8):
            if j < 6:
                if _array_of_bits[j] == 0:
                    temporary_sum *= 67429 ** (j+1)
                if _array_of_bits[j] == 1:
                    temporary_sum *= 91997 ** (j+1)
            else:
                bit_duo.append(_array_of_bits[j])


        if bit_duo == [0, 0]: temporary_sum *= 410079252992648349570025508981
        if bit_duo == [0, 1]: temporary_sum *= 728730155706782142465312831289
        if bit_duo == [1, 1]: temporary_sum *= 233246422214829721422450466691
        if bit_duo == [1, 0]: temporary_sum *= 820249177872665494536846925429

        temporary_sum %= MOD
        calculated_number *= temporary_sum
        calculated_number %= MOD

    return calculated_number

if __name__ == "__main__":

    while True:
        word_to_hash = input("Enter the word you want to hash: ")
        #word_to_hash = 'moo'

        array_of_bytes = []

        encoded_text = word_to_hash.encode('utf-8')
        for letter in encoded_text:
            array_of_bits = []
            byte_form = format(letter, '08b')
            for bit in byte_form:
                array_of_bits.append(int(bit))
            array_of_bytes.append(array_of_bits)



        number_received = hash_function(array_of_bytes)

        hex_value = format(number_received, "x")
        print(hex_value)