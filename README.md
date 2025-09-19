
# Hash Function Logic

## Overview
This repository contains a Python script with a custom hash function that converts a text string into a 64 digit hexadecimal number through some arithmetic.

## Structure
The input is a string. Each letter of the string is converted to its byte form and is stored as bits in `array_of_bits[]`, which is then appended to another array called `array_of_bytes[]`.

## Hashing process logic 
1.  We pass an `array_of_bytes[]` into the `hash_function()`.
    
2.  The function loops through `array_of_bytes[]`, where each element is an array of bits called `array_of_bits[]`.

3. We create a temporary variable called `temporary_sum = 1` and loop through `array_of_bits[]` that consists of 8 elements that are bits.

4.  For the first 6 bits of each block, the following logic is applied to `temporary_sum`:
    
    -   If the bit is `0`, multiply `temporary_sum` by `67429` raised to the power of its position index.
        
    -   If the bit is `1`, multiply `temporary_sum` by `91997` raised to the power of its position index.
        
5. The last 2 bits of the block (`bit_duo[]`) determines by which large number we'll multiply `temporary_sum` by
    
    -   `[0, 0]` multiplies by `410079252992648349570025508981`
        
    -   `[0, 1]` multiplies by `728730155706782142465312831289`
        
    -   `[1, 1]` multiplies by `233246422214829721422450466691`
        
    -   `[1, 0]` multiplies by `820249177872665494536846925429`
        
6.  After fully processing the block, `calculated_number` is multiplied by `temporary_sum`. Then `temporary_sum` is reset to 1 for the next block.

7. When we loop through everything the function returns a large number, which then can be converted into hexadecimal form. In this case we just do:
   ```
   number = hash_function(array_of_bytes)
   hex_value = format(number, "x")
   cut_value = hex_value[:64]
   ```
   which just 'chops' the number if it has move than 64 digits.
    

**Note:** All numbers here randomly chosen large prime numbers.
 
