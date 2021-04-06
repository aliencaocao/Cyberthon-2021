from binascii import unhexlify

c = input('c: ')
p = input('p: leave empty if dont have')
q = input('q: leave empty if dont have')
d = input('d: ')
n = input('n: leave empty if dont have')
if p == '' and q == '':
    if n == '':
        print('n is required if either p or q is unknown!')
elif n == '':
    if p == '' and q == '':
        print('p and q are required if either p or q is unknown!')
    else:
        n = int(p) * int(q)
m = pow(int(c), int(d), n)
print(unhexlify(hex(m)[2:]).decode())
