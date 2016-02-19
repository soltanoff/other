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
            this.main_menuStrip.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.userinfo_groupBox.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // main_menuStrip
            // 
            this.main_menuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.settingsToolStripMenuItem});
            this.main_menuStrip.Location = new System.Drawing.Point(0, 0);
            this.main_menuStrip.Name = "main_menuStrip";
            this.main_menuStrip.Size = new System.Drawing.Size(538, 24);
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
            this.setToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.setToolStripMenuItem.Text = "4332 Soltanov";
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
            this.label1.Location = new System.Drawing.Point(9, 94);
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
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(538, 328);
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
    }
}

