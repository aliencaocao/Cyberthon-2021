from binascii import unhexlify


c = input('c: ')  # Cipher message (int)
p = input('p: leave empty if dont have')  # Prime factor 1
q = input('q: leave empty if dont have')  # Prime factor 2
d = input('d: ')  # Private Key
n = input('n: leave empty if dont have')  # Public Key
if p == '' and q == '':
    if n == '':
        print('n is required if either p or q is unknown!')
elif n == '':
    if p == '' and q == '':
        print('p and q are required if either p or q is unknown!')
    else:
        n = int(p) * int(q)
m = pow(int(c), int(d), int(n))
print(unhexlify(hex(m)[2:]).decode())
