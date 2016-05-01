/*
alter table Doctor_Specialty add unique(id_doc, id_spec)
go
*/
/* Процедура удаления специалиста */
create procedure Delete_Specialist
	@name varchar(15),
	@surname varchar(15),
	@middle_name varchar(15),
	@bday date,
	@specialty varchar(30)
as
	declare @id_doc int
	declare @id_spec int

	if @middle_name is null
		set @id_doc = (select id_doc from Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name is null and Doc_Bday_date = @bday)
	else 
		set @id_doc = (select id_doc from Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name = @middle_name and Doc_Bday_date = @bday)

	set @id_spec = (select id_spec from Specialty where Spec_Name = @specialty)

	if (@id_spec is not null and @id_doc is not null)
	begin
		if (exists (select * from Doctor_Specialty where id_spec = @id_spec and id_doc = @id_doc))
		begin
			delete Doctor_Specialty where id_doc = @id_doc and id_spec = @id_spec

			if (not exists (select * from Doctor_Specialty where id_spec = @id_spec))
				delete Specialty where id_spec = @id_spec

			if (not exists (select * from Doctor_Specialty where id_doc = @id_doc))
				delete Doctor where id_doc = @id_doc
		end
	end
go

/* ======================================================================== */
delete Doctor
delete Specialty
/* ======================================================================== */
exec Add_Specialist 'Test', 'Testov', null, '21.05.1922', 'Test'
go
exec Add_Specialist 'Test', 'Testov', null, '21.05.1922', 'Test2'
go
exec Add_Specialist 'Test1', 'Testov1', 'Testovich1', '21.05.1922', 'Test'
go
exec Add_Specialist 'Test1', 'Testov1', 'Testovich1', '21.05.1922', 'Test333'
go
exec Add_Specialist 'Test2', 'Testov2', null, '21.05.1922', 'Test1'
go
exec Delete_Specialist 'Test2', 'Testov2', null, '21.05.1922', 'Test1'
go
/* ======================================================================== */
select
	Doc_Name, Doc_Surname, Doc_Middle_name, Spec_Name 
from 
	Doctor, Doctor_Specialty, Specialty
where 
	Doctor.id_doc = Doctor_Specialty.id_doc and
	Doctor_Specialty.id_spec = Specialty.id_spec
select * from Doctor_Specialty
select * from Specialty
select * from Patient
select * from Reception_History
/* ======================================================================== */
insert into Patient values
	(0, 'Qw', 'ER', 'Ty', '21.01.1488'),
	(1, 'As', 'Df', 'GH', '21.01.1488'),
	(2, 'Zx', 'Cv', 'BN', '21.01.1488')

insert into Reception_History values
	(0, 0, 1, '21.01.2016'),
	(1, 1, 2, '21.01.2016'),
	(2, 2, 3, '21.01.2016')
