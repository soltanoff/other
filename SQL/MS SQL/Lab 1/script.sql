/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2008                    */
/* Created on:     15.02.2016 14:55:56                          */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('Doctor_Specialty') and o.name = 'FK_DOCTOR_S_RELATIONS_DOCTOR')
alter table Doctor_Specialty
   drop constraint FK_DOCTOR_S_RELATIONS_DOCTOR
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('Doctor_Specialty') and o.name = 'FK_DOCTOR_S_RELATIONS_SPECIALT')
alter table Doctor_Specialty
   drop constraint FK_DOCTOR_S_RELATIONS_SPECIALT
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('Patient') and o.name = 'FK_PATIENT_RELATIONS_RECEPTIO')
alter table Patient
   drop constraint FK_PATIENT_RELATIONS_RECEPTIO
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('Reception_History') and o.name = 'FK_RECEPTIO_REFERENCE_DOCTOR_S')
alter table Reception_History
   drop constraint FK_RECEPTIO_REFERENCE_DOCTOR_S
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Doctor')
            and   name  = 'Relationship_4_FK'
            and   indid > 0
            and   indid < 255)
   drop index Doctor.Relationship_4_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('Doctor')
            and   type = 'U')
   drop table Doctor
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Doctor_Specialty')
            and   name  = 'Relationship_2_FK'
            and   indid > 0
            and   indid < 255)
   drop index Doctor_Specialty.Relationship_2_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Doctor_Specialty')
            and   name  = 'Relationship_1_FK'
            and   indid > 0
            and   indid < 255)
   drop index Doctor_Specialty.Relationship_1_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('Doctor_Specialty')
            and   type = 'U')
   drop table Doctor_Specialty
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Patient')
            and   name  = 'Relationship_5_FK'
            and   indid > 0
            and   indid < 255)
   drop index Patient.Relationship_5_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('Patient')
            and   type = 'U')
   drop table Patient
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Reception_History')
            and   name  = 'Relationship_7_FK'
            and   indid > 0
            and   indid < 255)
   drop index Reception_History.Relationship_7_FK
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Reception_History')
            and   name  = 'Relationship_3_FK'
            and   indid > 0
            and   indid < 255)
   drop index Reception_History.Relationship_3_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('Reception_History')
            and   type = 'U')
   drop table Reception_History
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('Specialty')
            and   name  = 'Relationship_6_FK'
            and   indid > 0
            and   indid < 255)
   drop index Specialty.Relationship_6_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('Specialty')
            and   type = 'U')
   drop table Specialty
go

/*==============================================================*/
/* Table: Doctor                                                */
/*==============================================================*/
create table Doctor (
   id_doc               int                  not null,
   Doc_Name             varchar(15)          not null,
   Doc_Surname          varchar(15)          not null,
   Doc_Middle_name      varchar(15)          null,
   Doc_Bday_date        date                 not null,
   unique(Doc_Name, Doc_Surname, Doc_Middle_name, Doc_Bday_date),
   constraint PK_DOCTOR primary key nonclustered (id_doc)
)
go

/*==============================================================*/
/* Table: Doctor_Specialty                                      */
/*==============================================================*/
create table Doctor_Specialty (
   id_doc_spec          int                  not null,
   id_doc               int                  not null,
   id_spec              int                  not null,
   constraint PK_DOCTOR_SPECIALTY primary key nonclustered (id_doc_spec)
)
go

/*==============================================================*/
/* Index: Relationship_1_FK                                     */
/*==============================================================*/
create index Relationship_1_FK on Doctor_Specialty (
id_doc ASC
)
go

/*==============================================================*/
/* Index: Relationship_2_FK                                     */
/*==============================================================*/
create index Relationship_2_FK on Doctor_Specialty (
id_spec ASC
)
go

/*==============================================================*/
/* Table: Patient                                               */
/*==============================================================*/
create table Patient (
   id_pat               int                  not null,
   id_rec_history       int                  null,
   Pat_Name             varchar(15)          not null,
   Pat_Surname          varchar(15)          not null,
   Pat_Middle_name      varchar(15)          null,
   Pat_Bday_date        date                 not null,
   unique(Pat_Name, Pat_Surname, Pat_Middle_name, Pat_Bday_date),
   constraint PK_PATIENT primary key nonclustered (id_pat)
)
go

/*==============================================================*/
/* Index: Relationship_5_FK                                     */
/*==============================================================*/
create index Relationship_5_FK on Patient (
id_rec_history ASC
)
go

/*==============================================================*/
/* Table: Reception_History                                     */
/*==============================================================*/
create table Reception_History (
   id_rec_history       int                  not null,
   id_doc_spec          int                  null,
   Date_reception       smalldatetime        not null unique,
   constraint PK_RECEPTION_HISTORY primary key nonclustered (id_rec_history)
)
go

/*==============================================================*/
/* Table: Specialty                                             */
/*==============================================================*/
create table Specialty (
   id_spec              int                  not null,
   Spec_Name            varchar(30)          not null,
   constraint PK_SPECIALTY primary key nonclustered (id_spec)
)
go

alter table Doctor_Specialty
   add constraint FK_DOCTOR_S_RELATIONS_DOCTOR foreign key (id_doc)
      references Doctor (id_doc)
	  on update no action
	  on delete cascade
go

alter table Doctor_Specialty
   add constraint FK_DOCTOR_S_RELATIONS_SPECIALT foreign key (id_spec)
      references Specialty (id_spec)
	  on update no action
	  on delete cascade
go

alter table Patient
   add constraint FK_PATIENT_RELATIONS_RECEPTIO foreign key (id_rec_history)
      references Reception_History (id_rec_history)
	  on update no action
	  on delete set null
go

alter table Reception_History
   add constraint FK_RECEPTIO_REFERENCE_DOCTOR_S foreign key (id_doc_spec)
      references Doctor_Specialty (id_doc_spec)
	  /*on update no action*/
	  /*on delete cascade*/
go

