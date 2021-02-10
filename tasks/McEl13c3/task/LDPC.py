import numpy as np
import warnings

from random import choice
from pyldpc import coding_matrix_systematic, make_ldpc

from LinearCode import LinearCode


class LDPC(LinearCode):
	"""
	Low-Density Parity-Check code (extends LinearCode)

	...
	Methods
	-------
	from_params(n, d_v, d_c, regular=True)
		Init LDPC by size of H, column weight and row weight

	"""

	def __init__(self, G: np.ndarray, H: np.ndarray):       
		super().__init__(G, H)

	@classmethod
	def from_params(cls, n, d_v, d_c, regular=True):
		if regular:
			# Gallagher's algorithm
			H, G = make_ldpc(n, d_v, d_c, systematic=True, sparse=True)
		else:
			# MacKay's algorithm
			p = n // d_c

			vector = [1 for _ in range(d_c)] + [0 for _ in range(n - d_c)]
			vector = np.array(vector, dtype=int)

			matrix = np.array([np.random.permutation(vector) for _ in range(d_v * p)], dtype=int)
			H, G = coding_matrix_systematic(matrix)

		return cls(G.T, H)		
