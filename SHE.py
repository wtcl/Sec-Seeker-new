# SHE Scheme
import math
from random import randint, uniform

import pandas as pd
from Crypto.Util.number import getPrime
import time


def generate_key():
    k0, k1, k2 = 1024, 40, 100
    p = getPrime(k0)
    q = getPrime(k0)
    length = randint(2 ** (k2 - 1) + 1, 2 ** k2 - 1)
    n = p * q
    return k0, k1, k2, n, length, p, q


def encrypt(p, length, k0, k2, n, m):
    r = randint(2 ** (k2 - 1) + 1, 2 ** k2 - 1)
    rr = randint(2 ** (k0 - 1) + 1, 2 ** k0 - 1)
    c = ((r * length + m) % n) * ((1 + rr * p) % n)
    return c % n


def pub_encrypt(p, length, k0, k2, n, m, r1, r2):
    e01 = encrypt(p, length, k0, k2, n, 0)
    e02 = encrypt(p, length, k0, k2, n, 0)
    c = m + r1*e01 + r2*e02
    return c % n


def decrypt(p, length, c):
    m = (c % p) % length
    if m > (length >> 1):
        m = m - length
    return m


if __name__ == "__main__":
    k0, k1, k2, n, length, p, q = generate_key()
    print("--------------系统初始化-------------")
    print("k0: %d\nk1: %d\nk2: %d\nn: %d\nlength: %d\np: %d\nq: %d\n"
          "-------------参数设置完成-------------"
          % (k0, k1, k2, n, length, p, q))
    data=pd.read_csv("testdata.csv")
    data=list(data["num"])
    c = []
    print("加密")
    st = time.time()
    for i in range(1000000):
        if i == 1000-1:
            print(1000, time.time()-st)
        elif i == 10000-1:
            print(10000, time.time() - st)
        elif i == 100000:
            print(100000, time.time() - st)
        elif i == 1000000-1:
            print(1000000, time.time() - st)
        c.append(encrypt(p, length, k0, k2, n, data[i]))
    print("解密")
    st = time.time()
    for i in range(1000000):
        if i == 1000 - 1:
            print(1000, time.time() - st)
        elif i == 10000 - 1:
            print(10000, time.time() - st)
        elif i == 100000:
            print(100000, time.time() - st)
        elif i == 1000000 - 1:
            print(1000000, time.time() - st)
        d = decrypt(p, length, c[i])
