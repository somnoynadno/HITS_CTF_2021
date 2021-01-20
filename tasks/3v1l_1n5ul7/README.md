# 3v1l 1n5ul7

## Legend

### Escape it!

#### RU

Эти рамки всегда ущемляли меня...

#### EN

This limits has always hurt me...

### Deja Vu

#### RU

Наш разработчик ускорил работу сервиса в 10 раз!

Но какой ценой?..

#### EN

Our developer has accelerated the service by 10 times!

But at what cost?..

## Description

Service to sending evil insults.

## Solution

Task consist of two vulnerabilities:

1. Path traversal on line 71. ID came without any sanitization.
Payload like ../secret/flag.txt allows going to parent directory
and read file with known name. 
Exploit: ```path_traversal_exploit.py```.

2. Race condition on line 39. Asynchronous code execution 
allows you to read the file before the server response is 
written there. And before the request to the server, 
secret information that needs to be obtained is recorded 
in this file. Attacker just need to send read request as fast
as possible. Exploit: ```race_condition_exploit.py```.

## Flags

**HITS{71m3_70_7r4v3l}**

**HITS{f457_45_l1gh7n1ng}**

## Handout

```task/main.go```
