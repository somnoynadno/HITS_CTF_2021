#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

from time import sleep

def skip(sock):
	data = sock.recv(2048).decode()

	if "HITS" in data:
		print(data)
		exit(0)
	else:
		sleep(0.08)


def main():
    sock = socket.socket()

    sock.settimeout(None)
    sock.connect(('localhost', 8080))

    print("starting...")
    skip(sock); skip(sock);

    step = 6
    amount = step
    while True:
        sock.send(b"red\n")
        skip(sock)

        sock.send((str(amount) + "\n").encode('utf-8'))
        for i in range(5):
            skip(sock)

        data = sock.recv(2048).decode()
        print(data)

        if "money" in data:
            break

        if "won" in data:
            if amount > step:
                amount = step
        else:
            amount *= 2

        sleep(0.2)
        print(f"---> current amount {amount} <---")
        sock.send(b"status\n")

        sleep(0.2)
        data = sock.recv(2048).decode()
        print("MONEY: " + data)

        money = int(data.split('$')[0])
        if amount > money:
            break

        if amount == step:
            step = int(money / 16)
            amount = step

        sleep(0.5)

    print("[not this time]")
    sock.close()


if __name__ == "__main__":
    main()