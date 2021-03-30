# g1t

## Legend

### RUS

Это было лишь первое моё тестовое задание задание в крупную IT-компанию, но уже через пару минут после сабмита их отдел безопасности начал кричать, что мой репозиторий скомпрометирован. 

Конечно же, после такого инцидента меня никуда не взяли.

Ну что я сделал не так?

### EN

This was just my first test task, a task for a large IT company, but after a couple of minutes, their security department started shouting that my repository was compromised.

Of course, after such an incident, I was not taken anywhere.

What did it go wrong?

## Description

The file with the environment variables was accidentally committed, and then deleted from the repository.

## Solution

Git remembers everyting:

1. ``` $ git log```

2. ``` $ git reset --hard 9b2c08cc636e9f4b8fd69cd6512fb37ab7daa6ca```

3. ``` $ ls```

4. ``` $ cat .env```

## Flags

**HITS{h0w_4b0ut_g1t1gn0r3_dud3}**

## Handout

``` task/project.zip```
