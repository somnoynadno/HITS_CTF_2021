# c451n0

## Legend

### br0k3n

Вот пока ты это делал, так все и происходило!

### unf41r

Ты распечатала колоду на моих глазах! 

Как они могут быть там разложены в другом порядке?! 

### b4ckd00r3d

Вы чё, в киосках их заряжаете?!..

## Description

Simple roulette with different vulnerabilities for fun and profit.

## Solutions

### br0k3n

Just pass negative number to this roulette lul.

### unf41r

In this variation 'zero' is unavailable
and because of line 44 it's much better to 
put bets on black (sector 36 is unavailable too).

Roulette can be won by any of the 
following strategies or a combination of them:

1. By going all-in on red/black 4 times in a row. 
The best strategy. Winning chance: 6.25%.

2. By placing bet on one number, winning it 
and going all-in on color. Winning chance: 1.4%.

3. [Martingale](https://en.wikipedia.org/wiki/Martingale_(betting_system)) strategy. 
Almost safest (but longest) strategy.
If dynamic step chosen, player can only lose by having long chain
of bet losses (4 or more). 

Example solution: ```margingale_bot.py```.

### b4ckd00r3d

The random numbers are definitely guessable.

Seed for each sesson is a unix timestamp in seconds.
So, at first we need to guess that exact timestamp and then 
generate the same (pseudo)random sequence using rand() function from ```main.go```.

Sorry, I have no exploit for that, but it must be pretty simple to implement.

## Flags

**HITS{7uz_n3_n4_m35t3}**

**HITS{g0r0h0v03_mud1l0}**

**HITS{1_cr4ck_y0u_bullsh1t_sh1t}**

## Handout

File ```main.go``` in all of three folders.
