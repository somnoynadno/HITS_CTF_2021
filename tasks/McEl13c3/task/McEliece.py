import numpy as np

from random import randint
from math import factorial, log


def gaussjordan(X, change=0):
    """
    Compute the binary row reduced echelon form of X.

    Originally taken from https://github.com/hichamjanati/pyldpc

    Parameters
    ----------
    X: array (m, n)
    change : boolean (default, False). If True returns the inverse transform

    Returns
    -------
    if `change` == 'True':
        A: array (m, n). row reduced form of X.
        P: tranformations applied to the identity
    else:
        A: array (m, n). row reduced form of X.

    """

    A = np.copy(X)
    m, n = A.shape

    if change:
        P = np.identity(m).astype(int)

    pivot_old = -1

    # for each column
    for j in range(n):
        # take column
        filtre_down = A[pivot_old+1:m, j]
        # find first 1 index in that column
        pivot = np.argmax(filtre_down)+pivot_old+1

        # if it is really 1 on that index
        if A[pivot, j]:
            pivot_old += 1
            # if it is not previous index
            if pivot_old != pivot:
                # swap rows
                aux = np.copy(A[pivot, :])
                A[pivot, :] = A[pivot_old, :]
                A[pivot_old, :] = aux
                if change:
                    aux = np.copy(P[pivot, :])
                    P[pivot, :] = P[pivot_old, :]
                    P[pivot_old, :] = aux

            # for each row
            for i in range(m):
                # if found 1 in intersection
                if i != pivot_old and A[i, j]:
                    if change:
                        P[i, :] = abs(P[i, :]-P[pivot_old, :])
                    # put binary diff in a row
                    A[i, :] = abs(A[i, :]-A[pivot_old, :])

        if pivot_old == m-1:
            break

    if change:
        return A, P
    return A



class McEliece:
    """
    McEliece cryptosystem representation

    For more info: https://en.wikipedia.org/wiki/McEliece_cryptosystem

    ...

    Attributes
    ----------
    S : numpy.ndarrray
        random matrix (k, k)
    P : numpy.ndarrray
        random permutation matrix (n, n)
    t : int
        maximum code error
    code : LinearCode
        linear code using in decryption
    public_key : tuple
        (SGP, t)
    private key : tuple
        (S, G, P)

    Methods
    -------
    from_linear_code(code, t)
        Init cryptosystem with LinearCode with max error t

    encrypt(word)
        Encryption with public key

    decrypt(codeword)
        Decryption with private key

    _get_non_singular_matrix(k)
        Little helper to get inversable matrix (size k)
        
    """

    def __init__(self, code, S, P, t):
        self.S = S
        self.P = P
        self.t = t

        self.code = code

        # sizes
        self.k, self.n = code.getG().shape
                
        # McEliece keys
        self.public_key = ((self.S @ code.getG() @ self.P % 2), self.t)
        self.private_key = (self.S, code.getG(), self.P)
                    
    @classmethod 
    def from_linear_code(cls, code: LinearCode, t: int):
        k, n = code.getG().shape
        
        # permutation matrix (n * n)
        P = np.eye(n, dtype=int) 
        np.random.shuffle(P) 
        
        # random matrix (k * k)
        S = McEliece._get_non_singular_random_matrix(k)
        
        return cls(code, S, P, t)
        
    def encrypt(self, word):
        errors_num = self.t
        
        # error vector size n with t errors
        z = [1 for _ in range(errors_num)] + [0 for _  in range(self.n - errors_num)]
        z = np.array(z, dtype=int)
        np.random.shuffle(z)

        res = ((word @ self.public_key[0] % 2) + z) % 2
            
        return res
    
    def decrypt(self, codeword):
        A, invP = gaussjordan(self.P, True)

        c = codeword @ invP % 2
        c = np.array(c, dtype=int)
        
        d = self.code.decode(c)
        m = self.code.get_message(d)

        _, invS = gaussjordan(self.S, True)
        
        res = m @ invS % 2
        res = np.array(res, dtype=int)
        
        return res

    
    @staticmethod
    def _get_non_singular_random_matrix(k):
        while True:
            S = np.random.randint(0, 2, (k, k)) 

            A = gaussjordan(S)
            A = np.array(A, dtype=int)

            if (A == np.eye(k, dtype=int)).all():
                return S


if __name__ == "__main__":
    from LDPC import LDPC

    n = 150
    d_v = 6
    d_c = 10

    ldpc = LDPC.from_params(n, d_v, d_c)
    word = "REMOVED"

    crypto = McEliece.from_linear_code(ldpc, 5)

    encrypted = crypto.encrypt(word)
    print(encrypted)
