def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def factor(n):
    for i in range(3, n):
        if n%i == 0:
            return i

e = 2
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA
while True:
    rsa = RSA.construct((getPrime(512) * getPrime(512), 2))
    n = rsa.n
    p = factor(n)
    q = n//p
    phi_n = (p-1) * (q-1)

    # Only for python >= 3.8
    # From https://docs.python.org/3/library/functions.html#pow
    # If mod is present and exp is negative, base must be relatively prime to mod.
    # In that case, pow(inv_base, -exp, mod) is returned, where inv_base is an inverse to base modulo mod.
    # d_crack = pow(e, -1, phi_n)

    # python < 3.8
    d_crack = modinv(e, phi_n)

    print('cracked d:', d_crack) # prints "cracked d: 101"