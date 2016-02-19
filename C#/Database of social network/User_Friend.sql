/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2012                    */
/* Created on:     19.02.2016 12:34:30                          */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('Friends') and o.name = 'FK_FRIENDS_REFERENCE_USER')
alter table Friends
   drop constraint FK_FRIENDS_REFERENCE_USER
go

if exists (select 1
            from  sysobjects
           where  id = object_id('Friends')
            and   type = 'U')
   drop table Friends
go

if exists (select 1
            from  sysobjects
           where  id = object_id('"User"')
            and   type = 'U')
   drop table "User"
go

/*==============================================================*/
/* Table: Friends                                               */
/*==============================================================*/
create table Friends (
   id_friends           int                  not null,
   id_user              int                  null,
   Friend_id            int                  not null,
   constraint PK_FRIENDS primary key (id_friends)
)
go

/*==============================================================*/
/* Table: "User"                                                */
/*==============================================================*/
create table "User" (
   id_user              int                  not null,
   Surname              varchar(100)         not null,
   Name                 varchar(100)         not null,
   Age                  int                  not null,
   City                 varchar(100)         null,
   About                varchar(1000)        null,
   constraint PK_USER primary key (id_user)
)
go

alter table Friends
   add constraint FK_FRIENDS_REFERENCE_USER foreign key (id_user)
      references "User" (id_user)
go

