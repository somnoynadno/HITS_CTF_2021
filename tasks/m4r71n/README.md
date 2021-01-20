# M4r71n

## Legend

### RU

Ваше время доказать казино, что у них карты разложены не в том порядке.

### EN

It's your time to prove to the casino that their cards are laid out in the wrong order.

## Description

Simple fair roulette for fun and profit.

Roulette has no vulnerability, and can be 
won even without programming. 

## Solution

Roulette can be won by any of the 
following strategies or a combination of them:

1. By going all-in on red/black 4 times in a row. 
The best strategy. Winning chance: 6.25%.

2. By placing bet on one number, winning it 
and going all-in on color. Winning chance: 1.4%.

3. [Martingale](https://en.wikipedia.org/wiki/Martingale_(betting_system)) strategy. Almost safest (but longest) strategy.
If dynamic step chosen, player can only lose by having long chain
of bet losses (4 or more). 

Example exploit: ```margingale_bot.py```.

## Flag

**HITS{g0r0h0v03_mud1l0}**

## Handout

```task/main.go```
