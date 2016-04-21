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