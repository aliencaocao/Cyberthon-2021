from base64 import b85encode, b85decode
from random import shuffle

from Crypto.Util.number import GCD
from Crypto.Random.random import randint

BASE = 85
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~'


def preprocess(data):
    return [DIGITS.index(x) for x in b85encode(data).decode()]


def postprocess(data):
    return bytes(data)


def generate_alpha():
    candidates = list(range(BASE))
    shuffle(candidates)
    for candidate in candidates:
        if GCD(candidate, BASE):
            return candidate


def generate_beta():
    return randint(0, BASE-1)


def encrypt_element(data, alpha, beta):
    return ((data * alpha) + beta) % BASE


def encrypt(data, alpha, beta):
    return [encrypt_element(x, alpha, beta) for x in data]

ALPHA = generate_alpha()
BETA = generate_beta()

data = preprocess(open('../flag.jpg', 'rb').read())

result = postprocess(encrypt(data, ALPHA, BETA))
open('flag.jpg.encrypted', 'wb').write(result)
