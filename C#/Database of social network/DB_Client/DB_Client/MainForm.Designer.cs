namespace DB_Client
{
    partial class MainForm
    {
        /// <summary>
        /// Требуется переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Обязательный метод для поддержки конструктора - не изменяйте
        /// содержимое данного метода при помощи редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.main_menuStrip = new System.Windows.Forms.MenuStrip();
            this.settingsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.setToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.userid_label = new System.Windows.Forms.Label();
            this.get_button = new System.Windows.Forms.Button();
            this.userid_textBox = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.userinfo_groupBox = new System.Windows.Forms.GroupBox();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.userAbout_richTextBox = new System.Windows.Forms.RichTextBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.userFriends_listBox = new System.Windows.Forms.ListBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.userCity_textBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.userAge_textBox = new System.Windows.Forms.TextBox();
            this.userSurname_textBox = new System.Windows.Forms.TextBox();
            this.userName_textBox = new System.Windows.Forms.TextBox();
            this.userAge_label = new System.Windows.Forms.Label();
            this.userSurname_label = new System.Windows.Forms.Label();
            this.userName_label = new System.Windows.Forms.Label();
            this.time_label = new System.Windows.Forms.Label();
            this.search_button = new System.Windows.Forms.Button();
            this.search_checkBox = new System.Windows.Forms.CheckBox();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.user_listBox = new System.Windows.Forms.ListBox();
            this.groupBox6 = new System.Windows.Forms.GroupBox();
            this.searchAbout_textBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.searchCity_textBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.searchAge_textBox = new System.Windows.Forms.TextBox();
            this.searchSurname_textBox = new System.Windows.Forms.TextBox();
            this.searchName_textBox = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.age_range_checkBox = new System.Windows.Forms.CheckBox();
            this.age_panel = new System.Windows.Forms.Panel();
            this.to_age_textBox = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.from_age_textBox = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.main_menuStrip.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.userinfo_groupBox.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.groupBox6.SuspendLayout();
            this.age_panel.SuspendLayout();
            this.SuspendLayout();
            // 
            // main_menuStrip
            // 
            this.main_menuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.settingsToolStripMenuItem});
            this.main_menuStrip.Location = new System.Drawing.Point(0, 0);
            this.main_menuStrip.Name = "main_menuStrip";
            this.main_menuStrip.Size = new System.Drawing.Size(910, 24);
            this.main_menuStrip.TabIndex = 1;
            this.main_menuStrip.Text = "main_menuStrip";
            // 
            // settingsToolStripMenuItem
            // 
            this.settingsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.setToolStripMenuItem});
            this.settingsToolStripMenuItem.Name = "settingsToolStripMenuItem";
            this.settingsToolStripMenuItem.Size = new System.Drawing.Size(50, 20);
            this.settingsToolStripMenuItem.Text = "Menu";
            // 
            // setToolStripMenuItem
            // 
            this.setToolStripMenuItem.Name = "setToolStripMenuItem";
            this.setToolStripMenuItem.Size = new System.Drawing.Size(161, 22);
            this.setToolStripMenuItem.Text = "© 4332 Soltanov";
            // 
            // userid_label
            // 
            this.userid_label.AutoSize = true;
            this.userid_label.Location = new System.Drawing.Point(8, 22);
            this.userid_label.Name = "userid_label";
            this.userid_label.Size = new System.Drawing.Size(43, 13);
            this.userid_label.TabIndex = 3;
            this.userid_label.Text = "User id:";
            // 
            // get_button
            // 
            this.get_button.Location = new System.Drawing.Point(11, 45);
            this.get_button.Name = "get_button";
            this.get_button.Size = new System.Drawing.Size(127, 23);
            this.get_button.TabIndex = 4;
            this.get_button.Text = "Get info";
            this.get_button.UseVisualStyleBackColor = true;
            this.get_button.Click += new System.EventHandler(this.get_button_Click);
            // 
            // userid_textBox
            // 
            this.userid_textBox.Location = new System.Drawing.Point(51, 19);
            this.userid_textBox.Name = "userid_textBox";
            this.userid_textBox.Size = new System.Drawing.Size(87, 20);
            this.userid_textBox.TabIndex = 5;
            this.userid_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.get_button);
            this.groupBox1.Controls.Add(this.userid_label);
            this.groupBox1.Controls.Add(this.userid_textBox);
            this.groupBox1.Location = new System.Drawing.Point(12, 27);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(150, 78);
            this.groupBox1.TabIndex = 6;
            this.groupBox1.TabStop = false;
            // 
            // userinfo_groupBox
            // 
            this.userinfo_groupBox.Controls.Add(this.groupBox4);
            this.userinfo_groupBox.Controls.Add(this.groupBox3);
            this.userinfo_groupBox.Controls.Add(this.groupBox2);
            this.userinfo_groupBox.Location = new System.Drawing.Point(168, 27);
            this.userinfo_groupBox.Name = "userinfo_groupBox";
            this.userinfo_groupBox.Size = new System.Drawing.Size(356, 289);
            this.userinfo_groupBox.TabIndex = 7;
            this.userinfo_groupBox.TabStop = false;
            this.userinfo_groupBox.Text = "User information";
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.userAbout_richTextBox);
            this.groupBox4.Location = new System.Drawing.Point(6, 143);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(344, 140);
            this.groupBox4.TabIndex = 2;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "About user";
            // 
            // userAbout_richTextBox
            // 
            this.userAbout_richTextBox.Location = new System.Drawing.Point(6, 12);
            this.userAbout_richTextBox.Name = "userAbout_richTextBox";
            this.userAbout_richTextBox.ReadOnly = true;
            this.userAbout_richTextBox.Size = new System.Drawing.Size(331, 122);
            this.userAbout_richTextBox.TabIndex = 0;
            this.userAbout_richTextBox.Text = "";
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.userFriends_listBox);
            this.groupBox3.Location = new System.Drawing.Point(181, 19);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(169, 118);
            this.groupBox3.TabIndex = 1;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Friends list";
            // 
            // userFriends_listBox
            // 
            this.userFriends_listBox.FormattingEnabled = true;
            this.userFriends_listBox.Location = new System.Drawing.Point(6, 13);
            this.userFriends_listBox.Name = "userFriends_listBox";
            this.userFriends_listBox.Size = new System.Drawing.Size(156, 95);
            this.userFriends_listBox.TabIndex = 1;
            this.userFriends_listBox.SelectedIndexChanged += new System.EventHandler(this.userFriends_listBox_SelectedIndexChanged);
            this.userFriends_listBox.DoubleClick += new System.EventHandler(this.userFriends_listBox_DoubleClick);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.userCity_textBox);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Controls.Add(this.userAge_textBox);
            this.groupBox2.Controls.Add(this.userSurname_textBox);
            this.groupBox2.Controls.Add(this.userName_textBox);
            this.groupBox2.Controls.Add(this.userAge_label);
            this.groupBox2.Controls.Add(this.userSurname_label);
            this.groupBox2.Controls.Add(this.userName_label);
            this.groupBox2.Location = new System.Drawing.Point(6, 19);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(169, 118);
            this.groupBox2.TabIndex = 0;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Main info";
            // 
            // userCity_textBox
            // 
            this.userCity_textBox.Location = new System.Drawing.Point(62, 91);
            this.userCity_textBox.Name = "userCity_textBox";
            this.userCity_textBox.ReadOnly = true;
            this.userCity_textBox.Size = new System.Drawing.Size(100, 20);
            this.userCity_textBox.TabIndex = 6;
            this.userCity_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(7, 94);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(27, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "City:";
            // 
            // userAge_textBox
            // 
            this.userAge_textBox.Location = new System.Drawing.Point(62, 68);
            this.userAge_textBox.Name = "userAge_textBox";
            this.userAge_textBox.ReadOnly = true;
            this.userAge_textBox.Size = new System.Drawing.Size(100, 20);
            this.userAge_textBox.TabIndex = 5;
            this.userAge_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // userSurname_textBox
            // 
            this.userSurname_textBox.Location = new System.Drawing.Point(62, 43);
            this.userSurname_textBox.Name = "userSurname_textBox";
            this.userSurname_textBox.ReadOnly = true;
            this.userSurname_textBox.Size = new System.Drawing.Size(100, 20);
            this.userSurname_textBox.TabIndex = 4;
            this.userSurname_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // userName_textBox
            // 
            this.userName_textBox.Location = new System.Drawing.Point(62, 17);
            this.userName_textBox.Name = "userName_textBox";
            this.userName_textBox.ReadOnly = true;
            this.userName_textBox.Size = new System.Drawing.Size(100, 20);
            this.userName_textBox.TabIndex = 3;
            this.userName_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // userAge_label
            // 
            this.userAge_label.AutoSize = true;
            this.userAge_label.Location = new System.Drawing.Point(7, 71);
            this.userAge_label.Name = "userAge_label";
            this.userAge_label.Size = new System.Drawing.Size(29, 13);
            this.userAge_label.TabIndex = 2;
            this.userAge_label.Text = "Age:";
            // 
            // userSurname_label
            // 
            this.userSurname_label.AutoSize = true;
            this.userSurname_label.Location = new System.Drawing.Point(7, 46);
            this.userSurname_label.Name = "userSurname_label";
            this.userSurname_label.Size = new System.Drawing.Size(52, 13);
            this.userSurname_label.TabIndex = 1;
            this.userSurname_label.Text = "Surname:";
            // 
            // userName_label
            // 
            this.userName_label.AutoSize = true;
            this.userName_label.Location = new System.Drawing.Point(7, 20);
            this.userName_label.Name = "userName_label";
            this.userName_label.Size = new System.Drawing.Size(38, 13);
            this.userName_label.TabIndex = 0;
            this.userName_label.Text = "Name:";
            // 
            // time_label
            // 
            this.time_label.AutoSize = true;
            this.time_label.Location = new System.Drawing.Point(9, 303);
            this.time_label.Name = "time_label";
            this.time_label.Size = new System.Drawing.Size(71, 13);
            this.time_label.TabIndex = 8;
            this.time_label.Text = "Runtime: 0ms";
            // 
            // search_button
            // 
            this.search_button.Location = new System.Drawing.Point(6, 244);
            this.search_button.Name = "search_button";
            this.search_button.Size = new System.Drawing.Size(344, 23);
            this.search_button.TabIndex = 9;
            this.search_button.Text = "Let\'s search";
            this.search_button.UseVisualStyleBackColor = true;
            this.search_button.Click += new System.EventHandler(this.search_button_Click);
            // 
            // search_checkBox
            // 
            this.search_checkBox.AutoSize = true;
            this.search_checkBox.Location = new System.Drawing.Point(12, 107);
            this.search_checkBox.Name = "search_checkBox";
            this.search_checkBox.Size = new System.Drawing.Size(117, 17);
            this.search_checkBox.TabIndex = 10;
            this.search_checkBox.Text = "Show search panel";
            this.search_checkBox.UseVisualStyleBackColor = true;
            this.search_checkBox.CheckedChanged += new System.EventHandler(this.search_checkBox_CheckedChanged);
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.user_listBox);
            this.groupBox5.Controls.Add(this.groupBox6);
            this.groupBox5.Controls.Add(this.search_button);
            this.groupBox5.Location = new System.Drawing.Point(530, 33);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(356, 271);
            this.groupBox5.TabIndex = 11;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Search panel";
            // 
            // user_listBox
            // 
            this.user_listBox.FormattingEnabled = true;
            this.user_listBox.Location = new System.Drawing.Point(181, 26);
            this.user_listBox.Name = "user_listBox";
            this.user_listBox.Size = new System.Drawing.Size(169, 212);
            this.user_listBox.TabIndex = 2;
            this.user_listBox.DoubleClick += new System.EventHandler(this.user_listBox_DoubleClick);
            // 
            // groupBox6
            // 
            this.groupBox6.Controls.Add(this.age_panel);
            this.groupBox6.Controls.Add(this.age_range_checkBox);
            this.groupBox6.Controls.Add(this.searchAbout_textBox);
            this.groupBox6.Controls.Add(this.label2);
            this.groupBox6.Controls.Add(this.searchCity_textBox);
            this.groupBox6.Controls.Add(this.label3);
            this.groupBox6.Controls.Add(this.searchAge_textBox);
            this.groupBox6.Controls.Add(this.searchSurname_textBox);
            this.groupBox6.Controls.Add(this.searchName_textBox);
            this.groupBox6.Controls.Add(this.label4);
            this.groupBox6.Controls.Add(this.label5);
            this.groupBox6.Controls.Add(this.label6);
            this.groupBox6.Location = new System.Drawing.Point(6, 19);
            this.groupBox6.Name = "groupBox6";
            this.groupBox6.Size = new System.Drawing.Size(169, 218);
            this.groupBox6.TabIndex = 0;
            this.groupBox6.TabStop = false;
            this.groupBox6.Text = "Main info";
            // 
            // searchAbout_textBox
            // 
            this.searchAbout_textBox.Location = new System.Drawing.Point(62, 68);
            this.searchAbout_textBox.Name = "searchAbout_textBox";
            this.searchAbout_textBox.Size = new System.Drawing.Size(100, 20);
            this.searchAbout_textBox.TabIndex = 9;
            this.searchAbout_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(7, 71);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 13);
            this.label2.TabIndex = 9;
            this.label2.Text = "About:";
            // 
            // searchCity_textBox
            // 
            this.searchCity_textBox.Location = new System.Drawing.Point(62, 91);
            this.searchCity_textBox.Name = "searchCity_textBox";
            this.searchCity_textBox.Size = new System.Drawing.Size(100, 20);
            this.searchCity_textBox.TabIndex = 6;
            this.searchCity_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(7, 94);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(27, 13);
            this.label3.TabIndex = 1;
            this.label3.Text = "City:";
            // 
            // searchAge_textBox
            // 
            this.searchAge_textBox.Location = new System.Drawing.Point(63, 116);
            this.searchAge_textBox.Name = "searchAge_textBox";
            this.searchAge_textBox.Size = new System.Drawing.Size(100, 20);
            this.searchAge_textBox.TabIndex = 5;
            this.searchAge_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // searchSurname_textBox
            // 
            this.searchSurname_textBox.Location = new System.Drawing.Point(62, 43);
            this.searchSurname_textBox.Name = "searchSurname_textBox";
            this.searchSurname_textBox.Size = new System.Drawing.Size(100, 20);
            this.searchSurname_textBox.TabIndex = 4;
            this.searchSurname_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // searchName_textBox
            // 
            this.searchName_textBox.Location = new System.Drawing.Point(62, 17);
            this.searchName_textBox.Name = "searchName_textBox";
            this.searchName_textBox.Size = new System.Drawing.Size(100, 20);
            this.searchName_textBox.TabIndex = 3;
            this.searchName_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(7, 119);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(29, 13);
            this.label4.TabIndex = 2;
            this.label4.Text = "Age:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(7, 46);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(52, 13);
            this.label5.TabIndex = 1;
            this.label5.Text = "Surname:";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(7, 20);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(38, 13);
            this.label6.TabIndex = 0;
            this.label6.Text = "Name:";
            // 
            // age_range_checkBox
            // 
            this.age_range_checkBox.AutoSize = true;
            this.age_range_checkBox.Location = new System.Drawing.Point(62, 142);
            this.age_range_checkBox.Name = "age_range_checkBox";
            this.age_range_checkBox.Size = new System.Drawing.Size(91, 17);
            this.age_range_checkBox.TabIndex = 10;
            this.age_range_checkBox.Text = "Range of age";
            this.age_range_checkBox.UseVisualStyleBackColor = true;
            this.age_range_checkBox.CheckedChanged += new System.EventHandler(this.age_range_checkBox_CheckedChanged);
            // 
            // age_panel
            // 
            this.age_panel.Controls.Add(this.to_age_textBox);
            this.age_panel.Controls.Add(this.label7);
            this.age_panel.Controls.Add(this.from_age_textBox);
            this.age_panel.Controls.Add(this.label8);
            this.age_panel.Enabled = false;
            this.age_panel.Location = new System.Drawing.Point(62, 163);
            this.age_panel.Name = "age_panel";
            this.age_panel.Size = new System.Drawing.Size(106, 49);
            this.age_panel.TabIndex = 11;
            // 
            // to_age_textBox
            // 
            this.to_age_textBox.Location = new System.Drawing.Point(48, 27);
            this.to_age_textBox.Name = "to_age_textBox";
            this.to_age_textBox.Size = new System.Drawing.Size(52, 20);
            this.to_age_textBox.TabIndex = 12;
            this.to_age_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(15, 30);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(16, 13);
            this.label7.TabIndex = 13;
            this.label7.Text = "to";
            // 
            // from_age_textBox
            // 
            this.from_age_textBox.Location = new System.Drawing.Point(48, 2);
            this.from_age_textBox.Name = "from_age_textBox";
            this.from_age_textBox.Size = new System.Drawing.Size(52, 20);
            this.from_age_textBox.TabIndex = 11;
            this.from_age_textBox.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(15, 5);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(27, 13);
            this.label8.TabIndex = 10;
            this.label8.Text = "from";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(910, 328);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.search_checkBox);
            this.Controls.Add(this.time_label);
            this.Controls.Add(this.userinfo_groupBox);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.main_menuStrip);
            this.MainMenuStrip = this.main_menuStrip;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.ShowIcon = false;
            this.Text = "DataBase Client";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.main_menuStrip.ResumeLayout(false);
            this.main_menuStrip.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.userinfo_groupBox.ResumeLayout(false);
            this.groupBox4.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox5.ResumeLayout(false);
            this.groupBox6.ResumeLayout(false);
            this.groupBox6.PerformLayout();
            this.age_panel.ResumeLayout(false);
            this.age_panel.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip main_menuStrip;
        private System.Windows.Forms.ToolStripMenuItem settingsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem setToolStripMenuItem;
        private System.Windows.Forms.Label userid_label;
        private System.Windows.Forms.Button get_button;
        private System.Windows.Forms.TextBox userid_textBox;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox userinfo_groupBox;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TextBox userAge_textBox;
        private System.Windows.Forms.TextBox userSurname_textBox;
        private System.Windows.Forms.TextBox userName_textBox;
        private System.Windows.Forms.Label userAge_label;
        private System.Windows.Forms.Label userSurname_label;
        private System.Windows.Forms.Label userName_label;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.TextBox userCity_textBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RichTextBox userAbout_richTextBox;
        private System.Windows.Forms.ListBox userFriends_listBox;
        private System.Windows.Forms.Label time_label;
        private System.Windows.Forms.Button search_button;
        private System.Windows.Forms.CheckBox search_checkBox;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.ListBox user_listBox;
        private System.Windows.Forms.GroupBox groupBox6;
        private System.Windows.Forms.TextBox searchAbout_textBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox searchCity_textBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox searchAge_textBox;
        private System.Windows.Forms.TextBox searchSurname_textBox;
        private System.Windows.Forms.TextBox searchName_textBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.CheckBox age_range_checkBox;
        private System.Windows.Forms.Panel age_panel;
        private System.Windows.Forms.TextBox to_age_textBox;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox from_age_textBox;
        private System.Windows.Forms.Label label8;
    }
}

