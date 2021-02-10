import pickle
import uuid


class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password


def make_pickle(username, password):
	user = User(username, password)
	pd = pickle.dumps(user)

	u = str(uuid.uuid4()) + ".pickle"

	with open("tmp/" + u, "wb") as file:
		file.write(pd)

	return u


def load_user(pickle_data):
	user = pickle.loads(pickle_data)

	return user
