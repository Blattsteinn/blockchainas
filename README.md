
# Hash Function Logic

## Overview
This repository contains a Python script with a custom hash function that converts a text string into a 64 digit hexadecimal number through some arithmetic.

## Input
The input can be:  
1. A single word entered by the user.  
2. A `.txt` file with words, one per line.  

## Hashing process pseudo-code
```python
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

```
1. We pass an `array_of_bytes[]` into the `hash_function()`.
2. For every 8 bits of  `array_of_bits[]`, a temporary variables `temporary_sum = 1` & `temporary_index = 1` is created to.

3. For each bit in `_array_of_bits`:  
   - If the bit is `0`, `temporary_sum`  is multiplied by `67429` raised to `(temporary_index + (i // 8))`.  
   - If the bit is `1`, `temporary_sum`  is multiplied by `91997` raised to `(temporary_index + 1 + (i // 8))`.  
4. For every 6th & 7th bit (6, 7, 12, 13, 18, 19, 24, 25, …), we collect them as `bit_duo[]`.
   Depending on bit_duo[] value we'll multiply `temporary_sum` by:
    
    -   if `[0, 0]` multiplies by `410079252992648349570025508981`
    -   if `[0, 1]` multiplies by `728730155706782142465312831289`
    -   if `[1, 1]` multiplies by `233246422214829721422450466691`
    -   if `[1, 0]` multiplies by `820249177872665494536846925429`
5. After each 8-bit block, we multiply `calculated_number` by `temporary_sum`, reduce modulo `2**256`, and reset `temporary_sum` and `bit_duo`.  
6. Continue until all bits are processed. The function returns `calculated_number`.


**Note:** All numbers here randomly chosen large prime numbers.
 
## Output
The result then is converted to a 64-digit hexadecimal string:  
```python
number = hash_function(array_of_bits)
hex_value = format(number, "064x")
```
# Testing

## Efficiency measure


| Test    | 1 row  | 2 rows | 4 rows | 8 rows | 16 rows |
|---------|--------|--------|--------|--------|---------|
| 1       | 2.1688 | 3.1713 | 6.2848 | 15.158 | 46.9324 |
| 2       | 2.0810 | 3.1958 | 6.6905 | 13.3014| 47.0546 |
| 3       | 2.0885 | 3.1468 | 5.9326 | 13.2324| 31.4662 |
| 4       | 2.1176 | 3.2275 | 5.9186 | 13.1107| 30.2204 |
| 5       | 2.1142 | 3.1930 | 5.8710 | 13.1466| 29.3681 |
| **Average** | **2.11402** | **3.18688** | **6.1395** | **13.58982** | **37.00834** |

This table shows how long it takes (in seconds) to hash different numbers of lines from the file `konstitucija.txt`.
The columns represent how many lines are hashed at once (1, 2, 4, 8, 16).
The rows represent repeated tests

<img width="637" height="357" alt="image" src="https://github.com/user-attachments/assets/ba04a828-cb95-4275-8dd5-62456f6e5619" />

## Collision measure
Program choice 3

File `random_strings_100k.txt` contains completely random strings (100 000 total):
- 25k strings with 10 characters
- 25k strings with 100 characters
- 25k strings with 500 characters
- 25k strings with 1000 characters

When hashed (hashes in `random_strings_hashed_100k.txt`) and compared with each other, it appears that 411 of 100 000 are not unique hashes with 419 total duplicates.

Code:
```python
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

```
## Avalanche effect
Program choice 4 & 5

Collision detection with extremely similar 100 000 strings

Files used: 
- `similar_strings_100k.txt` strings with size 16 characters
-  `similar_strings_hashes_100k.txt` hashed strings

Using same code as above we get the following results:
- Number of duplicate hashes: 4668
- Total duplicate occurrences: 4972


### Comparing how much hashes differ to each on binary and hexadecimal level:


Binary:
- Min: 0.0 (there is an identical)
- Max: 62.5
- Average: 48.47

Hexadecimal:
- Min: 0.0
- Max: 100.0
- Average: 91.2190371903719

