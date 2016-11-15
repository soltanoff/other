#!/usr/bin/env python
# -*- coding: utf8 -*-

ALPH = u"абвгдежзийклмнопрстуфхцчшщъыьэюя+-,.!?:'vin()0123456789"
MODULE = 55
KEYS = [29, 26, 1]
P = [3, 4, 1, 2]


def s(x, key):
    print '\n\t\tS: (%s * %s) mod %s = %s' % (key, x, MODULE, (key * x) % MODULE)
    return (key * x) % MODULE


def p(x):
    newX = []
    for i in range(len(x)):
        newX.append(
            x[
                P[i]-1
            ]
        )
    print '\n\t\tP: IN: %s | OUT: %s' % (x, newX)
    return newX


def f(x, key):
    newX = []
    for i in x:
        newX.append(s(i, key))

    return p(newX)


def summByModule(fList, sList):
    result = []
    for i in range(len(fList)):
        result.append((fList[i] + sList[i]) % MODULE)
    return result


def divByModule(fList, sList):
    result = []
    for i in range(len(fList)):
        print '\n\tMOD: (%s - %s) mod %s = %s' % (fList[i], sList[i], MODULE, (fList[i] - sList[i]) % MODULE)
        result.append((fList[i] - sList[i]) % MODULE)
    return result


def decrypt(L, R, key):
    newL = R
    newR = L
    print 'E: key = %s \n\tINPUT:  %s %s' % (
        key,
        L, R
    )
    print '\n\tExec f():'
    tempR = f(newR, key)
    newL = divByModule(newL, tempR)
    print '\n\tOUTPUT: %s %s\n' % (
        newL, newR
    )
    return newL, newR


def encrypt(L, R, key):
    newL = L
    newR = R
    print 'E: key = %s \n\tINPUT:  %s %s' % (
        key,
        L, R
    )
    print '\n\tExec f():'
    tempR = f(newR, key)
    newL = summByModule(newL, tempR)
    print '\n\tOUTPUT: %s %s\n' % (
        newL, newR
    )
    return newR, newL


def feistel(side, decr=False):
    L, R = side[:4], side[4:]

    for x in KEYS[::-1] if decr else KEYS:
        if decr:
            L, R = decrypt(L, R, x)
        else:
            L, R = encrypt(L, R, x)

    return L, R


def main():
    q = u"ц:кvя72(+,й0жвб3"

    left = [ALPH.index(x) for x in q[:8]]
    right = [ALPH.index(x) for x in q[8:]]

    print 'LEFT SIDE: %s' % left
    a, b = feistel(left, True)
    print 'RIGHT SIDE: %s' % left
    c, d = feistel(right, True)

    qresult = ''.join([ALPH[x] for x in a+b+c+d])
    print u'\nRESULT: %s' % qresult


if __name__ == '__main__':
    main()
