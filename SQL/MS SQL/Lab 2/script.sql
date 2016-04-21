delete from Reception_History
delete from Specialty
delete from Doctor
delete from Patient
go
/* ====================================================== */
insert into Patient values
	(0, null, 'Анастасия', 'Арбаева', null, '21.01.1999'),
	(1, null, 'Мария', 'Киоллер', 'Артемовна', '03.02.1990'),
	(2, null, 'Себастьян', 'Пауль', null, '14.11.1988'),
	(3, null, 'Карина', 'Федосеева', 'Олеговна', '01.01.1991'),
	(4, null, 'Александр', 'Пастух', null, '09.09.1988')
go

select * from Patient
go
/* ====================================================== */
insert into Specialty values (0, 'Терапевт')
insert into Specialty values 
	(1, 'Венеролог'),
	(2, 'Инфекционист'),
	(3, 'Невролог'),
	(4, 'Онколог'),
	(5, 'Отоларинголог'),
	(6, 'Офтальмолог')
go

select * from Specialty
go
/* ====================================================== */
delete from Doctor 
go

insert into Doctor values 
	(0, 'Сергей', 'Иванов', 'Петрович', '21.01.1987'),
	(1, 'Наталья', 'Кришталь', 'Олеговна', '11.07.1988'),
	(2, 'Михаил', 'Колтышев', 'Алексеевич', '01.12.1985'),
	(3, 'Евгения', 'Алиханова', 'Федоровна', '23.08.1989')
go

select * from Doctor
go
/* ====================================================== */
insert into Doctor_Specialty values 
	(0, 0, 0),
	(1, 0, 1),
	(2, 0, 3),
	(3, 1, 5),
	(4, 2, 6)
go

insert into Doctor_Specialty values 
		(5, 
			(select id_doc from Doctor where Doc_Name = 'Евгения' and Doc_Surname = 'Алиханова'), 
			(select id_spec from Specialty where Spec_name = 'Онколог')
		),
		(6, 
			(select id_doc from Doctor where Doc_Name = 'Евгения' and Doc_Surname = 'Алиханова'), 
			(select id_spec from Specialty where Spec_name = 'Инфекционист')
		)
	
go

select * from Doctor_Specialty
go
/* ====================================================== */
/* ====================================================== */
insert into Reception_History values
	(0, 
		(
			select id_doc_spec from Doctor_Specialty 
				where id_doc = (select id_doc from Doctor where Doc_Name = 'Сергей' and Doc_Surname = 'Иванов') and
					id_spec = (select id_spec from Specialty where Spec_Name = 'Терапевт')
		), 
	'21.03.2016 16:00')
update Patient
	set
		id_rec_history = 0
	where
		Pat_Name = 'Карина' and
		Pat_Surname = 'Федосеева'
go

insert into Reception_History values
	(1, 1, '22.03.2016 12:00')
update Patient
	set
		id_rec_history = 1
	where
		id_pat = 0 
go

insert into Reception_History values
	(2, 3, '22.03.2016 14:00')
update Patient
	set
		id_rec_history = 2
	where
		id_pat = 1
go

insert into Reception_History values
	(3, 4, '21.03.2016 12:00')
update Patient
	set
		id_rec_history = 3
	where
		id_pat = 2
go
		
insert into Reception_History values
	(4, 2, '24.03.2016 12:00')
update Patient
	set
		id_rec_history = 4
	where
		id_pat = 4  
go

select * from Reception_History
go
/* ====================================================== */
alter table Reception_History add 
	Patient_count smallint
go

alter table Reception_History drop column Patient_count
go

alter table Doctor_Specialty add
	unique(id_doc, id_spec)
go
/* ====================================================== */
/* Некорректные */

/*
delete from Specialty
go

delete from Doctor
go
*/

/*
insert into Specialty values
	(0, 'Стоматолог')
go

insert into Patient values
	(40, null, 'Александр', 'Пастух', null, '09.09.1988')
go
*/

/*
update Reception_History
	set
		Date_reception = '24.03.2016 12:00'
	where
		id_rec_history = 3
go

update Doctor
	set
		id_doc = 10
	where
		id_doc = 0
go
*/