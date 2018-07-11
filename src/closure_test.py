#!/bin/python
# -*-coding:utf-8-*-


def make_printer(msg1, msg2):
    def printer():
        print(msg1, msg2)
    return printer


printer = make_printer('foo', 'bar')
printer()
import pdb
pdb.set_trace()

printer.__closure__
