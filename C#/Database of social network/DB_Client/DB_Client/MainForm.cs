using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace DB_Client
{
    public partial class MainForm : Form
    {
        private SqlConnection DataBase_0 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=0;Integrated Security=True");
        private SqlConnection DataBase_1 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=1;Integrated Security=True");
        private SqlConnection DataBase_2 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=2;Integrated Security=True");
        private SqlConnection DataBase_3 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=3;Integrated Security=True");
        private SqlConnection DataBase_4 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=4;Integrated Security=True");
        private SqlConnection DataBase_info = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=DB_info;Integrated Security=True");

        private int[] friend_list;

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            try
            {
                DataBase_0.Open();
                DataBase_1.Open();
                DataBase_2.Open();
                DataBase_3.Open();
                DataBase_4.Open();
                DataBase_info.Open();
            }
            catch (SqlException)
            {
                
                MessageBox.Show(
                    "Connection failed. DataBases states:\n" +
                    "\nDataBase #1: " + DataBase_0.State.ToString() +
                    "\nDataBase #2: " + DataBase_1.State.ToString() +
                    "\nDataBase #3: " + DataBase_2.State.ToString() +
                    "\nDataBase #4: " + DataBase_3.State.ToString() +
                    "\nDataBase #5: " + DataBase_4.State.ToString() +
                    "\nDataBase info: " + DataBase_info.State.ToString()
                );
            }
            catch { MessageBox.Show("Oops!"); }
        }

        private void get_connection(out SqlCommand cmd, int user_id)
        {
            SqlCommand get_db_id = new SqlCommand();
            get_db_id.Connection = DataBase_info;
            get_db_id.CommandType = CommandType.StoredProcedure;
            get_db_id.CommandText = "Get_DB_id";
            get_db_id.Parameters.Add("@User_id", SqlDbType.Int);
            get_db_id.Parameters["@User_id"].Value = user_id;
            get_db_id.Parameters.Add("@DB_id", SqlDbType.Int);
            get_db_id.Parameters["@DB_id"].Direction = ParameterDirection.Output;

            get_db_id.ExecuteNonQuery();

            cmd = new SqlCommand();
            switch (Convert.ToInt32(get_db_id.Parameters["@DB_id"].Value))
            {
                case 0:
                    cmd.Connection = DataBase_0;
                    break;
                case 1:
                    cmd.Connection = DataBase_1;
                    break;
                case 2:
                    cmd.Connection = DataBase_2;
                    break;
                case 3:
                    cmd.Connection = DataBase_3;
                    break;
                case 4:
                    cmd.Connection = DataBase_4;
                    break;
                default:
                    throw new FormatException("User id must be on range [1..500000].");
            }
        }

        private void get_button_Click(object sender, EventArgs e)
        {
            int user_id = 0;
            try
            {
                DataSet data_set;
                SqlCommand cmd;
                SqlDataReader data_reader;
                SqlDataAdapter data_adapter;

                userFriends_listBox.Items.Clear();
                user_id = Convert.ToInt32(userid_textBox.Text.ToString());

                get_connection(out cmd, user_id);
                cmd.CommandText = "select * from [User] where [id_user] =" + user_id.ToString();

                data_reader = cmd.ExecuteReader();
                data_reader.Read();
                if (data_reader.HasRows)
                {
                    userName_textBox.Text = data_reader["Name"].ToString();
                    userSurname_textBox.Text = data_reader["Surname"].ToString();
                    userAge_textBox.Text = data_reader["Age"].ToString();
                    userCity_textBox.Text = data_reader["City"].ToString();
                    userAbout_richTextBox.Text = data_reader["About"].ToString();
                    data_reader.Close();

                    cmd.CommandText = "select * from [Friends] where [id_user] =" + user_id.ToString();
                    data_set = new DataSet();
                    data_adapter = new SqlDataAdapter(cmd);
                    data_adapter.Fill(data_set);

                    DataSet f_data_set;

                    friend_list = new int[data_set.Tables[0].Rows.Count];

                    for (int i = 0; i < data_set.Tables[0].Rows.Count; i++)
                    {
                        get_connection(out cmd, Convert.ToInt32(data_set.Tables[0].Rows[i][2]));
                        cmd.CommandText = "select Name, Surname from [User] where [id_user] =" + Convert.ToInt32(data_set.Tables[0].Rows[i][2].ToString());
                        f_data_set = new DataSet();
                        data_adapter = new SqlDataAdapter(cmd);
                        data_adapter.Fill(f_data_set);

                        if (f_data_set.Tables[0].Rows.Count > 0)
                        {
                            friend_list[i] = Convert.ToInt32(data_set.Tables[0].Rows[i][2]);
                            userFriends_listBox.Items.Add(f_data_set.Tables[0].Rows[0]["Name"] + " " + f_data_set.Tables[0].Rows[0]["Surname"]);
                        }
                    }
                }
                else MessageBox.Show("Запись не найдена!");
            }
            catch (SqlException error)
            {
                MessageBox.Show(error.Message.ToString());
            }
            catch (FormatException error)
            {
                MessageBox.Show(error.Message);
            }
            catch (InvalidCastException error)
            {
                MessageBox.Show(error.Message);
            }
			catch
			{
				MessageBox.Show("Неизвестная ошибка.");
			}
        }

        private void userFriends_listBox_DoubleClick(object sender, EventArgs e)
        {
            if (friend_list.Count() > 0)
            {
                userid_textBox.Text = friend_list[userFriends_listBox.SelectedIndex].ToString();
                get_button_Click(sender, e);
            }
        }
    }
}
