using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;
using System.Data.SqlClient;
using System.Net;
using Enyim.Caching;
using Enyim.Caching.Configuration;
using Enyim.Caching.Memcached;
using System.Text.RegularExpressions;



namespace DB_Client
{
    public partial class MainForm : Form
    {
        const int MAX_USERS_COUNT = 500000;

        SqlConnection DataBase_0 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=0;Integrated Security=True");
        SqlConnection DataBase_1 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=1;Integrated Security=True");
        SqlConnection DataBase_2 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=2;Integrated Security=True");
        SqlConnection DataBase_3 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=3;Integrated Security=True");
        SqlConnection DataBase_4 = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=4;Integrated Security=True");
        SqlConnection DataBase_info = new SqlConnection(@"Data Source=PETTISSON;Initial Catalog=DB_info;Integrated Security=True");
        
        System.Diagnostics.Stopwatch timer = new System.Diagnostics.Stopwatch();
        Enyim.Caching.MemcachedClient mcache_client;
        MemcachedClientConfiguration mcache_config;

        string mcache_ip = "127.0.0.1";
        int mcache_port = 11211;

        int[] friend_list;

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            
            try
            {
                mcache_config = new MemcachedClientConfiguration();
                mcache_config.Servers.Add(new IPEndPoint(IPAddress.Parse(mcache_ip), mcache_port));
                mcache_config.Protocol = MemcachedProtocol.Text;
                mcache_client = new Enyim.Caching.MemcachedClient(mcache_config);

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
            catch (Exception error) { MessageBox.Show("MainForm_Load: " + error.Message); }
        }

        private void get_connection(out SqlCommand cmd, int user_id)
        {
            if (user_id > 0 && user_id <= MAX_USERS_COUNT)
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
                }
            }
            else throw new FormatException("User id must be on range [1.." + MAX_USERS_COUNT.ToString() + "].");
        }

        private String xml_parse(String input, String block_name)
        {
            String temp = new Regex("<" + block_name + ">.*</" + block_name + ">").Match(input).ToString();
            return temp.Substring(block_name.Length + 2, temp.Length - 2*block_name.Length - 5);
        }

        private void cache_parser(String cache)
        {
            userName_textBox.Text = xml_parse(cache, "name");
            userSurname_textBox.Text = xml_parse(cache, "surname");
            userAge_textBox.Text = xml_parse(cache, "age");
            userCity_textBox.Text = xml_parse(cache, "city");

            int size = Convert.ToInt32(xml_parse(cache, "friend_count"));
            friend_list = new int[size];
            for (int i = 0; i < size; i++)
            {
                userFriends_listBox.Items.Add(xml_parse(cache, "friend_name_" + i.ToString()));
                friend_list[i] = Convert.ToInt32(xml_parse(cache, "id_" + i.ToString()));
            }

            userAbout_richTextBox.Text = xml_parse(cache, "about");
        }

        private void select_info_from_DB(int user_id)
        {
            DataSet data_set;
            SqlCommand cmd;
            SqlDataReader data_reader;
            SqlDataAdapter data_adapter;

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
                String user_info =
                     "<name>" + userName_textBox.Text + "</name>\n" +
                     "<surname>" + userSurname_textBox.Text + "</surname>\n" +
                     "<age>" + userAge_textBox.Text + "</age>\n" +
                     "<city>" + userCity_textBox.Text + "</city>\n" +
                     "<friend_count>" + userFriends_listBox.Items.Count + "</friend_count>";
                for (int i = 0; i < userFriends_listBox.Items.Count; i++)
                    user_info += "\n<friend_name_" + i.ToString() + ">" + userFriends_listBox.Items[i] + "</friend_name_" + i.ToString() + ">\n<id_" + i.ToString() + ">" + friend_list[i] + "</id_" + i.ToString() + ">";
                user_info += "\n<about>" + userAbout_richTextBox.Text + "</about>";

                mcache_client.Store(StoreMode.Set, "user_" + user_id.ToString(), user_info);
            }
            else MessageBox.Show("Запись не найдена!");
        }

        private void get_button_Click(object sender, EventArgs e)
        {
            get_user_info();
        }

        private void get_user_info()
        {
            int user_id = 0;
            try
            {
                userFriends_listBox.Items.Clear();
                user_id = Convert.ToInt32(userid_textBox.Text.ToString());

                object cache_value;

                timer.Start();
                if (try_get_info_from_mcache(user_id, out cache_value))
                {
                    cache_parser(Convert.ToString(cache_value));
                    timer.Stop();
                }
                else
                {
                    timer.Stop();
                    timer.Start();
                    select_info_from_DB(user_id);
                    timer.Stop();
                }
                time_label.Text = "Runtime: " + timer.ElapsedMilliseconds.ToString() + "ms";
                timer.Reset();
            }
            catch (Exception error)
            {
                MessageBox.Show(error.Message);
            }
        }

        private bool try_get_info_from_mcache(int user_id, out object cache_value)
        {
            return mcache_client.TryGet("user_" + user_id.ToString(), out cache_value);
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
