from binascii import unhexlify
from Crypto.Util.number import bytes_to_long, long_to_bytes
with open('flag.txt.encrypted welp.encrypted', 'rb') as f:
    data = f.read()
c = input('c: ')  # Cipher message (int)
c = bytes_to_long(data)
print(c)
p = input('p: leave empty if dont have')  # Prime factor 1
q = input('q: leave empty if dont have')  # Prime factor 2
d = input('d: ')  # Private Key
n = input('n: leave empty if dont have')  # Public Key
n = 139303184393910343616388465024729041891194370968355821658633930074291687645970474150176305115860217573060798552886504134117064673553937346718393596111932314544406857091438701763190299564767036583256984292944743619704748532647422538215488790321932776224130907529180684741196884758792545514555598233850858125893

'''MIGdMA0GCSqGSIb3DQEBAQUAA4GLADCBhwKBgQCGQukWKB6AosruYhSIL0MnU/Xq
1FIh/CL3wcILt2JA0/twQ5Wc3Z9iJESyXqrip0js/5b8wlIOB1sOYVRCiZa27sot
HVZ3kxBwNAdSBWXL0cAwXMrUN/ng7LLJ3YpYuUd2B+w9j7spEpTYPYYlhx2YPzjQ
cTRPhomxgcXib23HaQIBAg=='''

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
