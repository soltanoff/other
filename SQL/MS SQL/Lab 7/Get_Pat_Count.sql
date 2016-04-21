/* Количество пациентов принятых больницей за указанный год */
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
/* ======================================================================== */
declare @x int
exec Get_Pat_Count 2010, @x out
select @x
/* ======================================================================== */
select 
	Count(distinct id_pat) as Pat_Count, Year(Reception_History.Date_reception) as [Year]
from 
	Reception_History
group by
	Year(Reception_History.Date_reception)
go
/* ======================================================================== */