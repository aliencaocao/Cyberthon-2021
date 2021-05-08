from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

rsa = RSA.construct((getPrime(512) * getPrime(512), 2))
# print(rsa.d) # AttributeError: No private exponent available for public keys
print(rsa.e)
print(rsa.n)
# print(rsa.p)  # No CRT component 'p' available for public keys
# print(rsa.q)  # AttributeError: No CRT component 'q' available for public keys
# print(rsa.u)  # AttributeError: No CRT component 'u' available for public keys
with open('flag.txt', 'rb') as f:
    data = f.read()

plaintext = bytes_to_long(data)
ciphertext = pow(plaintext, rsa.e, rsa.n)

# with open('./dist/flag.txt.encrypted', 'wb') as f:
#     f.write(long_to_bytes(ciphertext))
#
# with open('./dist/pubkey.pem', 'wb') as f:
#     f.write(rsa.export_key('PEM'))
