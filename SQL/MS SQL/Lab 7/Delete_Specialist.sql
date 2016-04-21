/* Процедура удаления специалиста */
create procedure Delete_Specialist
	@name varchar(15),
	@surname varchar(15),
	@middle_name varchar(15),
	@bday date
as begin
	if @middle_name is null
		delete Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name is null and Doc_Bday_date = @bday
	else 
		delete Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name = @middle_name and Doc_Bday_date = @bday

	create table #Useless_Spec (id_spec int primary key)
	insert into #Useless_Spec
		select id_spec from Specialty
		except
		select distinct Doctor_Specialty.id_spec
		from Doctor, Doctor_Specialty
		where Doctor.id_doc = Doctor_Specialty.id_doc
	
	if exists (select * from #Useless_Spec)
		delete Specialty where id_spec in (select #Useless_Spec.id_spec from #Useless_Spec)

	drop table #Useless_Spec
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
exec Add_Specialist 'Test2', 'Testov2', null, '21.05.1922', 'Test2'
go
exec Delete_Specialist 'Test2', 'Testov2', null, '21.05.1922'
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
/* ======================================================================== */