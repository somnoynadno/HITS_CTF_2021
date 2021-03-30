# 4dm1n

## Legend

### RU

Наша компания "Agrometeomonitor", производящая устройства для интернета вещей, не беспокоилась о вопросах внутренней безопасности до тех пор, пока какой-то сотрудник не сбрутил пароль администратора и не поменял секретные ключи у пары наших устройств.

Помогите нам разобраться, какие ключи он выставил.

### EN 

Our company "Agrometeomonitor", which produces IoT-devices, did not worry about internal security issues until some employee bruteforced the administrator password and changed the secret keys of a couple of our devices.

Help us figure out what keys he set up.

## Description

Long-long log file with with an admin password bruteforce.

## Solution

There can be multiple solutions:

1. Grep by keyword 'key'.

2. Guess that it is REST API and grep by 'POST' method.

3. Grep by 'backend' service and investigate suspicious traffic.

NOTE: secret key need to be decoded from base64.

## Flag

**HITS{pyth0n_r3qu35t5_g035_brrrrrrrrrrrrrrrr}**

## Handout

```task/logs.txt.zip```
