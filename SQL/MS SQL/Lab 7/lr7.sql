/* 1) Процедура добавления специалиста; */
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
/* 2) Процедура удаления специалиста; */
create procedure Delete_Specialist
	@name varchar(15),
	@surname varchar(15),
	@middle_name varchar(15),
	@bday date
as begin
	if @middle_name is null
		delete Doctor 
where 
Doc_Name = @name and 
Doc_Surname = @surname and 
Doc_Middle_name is null and Doc_Bday_date = @bday
	else 
		delete Doctor 
where 
Doc_Name = @name and 
Doc_Surname = @surname and 
Doc_Middle_name = @middle_name and Doc_Bday_date = @bday

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

/* 3) Количество пациентов принятых больницей за указанный год; */
create procedure Get_Pat_Count @year int, @pat_count int = 0 out
as begin
	select 
		@pat_count = Count(distinct id_pat)
	from 
		Reception_History
	where
		Year(Reception_History.Date_reception) = @year
end
go
declare @x int
exec Get_Pat_Count 2010, @x out
select @x
/* 4) Количество пациентов принятых больницей за указанный год; */
create procedure Get_Doc_Stats 
	@name varchar(15),
	@surname varchar(15),
	@middle_name varchar(15),
	@bday date
as begin
	declare @id int
	declare @pat_count int
	declare @avg_yaer_pat_cout int
	declare @spec_count int

	if @middle_name is null
		set @id = (
select id_doc 
from Doctor 
where 
Doc_Name = @name and 
Doc_Surname = @surname and 
Doc_Middle_name is null and 
Doc_Bday_date = @bday
)
	else 
		set @id = (
select id_doc 
from Doctor 
where 
Doc_Name = @name and 
Doc_Surname = @surname and 
Doc_Middle_name = @middle_name and 
Doc_Bday_date = @bday
)
	
	if @id is null
		return
	
	create table #Doc_Stats (
		name varchar(15),
		surname varchar(15),
		middle_name varchar(15),
		bday date,
		all_pat_count int,
		spec_count int,
		avg_year_pat_count int
	)

	set @pat_count = (
		select Count(distinct id_pat)
		from Doctor_Specialty, Reception_History
		where
			Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
			Doctor_Specialty.id_doc = @id
	)

	set @spec_count = (
		select Count(distinct id_spec)
		from Doctor_Specialty
		where
			Doctor_Specialty.id_doc = @id
	)
	insert into #Doc_Stats values (
		@name,
		@surname,
		@middle_name,
		@bday,
		@pat_count,
		@spec_count,
		(select Avg(pat_count)
		from
		(
			select Count(distinct id_pat) as pat_count
			from Doctor_Specialty, Reception_History
			where
				Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
				Doctor_Specialty.id_doc = @id
			group by
				Year(Date_reception)
		) as temp)
	)
	select * from #Doc_Stats
	drop table #Doc_Stats
end
go
exec Get_Doc_Stats 'Сергей', 'Иванов', 'Петрович', '21.01.1987'
go
/* 5) вывести среднее значение и статистику по годам */
declare @x int
set @x = (
	select Avg(pat_count)
	from
	(
		select 
			Count(distinct id_pat) as pat_count
		from 
			Reception_History as RH
		group by
			Year(RH.Date_reception)
	) as C
)
select @x as avg_pat_count

select 
	Year(RH.Date_reception) as [year],
	pat_count = 
	case
		when Count(distinct id_pat) < @x then 'Меньше среднего'
		when Count(distinct id_pat) = @x then 'Среднее значение'
		when Count(distinct id_pat) > @x then 'Больше среднего'
	end
from 
	Reception_History RH
group by
	Year(RH.Date_reception)
go

/* 6) сформировать докторам зарплаты случайно, чтобы среднее значение 
	было не меньше 15,000р. */
create table #Doc_Salary (
	id_doc int,
	salary money
)

declare @doc_count int
select @doc_count = (select Count(id_doc) from Doctor)

while @doc_count <> 0
begin
	set @doc_count = @doc_count - 1
	insert into #Doc_Salary values
		(@doc_count, cast(9000*rand() as money))
end

select 
	Doc_Name, Doc_Surname, Doc_Middle_name, 
	salary as Doc_Salary 
from Doctor, #Doc_Salary 
where Doctor.id_doc = #Doc_Salary.id_doc
	
while (select avg(salary) from #Doc_Salary) < 15000
	update #Doc_Salary
		set salary = salary * 1.1

select 
	Doc_Name, Doc_Surname, Doc_Middle_name, 
	salary as Doc_Salary 
from Doctor, #Doc_Salary 
where Doctor.id_doc = #Doc_Salary.id_doc

drop table #Doc_Salary
go