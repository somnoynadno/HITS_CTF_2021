# H175

## Legend

### Idorable Service

#### RUS

Админ это кто (who?)

#### EN

Admin is who (кто?)

### ```5**1```

#### RUS

Эксплуатация простая как 2×2

*Флаг записан в app.config["SECRET_KEY"]*

#### EN

Exploitation is as simple as 2×2

*Flag is written in app.config["SECRET_KEY"]*

## Description

Damn vulnerable Python 2 project.

Simple service to store CTF task ideas.

## Solutions

1. IDOR allows to read admin profile at <URL>/user/1 (flag is in surname).

2. SSTI in "create private comment form" allows to escape sandbox and 
write arbitary code on the server side. But we only need to read one of
runtime variables, which is much more easy.

## Flags

**HITS{j1nj4_b3z_cr1nj4}**

**HITS{4r3_y0u_w1nn1ng_50n}}**

## Handout

*Nothing*
