large_string = """
Choice:
	1. user-input
	2. read .txt file

    """
def hash_function(_array_of_bits):
    modulo = 2 ** 256
    calculated_number: int = 1

    temporary_sum: int = 1
    temporary_index: int = 0
    bit_duo = []

    for i, _bit in enumerate(_array_of_bits):

        if _array_of_bits[i] == 0:
            temporary_sum *= (67429 ** (temporary_index + (i // 8)))
        else:
            temporary_sum *= (91997 ** (temporary_index + 1 + (i // 8)))

        if i >= 6 and (i % 6 == 0 or i % 6 == 1):
            bit_duo.append(_array_of_bits[i])


        if len(bit_duo) == 2:
            if bit_duo == [0, 0]: temporary_sum *= 5938474430905413401767207523544980081
            if bit_duo == [0, 1]: temporary_sum *= 2268752756812624175100564572640790511
            if bit_duo == [1, 1]: temporary_sum *= 9808407823880205631311916183101774079
            if bit_duo == [1, 0]: temporary_sum *= 8190922290267339622366176529252862003

        #reset everything if we passed 8 bits
        if (i + 1) % 8 == 0:
            calculated_number *= temporary_sum
            calculated_number = calculated_number  % modulo
            bit_duo = []
            temporary_sum = 1
            temporary_index = 0
        else:
            temporary_sum %= modulo
            temporary_index += 1

    return calculated_number

def encode_word(word_):
    encoded_text = word_.encode('utf-8')
    for letter in encoded_text:
        byte_form = format(letter, '08b')
        for bit in byte_form:
            array_of_bits.append(int(bit))

if __name__ == "__main__":
    array_of_bits = []
    user_input: int

    while True:
        user_input = int(input(large_string))

        if user_input == 1:
            word_to_hash = input("Enter the word you want to hash: ")
            encode_word(word_to_hash)
            number_received = hash_function(array_of_bits)
            hex_value = format(number_received, "064x")
            print(f"Word: {word}, hash: {hex_value}")

        elif user_input == 2:
            file_name = input("Enter file name: ")
            file_name += ".txt"
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    for line in f:
                        word = line.strip()
                        if not word:
                            continue
                        array_of_bits.clear()
                        encode_word(word)
                        number_received = hash_function(array_of_bits)
                        hex_value = format(number_received, "064x")
                        print(f"Word: {word}, hash: {hex_value}")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")