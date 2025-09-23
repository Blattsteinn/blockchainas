large_string = """
Choice:
	1. user-input
	2. read .txt file
	3. Collisions check
	4. Bit comparison
	5. Hexadecimal comparison
	
	6. Read from file and write hexadecimal to file
	7. user-input + salt
	8. Konstitucijos testavimas
    """

import random
import time

def hash_function(_array_of_bits):
    MODULO = 2 ** 256

    # Large primes for mixing
    PRIME_INIT = 104395301
    PRIME_1 = 373587913
    PRIME_2 = 104729

    calculated_number: int = PRIME_INIT
    temporary_index: int = 0
    bit_duo = []

    for i, bit in enumerate(_array_of_bits):

        # Directly mix bit into calculated_number
        if bit == 0:
            calculated_number ^= pow(67429, temporary_index + (i // 8), MODULO)
        else:
            calculated_number ^= pow(91997, temporary_index + 1 + (i // 8), MODULO)

        # Track pairs of bits
        if i >= 6 and (i % 6 in (0, 1)):
            bit_duo.append(bit)

        if len(bit_duo) == 2:
            if bit_duo == [0, 0]:
                calculated_number ^= 5938474430905413401767207523544980081
            elif bit_duo == [0, 1]:
                calculated_number ^= 2268752756812624175100564572640790511
            elif bit_duo == [1, 1]:
                calculated_number ^= 9808407823880205631311916183101774079
            elif bit_duo == [1, 0]:
                calculated_number ^= 8190922290267339622366176529252862003
            calculated_number %= MODULO
            bit_duo = []  # reset immediately

        # Every 8 bits → apply stronger mixing
        if (i + 1) % 8 == 0:
            calculated_number = (calculated_number * PRIME_2 + PRIME_1) % MODULO
            # Small rotation
            calculated_number = ((calculated_number << 13) | (calculated_number >> (256 - 13))) % MODULO
            temporary_index = 0
        else:
            temporary_index += 1

    return calculated_number % MODULO

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
            file_name = input("Enter file name: ")
            try:
                with open("files" + file_name + "txt", "r", encoding="utf-8") as f:
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
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")

        elif user_input == 4:
            def hex_to_bin(hex_str):
                return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


            hashes = []
            file_name = input("Enter file name (hashes): ")
            try:
                with open("files" + file_name + "txt", "r", encoding="utf-8") as f:
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
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")

        elif user_input == 5:

            hashes = []

            file_name = input("Enter file name (hashes): ")
            try:
                with open("files" + file_name + "txt", "r", encoding="utf-8") as f:
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
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")

        elif user_input == 6:
            file_name = input("Enter file name: ")
            file_name += ".txt"
            file_name = "files/" + file_name

            files_out = input("Enter file name to create: ")
            files_out += ".txt"
            files_out = "files/" + files_out

            try:
                with open(file_name, "r", encoding="utf-8") as f, open(files_out,"w", encoding="utf-8") as out:
                    for line in f:
                        word = line.strip()
                        if not word:
                            continue
                        array_of_bits.clear()
                        encode_word(word)
                        number_received = hash_function(array_of_bits)
                        hex_value = format(number_received, "064x")
                        out.write(hex_value +'\n')
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")

        elif user_input == 7:
            word_to_hash = input("Enter the word you want to hash: ")

            letters_array = ['a','b','c','d','e','f', 'g', 'h']
            salt = ''.join(random.choice(letters_array) for _ in range(16))
            print(f"Generated salt {salt}")

            word_to_hash = salt + word_to_hash
            encode_word(word_to_hash)
            number_received = hash_function(array_of_bits)
            hex_value = format(number_received, "064x")
            print(f"Word: {word_to_hash[:20]}, hash: {hex_value}")

        elif user_input == 8:
            try:
                with open("konstitucija.txt", "r", encoding="utf-8") as f:
                    lines_to_hash = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print("File 'konstitucija.txt' not found.")
                continue

            num_lines = 1
            while num_lines <= 16:  # or any max block size you want
                print(f"Number of lines: {num_lines}")

                for j in range(6):
                    start_time = time.perf_counter()

                    # Process all consecutive blocks of size num_lines
                    for i in range(0, len(lines_to_hash), num_lines):
                        block = lines_to_hash[i:i + num_lines]
                        combined_string = "".join(block)

                        array_of_bits.clear()
                        encode_word(combined_string)

                        number_received = hash_function(array_of_bits)
                        hex_value = format(number_received, "064x")


                    end_time = time.perf_counter()
                    elapsed_time = (end_time - start_time)

                    print(f"{elapsed_time:.4f}")

                num_lines *= 2