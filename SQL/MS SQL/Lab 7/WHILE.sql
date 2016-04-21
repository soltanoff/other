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