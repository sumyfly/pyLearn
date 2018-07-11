#!/bin/python
# -*-coding:utf-8-*-


def consumer():
    r = 'init'
    print("started")
    while True:
        print("start step1")
        # looks like yiled has tow steps: 
        # 1. yield r 2. received new sedt value
        n = yield r 
        print('start setp2')
        if not n:
            print('not n>>>', n)
            yield
            return
        print('consumer receive %s' % n)
        print('here %s' % n)
        r = '200 ok: %s' % n


def produce(c):
    first_r = c.send(None)
    print(first_r)
    n = 0
    while n < 5:
        print('-------')
        n = n + 1
        print('produce send %s' % n)
        r = c.send(n)
        print('consumer return: %s' % n)
        print('r %s' % r)
    c.send(None)
    # c.close()


c = consumer()
produce(c)
