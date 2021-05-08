#! /usr/bin/python3

from Crypto.Hash import MD5
from Crypto.Cipher import AES
from binascii import unhexlify
import sys


KEY = open('/home/encraptor1/aeskey', 'rb').read()
IV = open('/home/encraptor1/iv', 'rb').read()


def read(prompt):
    write(prompt)
    data = sys.stdin.buffer.read()
    write('\n')

    return data


def write(prompt):
    try:
        sys.stdout.buffer.write(prompt)
    except TypeError:
        sys.stdout.buffer.write(prompt.encode('utf-8'))

    sys.stdout.flush()


def md5sum(data):
    md5 = MD5.new()
    md5.update(data)

    return md5.hexdigest()


def encrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    return unhexlify(md5sum(data)) + cipher.encrypt(data)


def banner():
    write("  ______        _____                 _               __   ___  \n")
    write(" |  ____|      / ____|               | |             /_ | / _ \\ \n")
    write(" | |__   _ __ | |     _ __ __ _ _ __ | |_ ___  _ __   | || | | |\n")
    write(" |  __| | '_ \\| |    | '__/ _` | '_ \\| __/ _ \\| '__|  | || | | |\n")
    write(" | |____| | | | |____| | | (_| | |_) | || (_) | |     | || |_| |\n")
    write(" |______|_| |_|\\_____|_|  \\__,_| .__/ \\__\\___/|_|     |_(_)___/ \n")
    write("                               | |                              \n")
    write("                               |_|                              \n")
    write("\n");

banner()

data = read('[+] Data: ')
write('[+] Encrypted:\n')
write('----------------------------- START -------------------------------\n')
write(encrypt(data, KEY, IV))
write('\n------------------------------ END --------------------------------')
