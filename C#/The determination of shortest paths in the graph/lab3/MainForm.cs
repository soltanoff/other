using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace lab3
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
            is_first_multiple = true;
            open_file_button.Enabled = inc_button.Enabled = clear_button.Enabled = false;

            transform_matrix = false;
            user_matrix_dataGridView.CellValueChanged += user_matrix_dataGridView_CellContentClick;

        }
        /* ============================================================================================== */
        private const int COLUMN_WIDTH = 45;
        
        private const int INT_MAX_VALUE = 47483647;
        private const int MAX_VARIANTS = 25;
        private const string ENCODE_NAME = "windows-1251";

        bool is_first_multiple;
        bool transform_matrix;
        /* ============================================================================================== */
        private void ok_button_Click(object sender, EventArgs e)
        {
            prepare_information();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            try { increase_degree(); }
            catch { MessageBox.Show("Матрица пуста."); }
        }
        /* ============================================================================================== */
        private void prepare_information()
        {
            int n;
            bool fail = false;

            if (!int.TryParse(variant_textBox.Text.ToString(), out n))
                fail = true;
            else
            {
                n = Convert.ToInt32(variant_textBox.Text.ToString());
                if (n <= 0)
                    fail = true;
            }
            if (fail)
                MessageBox.Show("Вариант должен быть числом на интервале [1; " + MAX_VARIANTS.ToString() + "]");
            else
            {
                int variant = Convert.ToInt32(variant_textBox.Text);
                other_variant_textBox.Text = (variant % 7).ToString();
                matrix_init(5 + variant % 3, ref user_matrix_dataGridView);
                matrix_init(5 + variant % 3, ref prog_D_matrix_dataGridView, "");
                matrix_init(5 + variant % 3, ref prog_G_matrix_dataGridView, "");
                matrix_init(5 + variant % 3, ref prog_delta_matrix_dataGridView, "");

                open_file_button.Enabled = inc_button.Enabled = true;
                /*
                user_matrix_dataGridView[0, 0].Value = "0";
                user_matrix_dataGridView[1, 0].Value = "30";
                user_matrix_dataGridView[2, 0].Value = "inf";
                user_matrix_dataGridView[3, 0].Value = "20";
                user_matrix_dataGridView[4, 0].Value = "inf";
                user_matrix_dataGridView[5, 0].Value = "inf";

                user_matrix_dataGridView[0, 1].Value = "inf";
                user_matrix_dataGridView[1, 1].Value = "0";
                user_matrix_dataGridView[2, 1].Value = "15";
                user_matrix_dataGridView[3, 1].Value = "15";
                user_matrix_dataGridView[4, 1].Value = "inf";
                user_matrix_dataGridView[5, 1].Value = "inf";

                user_matrix_dataGridView[0, 2].Value = "inf";
                user_matrix_dataGridView[1, 2].Value = "15";
                user_matrix_dataGridView[2, 2].Value = "0";
                user_matrix_dataGridView[3, 2].Value = "20";
                user_matrix_dataGridView[4, 2].Value = "25";
                user_matrix_dataGridView[5, 2].Value = "inf";

                user_matrix_dataGridView[0, 3].Value = "20";
                user_matrix_dataGridView[1, 3].Value = "15";
                user_matrix_dataGridView[2, 3].Value = "20";
                user_matrix_dataGridView[3, 3].Value = "0";
                user_matrix_dataGridView[4, 3].Value = "inf";
                user_matrix_dataGridView[5, 3].Value = "25";

                user_matrix_dataGridView[0, 4].Value = "inf";
                user_matrix_dataGridView[1, 4].Value = "inf";
                user_matrix_dataGridView[2, 4].Value = "25";
                user_matrix_dataGridView[3, 4].Value = "10";
                user_matrix_dataGridView[4, 4].Value = "0";
                user_matrix_dataGridView[5, 4].Value = "40";

                user_matrix_dataGridView[0, 5].Value = "15";
                user_matrix_dataGridView[1, 5].Value = "inf";
                user_matrix_dataGridView[2, 5].Value = "inf";
                user_matrix_dataGridView[3, 5].Value = "25";
                user_matrix_dataGridView[4, 5].Value = "40";
                user_matrix_dataGridView[5, 5].Value = "0";
                /**/
            }
        }
        /* ============================================================================================== */
        private void matrix_init(int col_count, ref DataGridView matrix, string main_diag_element = "0")
        {
            char alphabet_symbol;

            matrix.RowCount = matrix.ColumnCount = col_count;

            for (int i = 0; i < col_count; i++)
            {
                matrix.Columns[i].Width = COLUMN_WIDTH;

                alphabet_symbol = (char)(i + 65);
                matrix.Rows[i].HeaderCell.Value = matrix.Columns[i].HeaderText = alphabet_symbol.ToString();
                matrix.Rows[i].HeaderCell.Style.Alignment = DataGridViewContentAlignment.NotSet;
                
                matrix[i, i].Value = main_diag_element;
            }
         
            matrix.RowHeadersWidth = COLUMN_WIDTH;
            matrix.DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter;
            matrix.ColumnHeadersDefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter;

            /*
            if (variant_textBox.Text.Length > 0 && col_count >= col_min && col_count <= col_max)
            {
                char alphabet_symbol;
                prog_D_matrix_dataGridView.RowCount = prog_D_matrix_dataGridView.ColumnCount = col_count;
                user_matrix_dataGridView.RowCount = user_matrix_dataGridView.ColumnCount = col_count;
                for (int i = 0; i < user_matrix_dataGridView.ColumnCount; i++)
                {
                    prog_D_matrix_dataGridView.Columns[i].Width = user_matrix_dataGridView.Columns[i].Width = column_width;
                    alphabet_symbol = (char)(i + 65);
                    user_matrix_dataGridView.Rows[i].HeaderCell.Value = user_matrix_dataGridView.Columns[i].HeaderText = alphabet_symbol.ToString();
                    prog_D_matrix_dataGridView.Rows[i].HeaderCell.Value = prog_D_matrix_dataGridView.Columns[i].HeaderText = alphabet_symbol.ToString();

                    prog_D_matrix_dataGridView[i, i].Value = user_matrix_dataGridView[i, i].Value = "0";
                }
                
            }
            */
        }
        public void matrix_multiple(DataGridView a, DataGridView b)
        {
            int[,] res = new int[a.ColumnCount, a.ColumnCount];

            for (int i = 0; i < a.ColumnCount; i++)
            {
                for (int j = 0; j < a.ColumnCount; j++)
                {
                    for (int k = 0; k < a.ColumnCount; k++)
                    {
                        res[i, j] += Convert.ToInt32(a[i, k].Value.ToString()) * Convert.ToInt32(b[k, j].Value.ToString());
                    }
                }
            }

            for (int i = 0; i < prog_D_matrix_dataGridView.ColumnCount; i++)
            {
                for (int j = 0; j < prog_D_matrix_dataGridView.ColumnCount; j++)
                {
                    prog_D_matrix_dataGridView[i, j].Value = res[i, j];
                }
            }
        }
        public void copy_matrix(DataGridView from_matrix, ref DataGridView to_matrix)
        {
            for (int i = 0; i < from_matrix.ColumnCount; i++)
                for (int j = 0; j < from_matrix.ColumnCount; j++)
                    to_matrix[i, j].Value = from_matrix[i, j].Value;
        }
        public void clear_matrixes()
        {
            for (int i = 0; i < user_matrix_dataGridView.ColumnCount; i++)
                for (int j = 0; j < user_matrix_dataGridView.ColumnCount; j++)
                {
                    user_matrix_dataGridView[i, j].Value =
                        prog_D_matrix_dataGridView[i, j].Value =
                        prog_G_matrix_dataGridView[i, j].Value =
                        prog_delta_matrix_dataGridView[i, j].Value = "";
                    if (i == j)
                        user_matrix_dataGridView[i, j].Value = "0";
                }
        }
        /* ============================================================================================== */
        public int try_to_convert(String str)
        {
            int result = 0;

            if (str == "inf")
            {
                result = INT_MAX_VALUE;
            }
            else
            {
                try
                {
                    result = Convert.ToInt32(str);
                }
                catch (System.FormatException)
                {
                    result = INT_MAX_VALUE;
                }
                catch (System.OverflowException error)
                {
                    MessageBox.Show(error.Message);
                }
            }
            return result;
        }
        public void transitive_ways(DataGridView a, DataGridView b)
        {
            int[,] res = new int[a.ColumnCount, a.ColumnCount];
            int[] min_mass = new int[a.ColumnCount];

            int f_val, s_val;

            for (int i = 0; i < a.ColumnCount; i++)
            {
                for (int j = 0; j < a.ColumnCount; j++)
                {
                    for (int k = 0; k < a.ColumnCount; k++)
                    {
                        //f_val = try_to_convert(a[i, k].Value.ToString()); 
                        //s_val = try_to_convert(b[k, j].Value.ToString());
                        f_val = try_to_convert(a[k, i].Value.ToString());
                        s_val = try_to_convert(b[j, k].Value.ToString());


                        min_mass[k] = f_val + s_val;
                    }
                    res[i, j] = min_mass.Min();
                }
            }


            bool is_compare = true;
            bool cycle_out = false;
            for (int i = 0; i < prog_D_matrix_dataGridView.ColumnCount; i++)
            {
                for (int j = 0; j < prog_D_matrix_dataGridView.ColumnCount; j++)
                {
                    if (prog_D_matrix_dataGridView[j, i].Value.ToString() != res[i, j].ToString())
                    {
                        is_compare = false;
                        cycle_out = true;
                        break;
                    }
                }
                if (cycle_out) break;
            }

            if (is_compare)
            {
                transform_matrix = true;
                matrix_transformed();
            }
            else
            {

                for (int i = 0; i < prog_D_matrix_dataGridView.ColumnCount; i++)
                {
                    for (int j = 0; j < prog_D_matrix_dataGridView.ColumnCount; j++)
                    {
                        if (res[i, j] == INT_MAX_VALUE)
                            prog_D_matrix_dataGridView[j, i].Value = "inf"; // i j
                        else
                            prog_D_matrix_dataGridView[j, i].Value = res[i, j];
                    }
                }
            }
        }
        public void transitive_ways_with_pos(DataGridView a, DataGridView b)
        {
            int[,] res = new int[a.ColumnCount, a.ColumnCount];
            int[] min_mass = new int[a.ColumnCount];

            int f_val, s_val;

            for (int i = 0; i < a.ColumnCount; i++)
            {
                for (int j = 0; j < a.ColumnCount; j++)
                {
                    for (int k = 0; k < a.ColumnCount; k++)
                    {
                        f_val = try_to_convert(a[k, i].Value.ToString());
                        s_val = try_to_convert(b[j, k].Value.ToString());

                        min_mass[k] = f_val + s_val;
                    }
                    int indexMin = Array.FindIndex(min_mass, x => x == min_mass.Min());
                    res[i, j] = 65 + indexMin;
                }
            }

            for (int i = 0; i < prog_delta_matrix_dataGridView.ColumnCount; i++)
            {
                for (int j = 0; j < prog_delta_matrix_dataGridView.ColumnCount; j++)
                {
                    if (i == j) prog_delta_matrix_dataGridView[j, i].Value = "-";
                    else prog_delta_matrix_dataGridView[j, i].Value = ((char)res[i, j]); // i j
                }
            }
        }
        /* ============================================================================================== */
        private void increase_degree()
        {
            if (is_first_multiple)
            {
                transitive_ways(user_matrix_dataGridView, user_matrix_dataGridView);
                is_first_multiple = false;
            }
            else transitive_ways(prog_D_matrix_dataGridView, user_matrix_dataGridView);

            if (!transform_matrix) prog_matrix_label.Text = (Convert.ToInt32(prog_matrix_label.Text) + 1).ToString();
            else
            {   //if (Convert.ToInt32(prog_matrix_label.Text) == user_matrix_dataGridView.ColumnCount)
                matrix_transformed();

                copy_matrix(user_matrix_dataGridView, ref prog_G_matrix_dataGridView);

                for (int i = 0; i < prog_G_matrix_dataGridView.ColumnCount; i++)
                    if (prog_G_matrix_dataGridView[i, i].Value.ToString() == "0") prog_G_matrix_dataGridView[i, i].Value = "inf";

                transitive_ways_with_pos(prog_G_matrix_dataGridView, prog_D_matrix_dataGridView);
            }
        }
        private void matrix_transformed()
        {
            inc_button.Enabled = false;
            prog_matrix_name_label.Text = "Матрица D";
            prog_matrix_label.Text = "";
        }
        private void clear_button_Click(object sender, EventArgs e)
        {
            clear_matrixes();
            prog_matrix_label.Text = "1";
            prog_matrix_name_label.Text = "Матрица L";
            inc_button.Enabled = true;
            is_first_multiple = true;
            transform_matrix = false;
        }
        private void user_matrix_dataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            if (!clear_button.Enabled) clear_button.Enabled = !clear_button.Enabled;
        }
        /* ============================================================================================== */
        private void variant_textBox_TextChanged(object sender, EventArgs e)
        {
            
        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }
        /* ============================================================================================== */
        private void open_file_button_Click(object sender, EventArgs e)
        {
            matrix_openFileDialog.ShowDialog();
        }
        private void matrix_openFileDialog_FileOk(object sender, CancelEventArgs e)
        {
            try
            {
                StreamReader read_file = new StreamReader(matrix_openFileDialog.OpenFile(), Encoding.GetEncoding(ENCODE_NAME));

                String matrix_line;
                String[] matrix_line_elements;

                for (int i = 0; i < user_matrix_dataGridView.ColumnCount; i++)
                {
                    matrix_line = read_file.ReadLine();
                    matrix_line_elements = matrix_line.Split('\t');
                    for (int j = 0; j < user_matrix_dataGridView.ColumnCount; j++)
                    {
                        user_matrix_dataGridView[j, i].Value = matrix_line_elements[j];
                    }
                }

                read_file.Close();
            }
            catch
            {
                MessageBox.Show("Ошибка открытия файла!");
                clear_button_Click(sender, e);
            }
        }
        /* ============================================================================================== */
    }
}
