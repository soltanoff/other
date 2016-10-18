# Algorithms for fast modular exponentiation (Exponentiation by squaring modulo)

Exponentiation by squaring modulo aka ESM
____

ESM - a kind of algorithms modular exponentiation, widely used in various cryptosystems, 
to accelerate computational operations with large numbers.

A significant benefit from this algorithm can be obtained by performing multiplication. 
Multiplication is carried out in two times faster when using this algorithm.

How to enter values:

For example, you need to vychilist 5 ^ 70 mod 62, then

python esm.py 5 70 62


Python: Python 2.7.*

# Example

Algorithms for fast modular exponentiation

Solve on the forehead: 789^654 mod 89 = 34

Solve by algorithm:

a^d mod m => 789^654 mod 89

1) d = 1010001110 (list of binary numbers)

2) b = a^d[9] = 1; A = a = 789

3) Cycle: A = A^2 mod m; b = b * A^d[i];


	d[8] = 1
	
	A = 789^2 mod 89 = 55
	
	b = 1 * 55^1 mod 89 = 55

	
	d[7] = 1
	
	A = 55^2 mod 89 = 88
	
	b = 55 * 88^1 mod 89 = 34

	
	d[6] = 1
	
	A = 88^2 mod 89 = 1
	
	b = 34 * 1^1 mod 89 = 34
	

	d[5] = 0
	
	A = 1^2 mod 89 = 1
	
	b = 34 * 1^0 mod 89 = 34
	

	d[4] = 0
	
	A = 1^2 mod 89 = 1
	
	b = 34 * 1^0 mod 89 = 34
	

	d[3] = 0
	
	A = 1^2 mod 89 = 1
	
	b = 34 * 1^0 mod 89 = 34
	

	d[2] = 1
	
	A = 1^2 mod 89 = 1
	
	b = 34 * 1^1 mod 89 = 34
	

	d[1] = 0
	
	A = 1^2 mod 89 = 1
	
	b = 34 * 1^0 mod 89 = 34
	

	d[0] = 1
	
	A = 1^2 mod 89 = 1
	
	b = 34 * 1^1 mod 89 = 34
	

4) Result: 789^654 mod 89 = 34
