/* Процедура добавления специалиста */
create procedure Add_Specialist
	@name varchar(15),
	@surname varchar(15),
	@middle_name varchar(15),
	@bday date,
	@specialty varchar(30)
as begin
	declare @doc_id int
	declare @new_doc_spec_id int
	declare @id_spec int

	set @new_doc_spec_id = (select max(id_doc_spec) from Doctor_Specialty) + 1
	if @new_doc_spec_id is null
		set @new_doc_spec_id = 0

	set @id_spec = (select id_spec from Specialty where Spec_Name = @specialty)
	if @id_spec is null
	begin
		set @id_spec = (select max(id_spec) from Specialty) + 1
		if @id_spec is null
			set @id_spec = 0

		insert into Specialty values
			(@id_spec, @specialty)
	end

	if @middle_name is null
		set @doc_id = (select id_doc from Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name is null and Doc_Bday_date = @bday)
	else 
		set @doc_id = (select id_doc from Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name = @middle_name and Doc_Bday_date = @bday)
	if @doc_id is null
	begin
		set @doc_id = (select max(id_doc) from Doctor) + 1
		if @doc_id is null
			set @doc_id = 0

		insert into Doctor values
			(@doc_id, @name, @surname, @middle_name, @bday)
	end

	insert into Doctor_Specialty values
		(@new_doc_spec_id, @doc_id, @id_spec)
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