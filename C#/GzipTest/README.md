# GZip 

ENG
---

ABOUT
-------

The program is written in C#, designed to compress and gunzip it files with 
using System.IO.Compression.GzipStream. Compression and decompression are used 
the flow System.Threading for a more efficient implementation of the algorithm. Threads 
shromisubani the mutual exclusion lock (operator lock).

The program works efficiently in a multiprocessor environment and is able to process 
files that are larger than available RAM.

USE
------
The parameters of the program, the names of the source and result files are specified in 
the command line as follows:

* for archiving: GZipTest.exe compress [source file name] [file name]

* to extract files: GZipTest.exe decompress [archive name] [name of the decompressed file]

If successful, the program returns 0, on error 1.



RU
---

ABOUT
-------

Программа написанная на C#, предназначенна для сжатия и разжатия файлов с 
помощью System.IO.Compression.GzipStream. При сжатии и распаковки используются 
потоки System.Threading для более эффективного исполнения алгоритма. Потоки 
сохронихзированы по блокировке взаимного исключения (оператор lock).

Программа работает эффективно в многопроцессорной среде и умеет обрабатывать 
файлы, размер которых превышает объем доступной оперативной памяти.

USE
------
Параметры программы, имена исходного и результирующего файлов задаются в 
командной строке следующим образом:

* для архивации: GZipTest.exe compress [имя исходного файла] [имя архива]

* для разархивации: GZipTest.exe decompress  [имя архива] [имя распакованного файла]

В случае успеха программа возвращает 0, при ошибке  1.

