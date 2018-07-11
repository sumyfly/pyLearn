#!/bin/python
# -*-coding:utf-8-*-


mcase = {'a': 10, 'b': 30, 'c': 11, 'A': 2, 'C': 3, 'z': 2}

d_gen = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

print(d_gen)
