large_string = """
Choice:
	1. user-input
	2. read .txt file
	3. Collisions check
	4. Bit comparison
	5. Hexadecimal comparison
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
            print(f"Word: {word_to_hash[:20]}, hash: {hex_value}")

        elif user_input == 2:
            file_name = input("Enter file name: ")
            file_name += ".txt"
            file_name = "files/" + file_name
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
                        print(f"Word: {word[:20]}, hash: {hex_value}")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")

        elif user_input == 3:
            hashes = []
            with open("files/random_strings_hashed_100k.txt", "r", encoding="utf-8") as f:
                for idx,line in enumerate(f):
                    hashes.append(line.strip())
            count: int = 0
            seen = set()
            duplicates = set()

            for h in hashes:
                if h in seen:
                    count += 1
                    duplicates.add(h)
                else:
                    seen.add(h)

            print(f"Number of duplicate hashes: {len(duplicates)}")
            print(f"Total duplicate occurrences: {count}")

        elif user_input == 4:
            def hex_to_bin(hex_str):
                return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


            hashes = []
            with open("files/similar_strings_hashed_100k.txt", "r", encoding="utf-8") as f:
                for line in f:
                    hashes.append(line.strip())


            difference_of_percentages = []

            total: float = 0.0
            different: int = 0
            for i in range(len(hashes) - 1):
                b1 = hex_to_bin(hashes[i])
                b2 = hex_to_bin(hashes[i + 1])
                different: int = 0
                for bit1, bit2 in zip(b1, b2):
                    if bit1 != bit2:
                        different += 1

                difference_of_percentages.append(different / len(b1)*100)
            percent_diff = sum(difference_of_percentages) / len(difference_of_percentages)

            print("Min:", min(difference_of_percentages))
            print("Max:", max(difference_of_percentages))
            print("Average:", percent_diff)

        elif user_input == 5:

            hashes = []
            with open("files/similar_strings_hashed_100k.txt", "r", encoding="utf-8") as f:
                for line in f:
                    hashes.append(line.strip())


            difference_of_percentages = []

            total: float = 0.0
            different: int = 0
            for i in range(len(hashes) - 1):
                different: int = 0
                for character1, character2 in zip(hashes[i], hashes[i + 1]):
                    if character1 != character2:
                        different += 1

                difference_of_percentages.append(different / 64 *100)
            percent_diff = sum(difference_of_percentages) / len(difference_of_percentages)

            print("Min:", min(difference_of_percentages))
            print("Max:", max(difference_of_percentages))
            print("Average:", percent_diff)
