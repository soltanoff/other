#!/usr/bin/env python
# -*- coding: utf8
import sys


def algorithm(a, d, m):
    print u'Solve on the forehead: %s^%s mod %s = %s' % (a, d, m, a**d % m)
    print u'Solve by algorithm:\n\n' \
          u'a^d mod m => %s^%s mod %s' % (a, d, m)

    binary_d = str(bin(d))[2:]
    print u'1) d = %s (list of binary numbers)' % binary_d

    b = a**(int(binary_d[-1]))
    A = a
    print u'2) b = a^d[%s] = %s; A = a = %s' % (len(binary_d)-1, b, A)

    print u'3) Cycle: A = A^2 mod m; b = b * A^d[i];\n'
    for x in range(len(binary_d[:-1]))[::-1]:
        oldA = A
        oldB = b
        A = A**2 % m
        b = (b * A**(int(binary_d[x]))) % m

        print u'\td[%s] = %s' % (x, binary_d[x])
        print u'\tA = %s^2 mod %s = %s' % (oldA, m, A)
        print u'\tb = %s * %s^%s mod %s = %s\n' % (oldB, A, binary_d[x], m, b)

    print u'4) Result: %s^%s mod %s = %s' % (a, d, m, b)


def main():
    print u'Algorithms for fast modular exponentiation\n'
    if len(sys.argv) >= 4:
        algorithm(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        print u'[ERROR] Not enough arguments.\n' \
              u'Example: 5^70 mod 62\n' \
              u'python esm.py 5 70 62\n'


if __name__ == '__main__':
    main()
