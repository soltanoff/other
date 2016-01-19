domains
	city = string
	day = string

	
predicates
	nondeterm city(city)
	nondeterm day(day)

	nondeterm eq(string, string)
	nondeterm equal(string, string, string, string, string, string)

	nondeterm creat_rasp(city, day, city, day, city, day)

	nondeterm condition1(city, day)
	nondeterm condition2(city, day)
	nondeterm condition3(city, day)
	nondeterm condition4(city, day)

	
clauses
	day("Monday").
	day("Tuesday").
	day("Wednesday").

	city("Plutograd").
	city("Nizhny Malograd").
	city("Verhny Bolshegrad").	

% C - city, D - day
	creat_rasp(C1, D1, C2, D2, C3, D3):-
		equal(C1, D1, C2, D2, C3, D3),
		condition1(C1, D1),
		condition2(C1, D1),
		condition3(C2, D2),
		condition4(C3, D3).

%=========================== Revisor #1 ========================================

	condition1(C1,_):- not(eq(C1, "Verhny Bolshegrad")). % ** CX 1)
	condition2("Plutograd", D1):- not(eq(D1, "Monday")). % ** CX 2)

%===============================================================================

%=========================== Revisor #2 ========================================

	condition3(C2, D2):- % ** KK 1)-2)
		eq(C2, "Verhny Bolshegrad"),
		not(eq(D2, "Tuesday")), not(eq(D2, "Monday")).

	condition3(C2, D2):- % ** KK 1)-2)
		eq(C2, "Nizhny Malograd"),
		not(eq(D2, "Tuesday")), not(eq(D2, "Monday")).

%===============================================================================

%=========================== Revisor #3 ========================================

	condition4(C3, "Monday"):- not(eq(C3, "Nizhny Malograd")). % ** L 1)

%===============================================================================
	equal(C1, D1, C2, D2, C3, D3):-
		city(C1), city(C2), city(C3), 
		day(D1), day(D2), day(D3),
		not(eq(C1, C2)), not(eq(C1, C3)), not(eq(C2, C3)),
		not(eq(D1, D2)), not(eq(D1, D3)), not(eq(D2, D3)).
	eq(X, X).
	
	
goal
	creat_rasp(X1, Y1, X2, Y2, X3, Y3),
	write("Auditor 1: go to \"", X1, "\" on ", Y1), nl,
	write("Auditor 2: go to \"", X2, "\" on ", Y2), nl,
	write("Auditor 3: go to \"", X3, "\" on ", Y3), nl, nl.