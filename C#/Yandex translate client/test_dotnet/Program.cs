using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace test_dotnet
{
    static class Program
    {
        /// <summary>
        /// Главная точка входа для приложения.
        /// </summary>
        [STAThread]
        static void Main()
        {
            try
            {
                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new mainform());
            }
            catch
            {
                MessageBox.Show("Mainform ERROR. Обратитесь к разработчику.\nhttp://vk.com/id96996256");
            }
        }
    }
}
