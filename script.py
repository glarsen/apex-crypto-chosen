#!/usr/bin/env python

import os
import sys

import raven

rclient = None

KEYSPACE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def set_trace():
    env = os.environ.get('APEX_ENV', "development")
    global rclient
    rclient = raven.Client(
        site='hack.utulsa.cc',
        environment=env
    )

def load_key():
    key = None
    try:
        with open('/run/secrets/key') as f:
            key = f.read()
    except FileNotFoundError:
        key = os.environ.get('KEY')

    return key

def service(key):
    cipher = str.maketrans(KEYSPACE, key) 

    try:
        plaintext = input()
    except EOFError:
        rclient.captureException(
            message="Possible port scan attempt",
            level='warning'
        )
        print("[!] FATAL: Unexpected input. Aborting.",
              file=sys.stderr)
        print("Come at me brah!")
        sys.exit(1)

    print(plaintext.translate(cipher))

if __name__ == "__main__":
    set_trace()
    key = load_key()
    if not key:
        rclient.capture('raven.events.Message',
            message="Initialization Error -- failed to load cipher key",
            level='fatal'
        )
        print("[!] FATAL: No cipher key present.",
              file=sys.stderr)
        print("SERVICE ERROR: Challenge misconfigured -- "\
              "Contact admin@utulsa.cc")
        sys.exit(1)
    service(key)

