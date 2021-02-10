# R54

## Legend

### RU

Мы перехватили пару сообщений. Мы знаем, что там зашифрована одна и та же секретная фраза одним и тем же приватным ключом, но всё равно не можем расшифровать её. 

Сможете нам помочь?

### EN 

We intercepted a couple of messages. We know that the same secret phrase is encrypted there with the same private key, but we still can't decrypt it. 

Can you help us?

## Description

Slightly wrong RSA protocol usage.

## Solution

All messages are encrypted with one private key. 

Just because number of messages is equal to public exponent and this number is very small, we can perform Hastad's Attack on RSA protocol.

Implementation: ```solver.py```

## Flag

**HITS{l0r3m_1psum_d0l0r_51t_4m3t_c0n53ct3tur_4d1p15c1ng_3l1t}**

## Handout

```task/task.txt```
