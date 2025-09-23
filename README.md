
# Hash Function Logic

## Overview
This repository contains a Python script with a custom hash function that converts a text string into a 64 digit hexadecimal number through some arithmetic.

## Input
The input can be:  
1. A single word entered by the user.  
2. A `.txt` file with words, one per line.  

## Hashing process pseudo-code (before AI)
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
| 1       | 2.17 | 3.17 | 6.28 | 15.16 | 46.93 |
| 2       | 2.08 | 3.20 | 6.69 | 13.30| 47.05 |
| 3       | 2.09 | 3.15 | 5.93 | 13.23| 31.47 |
| 4       | 2.12 | 3.23 | 5.92 | 13.11| 30.22 |
| 5       | 2.11 | 3.19 | 5.87 | 13.15| 29.37 |
| **Average** | **2.11** | **3.19** | **6.14** | **13.59** | **37.00** |

This table shows how long it takes (in seconds) to hash different numbers of lines from the file `konstitucija.txt`.
The columns represent how many lines are hashed at once (1, 2, 4, 8, 16).
The rows represent repeated tests

<img width="637" height="357" alt="image" src="https://github.com/user-attachments/assets/ba04a828-cb95-4275-8dd5-62456f6e5619" />

## Collision measure
We used .txt file that contains completely random strings (100 000 total):
- 25k strings with 10 characters
- 25k strings with 100 characters
- 25k strings with 500 characters
- 25k strings with 1000 characters

When hashed and compared with each other, it appears that 411 of 100 000 are not unique hashes with 419 total duplicates.
| Number of Duplicate Hashes | Total Duplicate Occurrences |
|----------------------------|-----------------------------|
| 411                        | 419                         |


## Avalanche effect
Collision detection with the same length similar strings (100 000 total).

When doing collision check we get:
| Number of Duplicate Hashes | Total Duplicate Occurrences |
|----------------------------|-----------------------------|
| 2868                       | 2978                        |


### Comparing how much hashes differ to each on binary and hexadecimal level:
| Metric      | Min (%) | Max (%) | Average (%)   |
|-------------|---------|---------|---------------|
| Binary      | 0.0     | 62.5    | 49.39         |
| Hexadecimal | 0.0     | 100.0   | 92.95         |



# Comparison with AI improved version
## Efficiency measure

| Test | 1 row  | 2 rows  | 4 rows  | 8 rows  | 16 rows  |
|------|--------|---------|---------|---------|----------|
| 1    | 0.73   | 0.89    | 1.07    | 1.23    | 1.36   |
| 2    | 0.73   | 0.86    | 1.06    | 1.21    | 1.37   |
| 3    | 0.74   | 0.84    | 1.01    | 1.19    | 1.40   |
| 4    | 0.74   | 0.86    | 1.02    | 1.24    | 1.36   |
| 5    | 0.74   | 0.85    | 1.01    | 1.22    | 1.37   |
| **Average**   | 0.74    | 0.86    | 1.04    | 1.22 | 1.37 |

Average run-time compared to No-AI version is much better:
| Version | 1 row  | 2 rows  | 4 rows  | 8 rows  | 16 rows  |
|---------|--------|---------|---------|---------|----------|
| No-AI   | 2.11   | 3.19    | 6.14    | 13.59   | 37.01    |
| AI      | 0.74   | 0.86    | 1.04    | 1.22    | 1.37     |


## Collision measure
When using using 100 000 random strings we get that all the hashes are unique:

| Version     | Number of Duplicate Hashes | Total Duplicate Occurrences |
|-------------|----------------------------|-----------------------------|
| No-AI       | 411                        | 419                         |
| AI Improved | 0                          | 0                           |


When using using 100 000 random strings that are extremely similar we get:
|  Version   | Number of Duplicate Hashes | Total Duplicate Occurrences |
|------------|----------------------------|-----------------------------|
| No-AI      | 2868                       | 2978                        |
| AI Improved| 0                          | 0                           |



## Avalanche effect
When comparing how much hashes differ to each on binary and hexadecimal level, we get that results are somewhat similar compared to No-AI version

| Version | Metric      | Min (%) | Max (%) | Average (%) |
|---------|-------------|---------|---------|-------------|
| No-AI   | Binary      | 0.0     | 62.5    | 49.39       |
| AI      | Bit         | 37.10   | 64.45   | 49.96       |
| No-AI   | Hexadecimal | 0.0     | 100.0   | 92.95       |
| AI      | Hexadecimal | 78.12   | 100.0   | 93.72       |

# Comparison between SHA-256, AI version & No-AI version

## Efficiency measure
| Test | 1 row  | 2 rows  | 4 rows  | 8 rows  | 16 rows  |
|------|---------|---------|---------|---------|----------|
| 1    | 0.12  | 0.10  | 0.10  | 0.10  | 0.10   |
| 2    | 0.12  | 0.11  | 0.10  | 0.10  | 0.10   |
| 3    | 0.11  | 0.10  | 0.10  | 0.10  | 0.10   |
| 4    | 0.10  | 0.10  | 0.10  | 0.10  | 0.11   |
| 5    | 0.11  | 0.13  | 0.11  | 0.10  | 0.10   |

Averages compared:
| Version | 1 row  | 2 rows  | 4 rows  | 8 rows  | 16 rows  |
|---------|--------|---------|---------|---------|----------|
| No-AI   | 2.11   | 3.19    | 6.14    | 13.59   | 37.01    |
| AI      | 0.74   | 0.86    | 1.04    | 1.22    | 1.37     |
| SHA-256 | 0.11   | 0.11    | 0.10    | 0.10    | 0.10     |

## Collision measure
When using using 100 000 random strings:

| Version     | Number of Duplicate Hashes | Total Duplicate Occurrences |
|-------------|----------------------------|-----------------------------|
| No-AI       | 411                        | 419                         |
| AI Improved | 0                          | 0                           |
| SHA-256     | 0                          | 0                           |


## Avalanche effect
When comparing how much hashes differ to each on binary and hexadecimal level, we get that results are somewhat similar compared to No-AI version

| Version | Metric      | Min (%) | Max (%) | Average (%) |
|---------|-------------|---------|---------|-------------|
| No-AI   | Binary      | 0.0     | 62.5    | 49.39       |
| AI      | Binary      | 37.10   | 64.45   | 49.96       |
| SHA-256 | Binary      | 35.93   | 62.10   | 49.98       | 
| No-AI   | Hexadecimal | 0.0     | 100.0   | 92.95       |
| AI      | Hexadecimal | 78.12   | 100.0   | 93.72       |
| SHA-256 | Hexadecimal | 76.5    | 100.0   | 93.74       |   



