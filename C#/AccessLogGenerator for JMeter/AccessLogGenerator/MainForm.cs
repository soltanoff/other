using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AccessLogGenerator
{
    public partial class MainForm : Form
    {
        private const string FILENAME = "AccessLog.log";
        private const string ENCODE_NAME = "windows-1251";

        public MainForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                gen_progressBar.Maximum = Convert.ToInt32(countVar_textBox.Text) + 1;

                StreamWriter write_file = new StreamWriter(FILENAME, false, Encoding.GetEncoding(ENCODE_NAME));
                for (gen_progressBar.Value = 1; gen_progressBar.Value < gen_progressBar.Maximum; gen_progressBar.Value++)
                {
                    write_file.WriteLine(
                        "\"GET /" + url_textBox.Text +
                        "?" + getParam_textBox.Text + 
                        "=" + gen_progressBar.Value.ToString());
                    this.Show();
                }
                write_file.Close();
                MessageBox.Show("Generated!");
            }
            catch (Exception error)
            {
                MessageBox.Show(error.Message);
            }
        }
    }
}
