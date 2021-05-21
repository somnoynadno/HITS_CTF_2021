# McEl13c3

## Legend

### RU

Когда вы перейдёте на сторону пост-квантовой криптографии, пути назад уже не будет...

Дешифруйте: 

[1 1 0 0 1 1 1 0 1 0 0 1 0 0 1 0 1 0 1 0 1 1 0 1 0 0 0 1 0 1 0 0 0 0 0 1 1
 0 1 0 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 0 0 0 1 1 0 0 1 1 1 1 0 0 1 1 0 1 0 0
 1 1 0 1 0 0 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 1 1 1 1 1 1 1 0 1 0 0 1 0 0
 0 1 1 1 1 0 0 0 1 0 0 0 1 1 0 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 1 1 0 0 1 1
 0 0]

Параметры G и H: https://pastebin.com/jpa4TgqG

Полученную битовую строку оберните в HITS{} (например, HITS{00101001101}).

### EN 

When you switch to the side of post-quantum cryptography, there will be no turning back...

Decrypt it:

[1 1 0 0 1 1 1 0 1 0 0 1 0 0 1 0 1 0 1 0 1 1 0 1 0 0 0 1 0 1 0 0 0 0 0 1 1
 0 1 0 1 1 0 0 1 0 0 1 0 1 0 0 1 1 0 0 0 0 1 1 0 0 1 1 1 1 0 0 1 1 0 1 0 0
 1 1 0 1 0 0 1 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 1 1 1 1 1 1 1 0 1 0 0 1 0 0
 0 1 1 1 1 0 0 0 1 0 0 0 1 1 0 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 1 1 0 0 1 1
 0 0]

G and H parameters: https://pastebin.com/jpa4TgqG

Wrap the resulting bit string in HITS{} (for example, HITS{00101001101}).

## Description

Implementation of McEliece cryptosystem.

## Solution

The most difficult part of the task is to run this Python code.

When you can do this, you just need to call the decrypt() method on the cryptosystem with initialized parameters, passing the ciphertext to it.

The resulting word must be represented as a bit string and wrapped in HITS{}, which can also be done using Python.

## Flag

**HITS{10101011101101110101101010101101010101001011000010111011010011001}**

## Handout

All in ```task``` folder.
