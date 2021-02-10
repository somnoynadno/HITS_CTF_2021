# McEl13c3

## Legend

### RU

Когда вы перейдёте на сторону пост-квантовой криптографии, пути назад уже не будет...

Дешифруйте: 

[1 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 0 1 1 1 1 0 1 0 1 0
 1 1 1 1 1 1 0 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 0 1 1 1 0 0 0 0 0 1 0 0
 1 0 0 0 1 0 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 0 1 1 0 1 1 0 0 0
 1 0 1 1 0 0 1 1 0 1 1 1 1 0 1 1 1 1 0 0 1 0 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1
 0 0]

Полученную битовую строку оберните в HITS{} (например, HITS{00101001101}).

### EN 

When you switch to the side of post-quantum cryptography, there will be no turning back...

Decrypt it:

[1 1 1 1 1 0 1 0 0 0 1 1 1 0 1 1 1 0 0 0 0 0 0 1 0 1 0 0 1 1 1 1 0 1 0 1 0
 1 1 1 1 1 1 0 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 0 1 1 1 0 0 0 0 0 1 0 0
 1 0 0 0 1 0 0 1 0 0 1 0 1 1 0 1 0 1 0 1 1 1 1 1 1 1 1 1 0 1 1 0 1 1 0 0 0
 1 0 1 1 0 0 1 1 0 1 1 1 1 0 1 1 1 1 0 0 1 0 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1
 0 0]

Wrap the resulting bit string in HITS{} (for example, HITS{00101001101}).

## Description

Implementation of McEliece cryptosystem.

## Solution

The most difficult part of the task is to run this Python code.

When you can do this, you just need to call the decrypt() method on the cryptosystem with initialized parameters, passing the ciphertext to it.

The resulting word must be represented as a bit string and wrapped in HITS{}, which can also be done using Python.

## Flag

**HITS{01001101101000111111001101111101000001011010101100010111101100101}**

## Handout

All in ```task``` folder.
