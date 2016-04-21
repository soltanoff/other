select * from Specialty
go

select id_pat, id_doc_spec
from Reception_History
where id_pat = 4
go

select Doctor.id_doc, Doc_Name, Doc_Surname, Spec_Name
from 
	Specialty, Doctor_Specialty, Doctor
where
	Doctor_Specialty.id_spec = Specialty.id_spec and
	Doctor_Specialty.id_doc = Doctor.id_doc
order by Spec_Name
go

select Patient.id_pat, Pat_Name, Pat_Surname, Pat_Middle_name, Spec_Name
from 
	Specialty, 
	Doctor_Specialty, 
	Reception_History, 
	Patient
where
	Doctor_Specialty.id_spec = Specialty.id_spec and
	Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
	Reception_History.id_pat = Patient.id_pat
order by Spec_Name
go

/* ж) Пациенты, которые никогда не посещали хирурга */
select distinct Patient.id_pat, Pat_Name, Pat_Surname, Pat_Middle_name
from 
	Patient
where
	not exists
	(
		select *
		from 
			Specialty S, 
			Doctor_Specialty DS, 
			Reception_History RH--, 
			--Patient P 
		where
			DS.id_spec = S.id_spec and
			DS.id_doc_spec = RH.id_doc_spec and
			RH.id_pat = Patient.id_pat and
			S.Spec_Name = 'Хирург'
	)
go

select distinct Patient.id_pat, Pat_Name, Pat_Surname, Pat_Middle_name
from 
	Specialty, 
	Doctor_Specialty, 
	Reception_History, 
	Patient
where
	Doctor_Specialty.id_spec = Specialty.id_spec and
	Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
	Reception_History.id_pat = Patient.id_pat and 
	Patient.id_pat not in
	(
		select distinct P.id_pat 
		from 
			Specialty S, 
			Doctor_Specialty DS, 
			Reception_History RH, 
			Patient P 
		where
			DS.id_spec = S.id_spec and
			DS.id_doc_spec = RH.id_doc_spec and
			RH.id_pat = P.id_pat and 
			S.Spec_Name = '’ирург'
	)
go
/* з) Пациентов, которые посетили всех специалистов */
select distinct Patient.id_pat, Pat_Name, Pat_Surname, Pat_Middle_name
from 
	Patient
where
	not exists (
	select * from Specialty S where not exists 
		(
			select * 
			from 
				Specialty S1, 
				Doctor_Specialty DS, 
				Reception_History RH, 
				Patient P
			where 
			DS.id_spec = S.id_spec and
			DS.id_doc_spec = RH.id_doc_spec and
			RH.id_pat = P.id_pat and 
			RH.id_pat = Patient.id_pat and
			S1.id_spec = S.id_spec
		)
	)
go

select distinct Patient.id_pat, Pat_Name, Pat_Surname, Pat_Middle_name
from 
	Specialty, 
	Doctor_Specialty, 
	Reception_History, 
	Patient
where
	Doctor_Specialty.id_spec = Specialty.id_spec and
	Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
	Reception_History.id_pat = Patient.id_pat and 
	not exists (
	select * from Specialty S where not exists 
		(
			select * 
			from 
				Specialty S1, 
				Doctor_Specialty DS, 
				Reception_History RH, 
				Patient P
			where 
			DS.id_spec = S.id_spec and
			DS.id_doc_spec = RH.id_doc_spec and
			RH.id_pat = P.id_pat and 
			RH.id_pat = Reception_History.id_pat and
			S1.id_spec = S.id_spec
		)
	)
go
/* и) Врачи, не совмещающие работу по различным специальностям */
select distinct Doctor.id_doc, Doc_Name, Doc_Surname, Doc_Middle_name
from 
	Doctor
where
	exists
	(
		select *
		from 
			Doctor_Specialty DS
		where
			DS.id_doc = Doctor.id_doc
		having
			count(DS.id_spec) = 1
	)
go

select distinct Doctor.id_doc, Doc_Name, Doc_Surname, Doc_Middle_name
from 
	Doctor_Specialty, Doctor
where
	Doctor.id_doc = Doctor_Specialty.id_doc
group by 
	Doctor.id_doc, Doc_Name, Doc_Surname, Doc_Middle_name
having
	count(Doctor_Specialty.id_spec) = 1
go

/* *) Врачи, чье количество принятых пациентов превышает среднее количество принятых пациентов всеми врачами */
select Count(distinct id_pat) pat_count, Doctor.id_doc, Doc_Name, Doc_Surname, Doc_Middle_name
from
	Reception_History, Doctor_Specialty, Doctor
where
	Doctor_Specialty.id_doc_spec = Reception_History.id_doc_spec and
	Doctor.id_doc = Doctor_Specialty.id_doc
group by Doctor.id_doc, Doctor.id_doc, Doc_Name, Doc_Surname, Doc_Middle_name
having
	Count(distinct id_pat) > 
	(
		select avg(pat_count) as avg_count
		from
		(
			select Count(distinct id_pat) pat_count, id_doc
			from
				Reception_History RH, Doctor_Specialty DS
			where
				DS.id_doc_spec = RH.id_doc_spec
			group by id_doc
		) as pat_count_table
	)
go