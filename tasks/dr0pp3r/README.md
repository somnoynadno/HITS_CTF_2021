# dr0pp3r

## Legend

### RU

Таск посвящается всем тем, кто любит запускать подозрительные файлы на своей рабочей машине.

### EN 

The task is dedicated to all those who are not afraid to run suspicious files on their working machine.

## Description

Simple reverse task.

## Solution

.pyc file can be easily uncompiled with uncompile6 util. After that you can view source code of this script.

The only function of the dropper is to download and run the file from a remote server.

The downloaded file performs the usual XOR operation between the flag and the random gamma, thereby encrypting it, and displays the flag on the screen.

You just need to track between which bytes XOR occurs, or just get the flag from the memory of the new process being started.

## Flag

**HITS{un7r4c34bl3_3x3cu710n}**

## Handout

```task/dropper.pyc```
