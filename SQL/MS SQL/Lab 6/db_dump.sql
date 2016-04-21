USE [master]
GO
/****** Object:  Database [Hospital(v3.0)]    Script Date: 07.04.2016 20:35:21 ******/
CREATE DATABASE [Hospital(v3.0)]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Hospital(v3.0)', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\Hospital(v3.0).mdf' , SIZE = 5120KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'Hospital(v3.0)_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\DATA\Hospital(v3.0)_log.ldf' , SIZE = 2048KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [Hospital(v3.0)] SET COMPATIBILITY_LEVEL = 120
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Hospital(v3.0)].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Hospital(v3.0)] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET ARITHABORT OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Hospital(v3.0)] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Hospital(v3.0)] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Hospital(v3.0)] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Hospital(v3.0)] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Hospital(v3.0)] SET  MULTI_USER 
GO
ALTER DATABASE [Hospital(v3.0)] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Hospital(v3.0)] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Hospital(v3.0)] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Hospital(v3.0)] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
ALTER DATABASE [Hospital(v3.0)] SET DELAYED_DURABILITY = DISABLED 
GO
USE [Hospital(v3.0)]
GO
/****** Object:  Table [dbo].[Doctor]    Script Date: 07.04.2016 20:35:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Doctor](
	[id_doc] [int] NOT NULL,
	[Doc_Name] [varchar](15) NOT NULL,
	[Doc_Surname] [varchar](15) NOT NULL,
	[Doc_Middle_name] [varchar](15) NULL,
	[Doc_Bday_date] [date] NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Doctor_Specialty]    Script Date: 07.04.2016 20:35:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Doctor_Specialty](
	[id_doc_spec] [int] NOT NULL,
	[id_doc] [int] NOT NULL,
	[id_spec] [int] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Patient]    Script Date: 07.04.2016 20:35:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Patient](
	[id_pat] [int] NOT NULL,
	[Pat_Name] [varchar](15) NOT NULL,
	[Pat_Surname] [varchar](15) NOT NULL,
	[Pat_Middle_name] [varchar](15) NULL,
	[Pat_Bday_date] [date] NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[Reception_History]    Script Date: 07.04.2016 20:35:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Reception_History](
	[id_rec_history] [int] NOT NULL,
	[id_pat] [int] NOT NULL,
	[id_doc_spec] [int] NULL,
	[Date_reception] [smalldatetime] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[Specialty]    Script Date: 07.04.2016 20:35:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Specialty](
	[id_spec] [int] NOT NULL,
	[Spec_Name] [varchar](30) NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[Doctor] ([id_doc], [Doc_Name], [Doc_Surname], [Doc_Middle_name], [Doc_Bday_date]) VALUES (0, N'Сергей', N'Иванов', N'Петрович', CAST(N'1987-01-21' AS Date))
INSERT [dbo].[Doctor] ([id_doc], [Doc_Name], [Doc_Surname], [Doc_Middle_name], [Doc_Bday_date]) VALUES (1, N'Наталья', N'Кришталь', N'Олеговна', CAST(N'1988-07-11' AS Date))
INSERT [dbo].[Doctor] ([id_doc], [Doc_Name], [Doc_Surname], [Doc_Middle_name], [Doc_Bday_date]) VALUES (2, N'Михаил', N'Колтышев', N'Алексеевич', CAST(N'1985-12-01' AS Date))
INSERT [dbo].[Doctor] ([id_doc], [Doc_Name], [Doc_Surname], [Doc_Middle_name], [Doc_Bday_date]) VALUES (3, N'Евгения', N'Алиханова', N'Федоровна', CAST(N'1989-08-23' AS Date))
INSERT [dbo].[Doctor] ([id_doc], [Doc_Name], [Doc_Surname], [Doc_Middle_name], [Doc_Bday_date]) VALUES (4, N'Петров', N'Анатолий', N'Павлович', CAST(N'1977-02-02' AS Date))
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (0, 0, 0)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (1, 0, 1)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (2, 0, 3)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (3, 1, 5)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (4, 2, 6)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (5, 3, 4)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (6, 3, 2)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (7, 4, 7)
INSERT [dbo].[Doctor_Specialty] ([id_doc_spec], [id_doc], [id_spec]) VALUES (8, 1, 0)
INSERT [dbo].[Patient] ([id_pat], [Pat_Name], [Pat_Surname], [Pat_Middle_name], [Pat_Bday_date]) VALUES (0, N'Анастасия', N'Арбаева', NULL, CAST(N'1999-01-21' AS Date))
INSERT [dbo].[Patient] ([id_pat], [Pat_Name], [Pat_Surname], [Pat_Middle_name], [Pat_Bday_date]) VALUES (1, N'Мария', N'Киоллер', N'Артемовна', CAST(N'1990-02-03' AS Date))
INSERT [dbo].[Patient] ([id_pat], [Pat_Name], [Pat_Surname], [Pat_Middle_name], [Pat_Bday_date]) VALUES (2, N'Себастьян', N'Пауль', NULL, CAST(N'1988-11-14' AS Date))
INSERT [dbo].[Patient] ([id_pat], [Pat_Name], [Pat_Surname], [Pat_Middle_name], [Pat_Bday_date]) VALUES (3, N'Карина', N'Федосеева', N'Олеговна', CAST(N'1991-01-01' AS Date))
INSERT [dbo].[Patient] ([id_pat], [Pat_Name], [Pat_Surname], [Pat_Middle_name], [Pat_Bday_date]) VALUES (4, N'Александр', N'Пастух', NULL, CAST(N'1988-09-09' AS Date))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (0, 0, 0, CAST(N'2016-03-23 11:22:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (1, 0, 1, CAST(N'2016-03-03 11:00:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (2, 1, 3, CAST(N'2016-03-02 11:40:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (3, 2, 2, CAST(N'2016-03-11 12:15:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (4, 3, 1, CAST(N'2016-03-10 14:00:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (5, 4, 0, CAST(N'2016-03-23 16:00:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (6, 1, 5, CAST(N'2016-03-04 13:25:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (7, 1, 7, CAST(N'2014-03-10 10:11:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (8, 3, 7, CAST(N'2013-03-23 12:15:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (9, 3, 5, CAST(N'2012-03-04 15:00:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (10, 0, 5, CAST(N'2016-03-04 16:25:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (11, 0, 1, CAST(N'2015-03-04 17:22:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (12, 2, 2, CAST(N'2015-03-04 16:22:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (13, 0, 5, CAST(N'2015-02-21 12:15:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (14, 4, 1, CAST(N'2016-03-21 12:51:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (15, 4, 2, CAST(N'2016-03-22 12:51:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (16, 4, 3, CAST(N'2016-03-23 12:51:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (17, 4, 4, CAST(N'2016-03-24 12:51:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (18, 4, 5, CAST(N'2016-03-25 12:51:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (19, 4, 6, CAST(N'2016-03-26 12:51:00' AS SmallDateTime))
INSERT [dbo].[Reception_History] ([id_rec_history], [id_pat], [id_doc_spec], [Date_reception]) VALUES (20, 4, 7, CAST(N'2016-03-27 12:51:00' AS SmallDateTime))
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (0, N'Терапевт')
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (1, N'Венеролог')
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (2, N'Инфекционист')
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (3, N'Невролог')
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (4, N'Кардиолог')
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (5, N'Отоларинголог')
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (6, N'Офтальмолог')
INSERT [dbo].[Specialty] ([id_spec], [Spec_Name]) VALUES (7, N'Хирург')
/****** Object:  Index [PK_DOCTOR]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Doctor] ADD  CONSTRAINT [PK_DOCTOR] PRIMARY KEY NONCLUSTERED 
(
	[id_doc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON

GO
/****** Object:  Index [UQ__Doctor__E7CF71BC209E9DC1]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Doctor] ADD UNIQUE NONCLUSTERED 
(
	[Doc_Name] ASC,
	[Doc_Surname] ASC,
	[Doc_Middle_name] ASC,
	[Doc_Bday_date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK_DOCTOR_SPECIALTY]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Doctor_Specialty] ADD  CONSTRAINT [PK_DOCTOR_SPECIALTY] PRIMARY KEY NONCLUSTERED 
(
	[id_doc_spec] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [Relationship_1_FK]    Script Date: 07.04.2016 20:35:22 ******/
CREATE NONCLUSTERED INDEX [Relationship_1_FK] ON [dbo].[Doctor_Specialty]
(
	[id_doc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [Relationship_2_FK]    Script Date: 07.04.2016 20:35:22 ******/
CREATE NONCLUSTERED INDEX [Relationship_2_FK] ON [dbo].[Doctor_Specialty]
(
	[id_spec] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK_PATIENT]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Patient] ADD  CONSTRAINT [PK_PATIENT] PRIMARY KEY NONCLUSTERED 
(
	[id_pat] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON

GO
/****** Object:  Index [UQ__Patient__FEC36724C40C0168]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Patient] ADD UNIQUE NONCLUSTERED 
(
	[Pat_Name] ASC,
	[Pat_Surname] ASC,
	[Pat_Middle_name] ASC,
	[Pat_Bday_date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK_RECEPTION_HISTORY]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Reception_History] ADD  CONSTRAINT [PK_RECEPTION_HISTORY] PRIMARY KEY NONCLUSTERED 
(
	[id_rec_history] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [UQ__Receptio__EE8E07F7FF65C9A8]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Reception_History] ADD UNIQUE NONCLUSTERED 
(
	[Date_reception] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [PK_SPECIALTY]    Script Date: 07.04.2016 20:35:22 ******/
ALTER TABLE [dbo].[Specialty] ADD  CONSTRAINT [PK_SPECIALTY] PRIMARY KEY NONCLUSTERED 
(
	[id_spec] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Doctor_Specialty]  WITH CHECK ADD  CONSTRAINT [FK_DOCTOR_S_RELATIONS_DOCTOR] FOREIGN KEY([id_doc])
REFERENCES [dbo].[Doctor] ([id_doc])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Doctor_Specialty] CHECK CONSTRAINT [FK_DOCTOR_S_RELATIONS_DOCTOR]
GO
ALTER TABLE [dbo].[Doctor_Specialty]  WITH CHECK ADD  CONSTRAINT [FK_DOCTOR_S_RELATIONS_SPECIALT] FOREIGN KEY([id_spec])
REFERENCES [dbo].[Specialty] ([id_spec])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Doctor_Specialty] CHECK CONSTRAINT [FK_DOCTOR_S_RELATIONS_SPECIALT]
GO
ALTER TABLE [dbo].[Reception_History]  WITH CHECK ADD  CONSTRAINT [FK_RECEPTIO_REFERENCE_DOCTOR_S] FOREIGN KEY([id_doc_spec])
REFERENCES [dbo].[Doctor_Specialty] ([id_doc_spec])
GO
ALTER TABLE [dbo].[Reception_History] CHECK CONSTRAINT [FK_RECEPTIO_REFERENCE_DOCTOR_S]
GO
ALTER TABLE [dbo].[Reception_History]  WITH CHECK ADD  CONSTRAINT [FK_Reception_History_Patient] FOREIGN KEY([id_pat])
REFERENCES [dbo].[Patient] ([id_pat])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Reception_History] CHECK CONSTRAINT [FK_Reception_History_Patient]
GO
USE [master]
GO
ALTER DATABASE [Hospital(v3.0)] SET  READ_WRITE 
GO
