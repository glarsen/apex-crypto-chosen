#!/usr/bin/env python

import os
import random

KEYSPACE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gen_key(choices):
    return ''.join(random.sample(choices, len(choices)))

def group(text, n):
    return ''.join(group + " " for group in [text.replace(" ", "")[i:i+n] for i in range(0, len(text), n)]).rstrip(" ")

def encrypt(cipher, group_size, input_file, output_file):
    with open(input_file, 'r') as f:
        plaintext = f.read()
    
    encrypted = group(plaintext.translate(cipher), group_size)
    with open(output_file, 'w') as f:
        f.write(encrypted)


if __name__ == "__main__":
    if not os.path.isfile("key.txt"):
        key = gen_key(KEYSPACE)
        print("[*] Generating key: {0}".format(key))
        with open("key.txt", 'w') as f:
            f.write(key)
    else:
        with open("key.txt") as f:
            key = f.read()
        print("[*] Loaded existing key: {0}".format(key))
    
    cipher = str.maketrans(KEYSPACE, key)

    print("[*] Encrypting flag...")
    encrypt(cipher, 5, "flag.txt", "flag.enc")

