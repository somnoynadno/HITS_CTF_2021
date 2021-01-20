# w1k1

## Legend

### RU

Реальный проект нашего четверокурсника.

*Флаг лежит в директории исполняемого приложения.*

### EN 

The real project of our fourth-year student.

*Flat is in the application directory.*

## Description

Small web-service with insecure OS command execution.

## Solution

Articles are taken from [wikit](https://www.npmjs.com/package/wikit) util,
which is called from OS ```exec``` function.

No input sanitization allows to execute any arbitrary shell command on the server 
with the running application privileges by simply appending malicious payload 
to the end of the harmless article name. 

For instance:

- query ```?search=TSU%20&&%20ls``` will display folder content. 

- query ```?search=TSU%20&&cat%20flag.txt``` will show you the flag.

## Flag

**HITS{my_f4v0r173_4r71cl3_15_5h3ll}**

## Handout

*Nothing*
