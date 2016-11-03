# Extended Euclid Algorithm (EEA)

Extended Euclid Algorithm aka EEA
____

In arithmetic and computer programming, the extended Euclidean algorithm is an extension to the 
Euclidean algorithm, which computes, besides the greatest common divisor of integers a and b, 
the coefficients of Bézout's identity, that is integers x and y such that ax+by=gcd(a,b).

Extended Euclidean algorithm also refers to a very similar algorithm for computing the polynomial 
greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials.

The extended Euclidean algorithm is particularly useful when a and b are coprime, since x is the 
modular multiplicative inverse of a modulo b, and y is the modular multiplicative inverse of b modulo a. 
Similarly, the polynomial extended Euclidean algorithm allows one to compute the multiplicative inverse 
in algebraic field extensions and, in particular in finite fields of non prime order. It follows that 
both extended Euclidean algorithms are widely used in cryptography. In particular, the computation of 
the modular multiplicative inverse is an essential step in RSA public-key encryption method.


How to enter values:

For example, you need to calculate 5^-1 mod 62, then

python eea.py 5 62


Python: Python 2.7.*

# Example
Extended Euclid Algorithm

ax+by=gcd(a,b)
Solve by algorithm:
a^-1 mod b => 5^-1 mod 62
Extended Euclid Algorithm 
i       q       a0      a1      x0      x1      y0      y1                                                              
1       0       62      5       0       1       1       0                                                               
2       12      5       2       1       -12     0       1                                                               
3       2       2       1       -12     25      1       -2                                                              
4       2       1       0       25      -62     -2      5                                                                               

Multiplicative inverse:                                                                                                 
gcd(a, b) = 1 => Result: 5^-1 mod 62 = 25 
