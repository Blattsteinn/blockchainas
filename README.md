
# Hash Function Logic

## Overview
This repository contains a Python script with a custom hash function that converts a text string into a 64 digit hexadecimal number through some arithmetic.

## Input
The input can be:  
1. A single word entered by the user.  
2. A `.txt` file with words, one per line.  

## Hashing process logic 
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
