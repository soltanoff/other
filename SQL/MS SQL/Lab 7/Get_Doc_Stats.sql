/* Количество пациентов принятых больницей за указанный год */
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
		set @id = (select id_doc from Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name is null and Doc_Bday_date = @bday)
	else 
		set @id = (select id_doc from Doctor where Doc_Name = @name and Doc_Surname = @surname and Doc_Middle_name = @middle_name and Doc_Bday_date = @bday)
	
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
	PRINT N'Статистика врача.';
	select * from #Doc_Stats
	PRINT N'Сводка посещений врача пациентами.';
	select 
		Count(distinct id_pat) as Pat_Count, Year(Reception_History.Date_reception) as [Year]
	from 
		Doctor_Specialty, Reception_History, Doctor
	where
		Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
		Doctor_Specialty.id_doc = @id
	group by
		Year(Reception_History.Date_reception)
	/**/
	drop table #Doc_Stats
end
go
/* ======================================================================== */

exec Get_Doc_Stats 'Сергей', 'Иванов', 'Петрович', '21.01.1987'
go

select 
	Count(distinct id_pat) as Pat_Count, Year(Reception_History.Date_reception) as [Year]
from 
	Doctor_Specialty, Reception_History, Doctor
where
	Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
	Doctor_Specialty.id_doc = Doctor.id_doc and
	Doctor.Doc_Name = 'Сергей' and
	Doctor.Doc_Surname = 'Иванов' and
	Doctor.Doc_Middle_name = 'Петрович'
group by
	Year(Reception_History.Date_reception)
go