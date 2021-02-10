import numpy as np


class LinearCode:
	"""
	LiearCode base class

	...

	Attributes
	----------
	G : numpy.ndarray
	    generator matrix
	H : numpy.ndarray
		parity-check matrix

	Methods
	-------
	encode(word)
	    Encode given word by coding matrix

	decode(codeword)
		Decode codeword with bit-flipping algorithm

	get_message(decoded)
		Extract message from decoded word (removing check bits)

	syndrome(codeword)
		Find syndrome for given codeword
		
	"""

	def __init__(self, G, H):
		self.G = G
		self.H = H

		# check that H is corresponding to G
		assert (self.G @ self.H.T % 2 == 0).all()

	def encode(self, word):
		return (word @ self.G) % 2

	def decode(self, codeword):
		return bit_flipping(self.H, codeword)

	def get_message(self, decoded):
		return decoded[:self.G.shape[0]] 

	def syndrome(self, codeword):
		return (codeword @ self.H.T) % 2 

	def getG(self):
		return self.G

	def getH(self):
		return self.H
