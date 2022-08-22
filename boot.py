import sys

import hello
import senko

ota = senko.Senko(user='bktero', repo="HelloWorld", files=['boot.py', 'hello.py'])

if ota.update():
    sys.exit(42)
else:
    hello.hello('world')