#!/usr/bin/env python
# -*- coding: utf8
import sys


def algorithm(a0, a1):
    def getNum(q, m):
        if q < 0:
            return (m + q) % m
        else:
            return q
    
    print u'ax+by=gcd(a,b)\nSolve by algorithm:\n' \
          u'a^-1 mod b => %s^-1 mod %s' % (a0, a1)
    a = a0
    b = a1

    q = 0
    a2 = 0  # а текущего шага
    i = 1
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    result = "Extended Euclid Algorithm\ni\tq\ta0\ta1\tx0\tx1\ty0\ty1";
    while a1:
        q = a0 / a1;

        a2 = a0 - q * a1
        a0 = a1
        a1 = a2

        x = x2 - q * x1
        x2 = x1
        x1 = x

        y = y2 - q * y1
        y2 = y1
        y1 = y

        result += "\n%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (i, q, a0, a1, x2, x1, y2, y1)
        # result += "\n" + str(i) + "\t" + str(q) + "\t" + str(a0) + "\t" + str(a1) + "\t" + x2 + "\t" + x1 + "\t" + y2 + "\t" + y1
        i += 1
    print result
    
    print '\nMultiplicative inverse:'
    if a0 == 1:
        print 'gcd(a, b) = 1 => Result: %s^-1 mod %s = %s' % (a, b, getNum(x2, b))
    else:
        print 'gcd(a, b) != 0 => multiplicative inverse not calculated' 


def main():
    print u'Extended Euclid Algorithm\n'
    if len(sys.argv) >= 3:
        algorithm(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print u'[ERROR] Not enough arguments.\n' \
              u'Example: 5^-1 mod 62\n' \
              u'python esm.py 5 62\n'


if __name__ == '__main__':
    main()
