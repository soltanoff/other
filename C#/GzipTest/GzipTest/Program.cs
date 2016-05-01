using System;
using System.IO;
using System.IO.Compression;
using System.Diagnostics;
using System.Threading;
using System.Runtime.InteropServices;

namespace GzipTest
{
    public class GZip
    {
        static object locker = new object();
        static FileStream fsInput;
        static FileStream fsOutput;
        static GZipStream gzipStream;
        static int bytesCount;

        static float perFreeRAM = 0.7f; // 70 % - верняя граница для свободного ОЗУ
        static float perBufferSize = 0.05f; // 5 % - величина буфера относительно свободного ОЗУ
        /*
        static long CountFreeRAM()
        {
            using (PerformanceCounter ramCounter = new PerformanceCounter("Memory", "Available MBytes"))
            {
                return (long)(ramCounter.NextValue() * 1024 * 1024);
            }
        }
        /**/
        static ulong SetBuffSize() // 5% от свободной памяти
        {
            //ulong freeRAMSize = CountFreeRAM();
            MEMORYSTATUSEX memEx = new MEMORYSTATUSEX();
            GlobalMemoryStatusEx(memEx);

            if ((ulong)fsInput.Length >= (ulong)(perFreeRAM * memEx.ullAvailPhys)) // если больше 70% от свободного озу
                return (ulong)(perBufferSize * memEx.ullAvailPhys);
            else
                return (ulong)fsInput.Length;
        }

        public static void Compress(String fileSource, String fileDestination)
        {
            using (fsInput = new FileStream(fileSource, FileMode.Open, FileAccess.Read))
            {
                using (fsOutput = new FileStream(fileDestination, FileMode.Create, FileAccess.Write))
                {
                    using (gzipStream = new GZipStream(fsOutput, CompressionMode.Compress))
                    {
                        Console.WriteLine("Start to compress file.");

                        SetThreads(ThreadRoutineCompress);

                        gzipStream.Dispose();
                        gzipStream.Close();
                        Console.WriteLine("File compressed.");
                    }
                    fsOutput.Dispose();
                    fsOutput.Close();
                }
                fsInput.Dispose();
                fsInput.Close();
            }
        }

        public static void Decompress(String fileSource, String fileDestination)
        {
            using (fsInput = new FileStream(fileSource, FileMode.Open, FileAccess.Read))
            {
                using (fsOutput = new FileStream(fileDestination, FileMode.Create, FileAccess.Write))
                {
                    using (gzipStream = new GZipStream(fsInput, CompressionMode.Decompress))
                    {
                        Console.WriteLine("Start to decompress file.");

                        SetThreads(ThreadRoutineDecompress);

                        gzipStream.Dispose();
                        gzipStream.Close();
                        Console.WriteLine("File decompressed.");
                    }
                    fsOutput.Dispose();
                    fsOutput.Close();
                }
                fsInput.Dispose();
                fsInput.Close();
            }
        }

        static void SetThreads(ThreadStart Routine)
        {
            Thread threadOne = new Thread(Routine);
            Thread threadTwo = new Thread(Routine);

            threadOne.Name = "Thread #1";
            threadTwo.Name = "Thread #2";
            threadOne.Start();
            threadTwo.Start();


            threadOne.Join();
            threadTwo.Join();
        }

        static void ThreadRoutineCompress()
        {
            Byte[] buffer = new Byte[SetBuffSize()];
            lock (locker) { bytesCount = 1; }
            while (bytesCount > 0)//(bytesCount = fsInput.Read(buffer, 0, buffer.Length)) > 0)
            {
                lock (locker)
                {
                    bytesCount = fsInput.Read(buffer, 0, buffer.Length);
                    gzipStream.Write(buffer, 0, bytesCount);
                }
            }
        }

        static void ThreadRoutineDecompress()
        {
            Byte[] buffer = new Byte[SetBuffSize()];
            lock (locker) { bytesCount = 1; }
            while (bytesCount > 0)//(bytesCount = gzipStream.Read(buffer, 0, buffer.Length)) > 0)
            {
                lock (locker)
                {
                    bytesCount = gzipStream.Read(buffer, 0, buffer.Length);
                    fsOutput.Write(buffer, 0, bytesCount);
                }
            }
        }
        /* ================================================================================= */
        [DllImport("kernel32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool GlobalMemoryStatusEx([In, Out] MEMORYSTATUSEX lpBuffer);

        [StructLayout(LayoutKind.Sequential)]
        public class MEMORYSTATUSEX
        {
            /// <summary>
            /// Size of the structure, in bytes. You must set this member before calling GlobalMemoryStatusEx. 
            /// </summary>
            public uint dwLength;

            /// <summary>
            /// Number between 0 and 100 that specifies the approximate percentage of physical memory that is in use (0 indicates no memory use and 100 indicates full memory use). 
            /// </summary>
            public uint dwMemoryLoad;

            /// <summary>
            /// Total size of physical memory, in bytes.
            /// </summary>
            public ulong ullTotalPhys;

            /// <summary>
            /// Size of physical memory available, in bytes. 
            /// </summary>
            public ulong ullAvailPhys;

            /// <summary>
            /// Size of the committed memory limit, in bytes. This is physical memory plus the size of the page file, minus a small overhead. 
            /// </summary>
            public ulong ullTotalPageFile;

            /// <summary>
            /// Size of available memory to commit, in bytes. The limit is ullTotalPageFile. 
            /// </summary>
            public ulong ullAvailPageFile;

            /// <summary>
            /// Total size of the user mode portion of the virtual address space of the calling process, in bytes. 
            /// </summary>
            public ulong ullTotalVirtual;

            /// <summary>
            /// Size of unreserved and uncommitted memory in the user mode portion of the virtual address space of the calling process, in bytes. 
            /// </summary>
            public ulong ullAvailVirtual;

            /// <summary>
            /// Size of unreserved and uncommitted memory in the extended portion of the virtual address space of the calling process, in bytes. 
            /// </summary>
            public ulong ullAvailExtendedVirtual;

            /// <summary>
            /// Initializes a new instance of the <see cref="T:MEMORYSTATUSEX"/> class.
            /// </summary>
            public MEMORYSTATUSEX()
            {
                this.dwLength = (uint)Marshal.SizeOf(typeof(MEMORYSTATUSEX));
            }
        }
        /* ================================================================================= */
    }

    class Program
    {
        static void BeginCompress(string[] args)
        {
            if (args.Length >= 3)
                // args[1] имя файла, args[2] имя архива
                GZip.Compress(args[1], args[2]);
            else
                throw new Exception("Not enough options for compression.");
        }

        static void BeginDecompress(string[] args)
        {
            if (args.Length >= 3)
                // args[1] имя архива, args[2] имя файла
                GZip.Decompress(args[1], args[2]);
            else
                throw new Exception("Not enough options for decompression.");
        }

        static void StartGzip(string[] args)
        {
            switch (args[0])
            {
                case "compress":
                    BeginCompress(args);
                    break;
                case "decompress":
                    BeginDecompress(args);
                    break;
                default:
                    throw new Exception(
                        "Unknown options \"" +
                        args[0] +
                        "\". Use \"compress\" and \"decompress\"."
                        );
            }
        }

        static int Main(string[] args)
        {
            if (args.Length > 0)
            {
                try 
                { 
                    StartGzip(args);
                    return 0;
                }
                catch (Exception error) 
                { 
                    Console.WriteLine(error.Message);
                    return 1;
                }
            }
            else
            {
                /*
                //string sourcePath = "t.avi";
                string sourcePath = "test.log";

                string compressed = Path.ChangeExtension(sourcePath, "gz");
                string decompressed = sourcePath.Insert(sourcePath.Length - 4, "_");

                GZip.Compress(sourcePath, compressed);
                GZip.Decompress(compressed, decompressed);

                string str1 = File.ReadAllText(sourcePath);
                string str2 = File.ReadAllText(decompressed);

                if (str1.Equals(str2))
                    Console.WriteLine("Files is compare.");
                else
                    Console.WriteLine("Files is not compare.");
                /**/
                /* ================================================================================= */
                //PerformanceCounter ramCounter = new PerformanceCounter("Memory", "Available MBytes");
                //int i = (int)(ramCounter.NextValue() * 1024 * 1024);
                //MEMORYSTATUSEX memEx = new MEMORYSTATUSEX();
                //GlobalMemoryStatusEx(memEx);
                /* ================================================================================= */
                Console.WriteLine("Not enough options. Use \"compress\" and \"decompress\".");
                //Console.ReadKey();
                return 1;
            }
        }
    }
}