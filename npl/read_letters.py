import os
import sys


def read_letter(name):
    f = open('../' + name, "r")
    print(f.read_letter())
