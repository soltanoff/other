/* г) количество пациентов, принятых каждым из врачей за прошедший год; */

select 
		Count(id_pat) as Pat_Count, 
		Year(Date_reception) as Selected_Year
	from 
		Reception_History
	group by 
		Year(Reception_History.Date_reception)
	having 
		Year(Reception_History.Date_reception) = Year(GETDATE()) - 1

/* д) врачи, принявшие меньше всего пациентов; */

select
		Doc_Surname, Doc_Name, Doc_Middle_name
	from
		Doctor, 
		Reception_History,
		Doctor_Specialty,
		(
			select 
				Min(Count_Pat) as Min_Pat_Count
			from
				(
					select 
						Count(id_pat) as Count_Pat
					from 
						Reception_History,
						Doctor_Specialty
					where
						Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec
					group by
						id_doc
				) as Count_Table
		) as Min_Count
	where
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and
		Doctor.id_doc = Doctor_Specialty.id_doc
	group by 
		Doc_Name, Doc_Surname, Doc_Middle_name, Min_Pat_Count
	having 
		Count(id_pat) = Min_Pat_Count

/* е) врачей, у которых количество принимаемых пациентов превышает среднее; */

select
		Doc_Surname, Doc_Name, Doc_Middle_name
	from
		Doctor, 
		Reception_History,
		Doctor_Specialty,
		(
			select 
				Avg(Count_Pat) as Avg_Pat_Count
			from
				(
					select 
						Count(id_pat) as Count_Pat
					from 
						Reception_History,
						Doctor_Specialty
					where
						Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec
					group by
						id_doc
				) as Count_Table
		) as Avg_Count
	where
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and
		Doctor.id_doc = Doctor_Specialty.id_doc
	group by 
		Doc_Name, Doc_Surname, Doc_Middle_name, Avg_Pat_Count
	having 
		Count(id_pat) > Avg_Pat_Count

/* *) пациентов, посещавших и хирурга, и кардиолога; */

select 
		Patient.Pat_Name, 
		Patient.Pat_Surname, 
		Patient.Pat_Middle_name
	from
		Patient,
		Reception_History,
		Doctor_Specialty,
		Specialty
	where
		Doctor_Specialty.id_spec = Specialty.id_spec and
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and
		Patient.id_pat = Reception_History.id_pat
	group by 
		Pat_Name,
		Pat_Surname, 
		Pat_Middle_name,
		Specialty.Spec_Name
	having 
		Specialty.Spec_Name = 'Хирург'
intersect
select  
		Patient.Pat_Name, 
		Patient.Pat_Surname, 
		Patient.Pat_Middle_name
	from
		Patient,
		Reception_History,
		Doctor_Specialty,
		Specialty
	where
		Doctor_Specialty.id_spec = Specialty.id_spec and
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and
		Patient.id_pat = Reception_History.id_pat
	group by 
		Pat_Name,
		Pat_Surname, 
		Pat_Middle_name,
		Specialty.Spec_Name
	having 
		Specialty.Spec_Name = 'Кардиолог'

/* *) список специальностей врачей, к которым не обращался пациент с id 1, но обращался пациент с id 0   */

select 
		Specialty.id_spec, Spec_Name
	from
		Reception_History,
		Doctor_Specialty,
		Specialty
	where
		Doctor_Specialty.id_spec = Specialty.id_spec and
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and 
		id_pat = 0
	group by
		Specialty.id_spec, Spec_Name
except
select 
		Specialty.id_spec, Spec_Name
	from
		Reception_History,
		Doctor_Specialty,
		Specialty
	where
		Doctor_Specialty.id_spec = Specialty.id_spec and
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and 
		id_pat = 1
	group by
		Specialty.id_spec, Spec_Name

/* *) список пациентов, посещавших или терапевта, или кардиолога; */

select 
		Patient.Pat_Name, 
		Patient.Pat_Surname, 
		Patient.Pat_Middle_name
	from
		Patient,
		Reception_History,
		Doctor_Specialty,
		Specialty
	where
		Doctor_Specialty.id_spec = Specialty.id_spec and
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and
		Patient.id_pat = Reception_History.id_pat
	group by 
		Pat_Name,
		Pat_Surname, 
		Pat_Middle_name,
		Specialty.Spec_Name
	having 
		Specialty.Spec_Name = 'Терапевт'
union
select  
		Patient.Pat_Name, 
		Patient.Pat_Surname, 
		Patient.Pat_Middle_name
	from
		Patient,
		Reception_History,
		Doctor_Specialty,
		Specialty
	where
		Doctor_Specialty.id_spec = Specialty.id_spec and
		Reception_History.id_doc_spec = Doctor_Specialty.id_doc_spec and
		Patient.id_pat = Reception_History.id_pat
	group by 
		Pat_Name,
		Pat_Surname, 
		Pat_Middle_name,
		Specialty.Spec_Name
	having 
		Specialty.Spec_Name = 'Кардиолог'