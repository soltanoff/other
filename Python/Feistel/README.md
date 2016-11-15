# Feistel network

Simple Feistel network
____

schema.pdf - schema of decoding by this network.

Main params:

* ALPH = u"абвгдежзийклмнопрстуфхцчшщъыьэюя+-,.!?:'vin()0123456789"

* MODULE = 55

* KEYS = [29, 26, 1]

* P = [3, 4, 1, 2]

How to work:

1) Set to "q" your encoded string

2) Run script


Python: Python 2.7.12

# Example

q = u"ц:кvя72(+,й0жвб3"

LEFT SIDE: [22, 38, 10, 40, 31, 52, 47, 43]
E: key = 1 
	INPUT:  [22, 38, 10, 40] [31, 52, 47, 43]

	Exec f():

		S: (1 * 22) mod 55 = 22

		S: (1 * 38) mod 55 = 38

		S: (1 * 10) mod 55 = 10

		S: (1 * 40) mod 55 = 40

		P: IN: [22, 38, 10, 40] | OUT: [10, 40, 22, 38]

	MOD: (31 - 10) mod 55 = 21

	MOD: (52 - 40) mod 55 = 12

	MOD: (47 - 22) mod 55 = 25

	MOD: (43 - 38) mod 55 = 5

	OUTPUT: [21, 12, 25, 5] [22, 38, 10, 40]

E: key = 26 
	INPUT:  [21, 12, 25, 5] [22, 38, 10, 40]

	Exec f():

		S: (26 * 21) mod 55 = 51

		S: (26 * 12) mod 55 = 37

		S: (26 * 25) mod 55 = 45

		S: (26 * 5) mod 55 = 20

		P: IN: [51, 37, 45, 20] | OUT: [45, 20, 51, 37]

	MOD: (22 - 45) mod 55 = 32

	MOD: (38 - 20) mod 55 = 18

	MOD: (10 - 51) mod 55 = 14

	MOD: (40 - 37) mod 55 = 3

	OUTPUT: [32, 18, 14, 3] [21, 12, 25, 5]

E: key = 29 
	INPUT:  [32, 18, 14, 3] [21, 12, 25, 5]

	Exec f():

		S: (29 * 32) mod 55 = 48

		S: (29 * 18) mod 55 = 27

		S: (29 * 14) mod 55 = 21

		S: (29 * 3) mod 55 = 32

		P: IN: [48, 27, 21, 32] | OUT: [21, 32, 48, 27]

	MOD: (21 - 21) mod 55 = 0

	MOD: (12 - 32) mod 55 = 35

	MOD: (25 - 48) mod 55 = 32

	MOD: (5 - 27) mod 55 = 33

	OUTPUT: [0, 35, 32, 33] [32, 18, 14, 3]

RIGHT SIDE: [22, 38, 10, 40, 31, 52, 47, 43]
E: key = 1 
	INPUT:  [32, 34, 9, 45] [6, 2, 1, 48]

	Exec f():

		S: (1 * 32) mod 55 = 32

		S: (1 * 34) mod 55 = 34

		S: (1 * 9) mod 55 = 9

		S: (1 * 45) mod 55 = 45

		P: IN: [32, 34, 9, 45] | OUT: [9, 45, 32, 34]

	MOD: (6 - 9) mod 55 = 52

	MOD: (2 - 45) mod 55 = 12

	MOD: (1 - 32) mod 55 = 24

	MOD: (48 - 34) mod 55 = 14

	OUTPUT: [52, 12, 24, 14] [32, 34, 9, 45]

E: key = 26 
	INPUT:  [52, 12, 24, 14] [32, 34, 9, 45]

	Exec f():

		S: (26 * 52) mod 55 = 32

		S: (26 * 12) mod 55 = 37

		S: (26 * 24) mod 55 = 19

		S: (26 * 14) mod 55 = 34

		P: IN: [32, 37, 19, 34] | OUT: [19, 34, 32, 37]

	MOD: (32 - 19) mod 55 = 13

	MOD: (34 - 34) mod 55 = 0

	MOD: (9 - 32) mod 55 = 32

	MOD: (45 - 37) mod 55 = 8

	OUTPUT: [13, 0, 32, 8] [52, 12, 24, 14]

E: key = 29 
	INPUT:  [13, 0, 32, 8] [52, 12, 24, 14]

	Exec f():

		S: (29 * 13) mod 55 = 47

		S: (29 * 0) mod 55 = 0

		S: (29 * 32) mod 55 = 48

		S: (29 * 8) mod 55 = 12

		P: IN: [47, 0, 48, 12] | OUT: [48, 12, 47, 0]

	MOD: (52 - 48) mod 55 = 4

	MOD: (12 - 12) mod 55 = 0

	MOD: (24 - 47) mod 55 = 32

	MOD: (14 - 0) mod 55 = 14

	OUTPUT: [4, 0, 32, 14] [13, 0, 32, 8]


RESULT: а.+-+тогда+она+и