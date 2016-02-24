namespace Translator
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.button_url = new System.Windows.Forms.Button();
            this.richTB = new System.Windows.Forms.RichTextBox();
            this.contextMS_richTB = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.cut_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.copy_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.paste_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.jToolStripMenuItem = new System.Windows.Forms.ToolStripSeparator();
            this.Hotkey_richTB_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.about_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.richTBres = new System.Windows.Forms.RichTextBox();
            this.contextMS_richTBres = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.copy_RichTBres_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.gToolStripMenuItem = new System.Windows.Forms.ToolStripSeparator();
            this.Hotkey_richTBres_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.about_RichTBres_ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Lang_CB_1 = new System.Windows.Forms.ComboBox();
            this.Lang_CB_2 = new System.Windows.Forms.ComboBox();
            this.button_reverse = new System.Windows.Forms.Button();
            this.button_clear = new System.Windows.Forms.Button();
            this.contextMenu = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.Hotkey_toolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutTranslator = new System.Windows.Forms.ToolStripMenuItem();
            this.Detect_label = new System.Windows.Forms.Label();
            this.openFileD = new System.Windows.Forms.OpenFileDialog();
            this.read_file_button = new System.Windows.Forms.Button();
            this.saveFileD = new System.Windows.Forms.SaveFileDialog();
            this.button_safe = new System.Windows.Forms.Button();
            this.button_clipboard_cpy = new System.Windows.Forms.Button();
            this.NI_menuItem_close = new System.Windows.Forms.MenuItem();
            this.NI_menuItem_hotkey = new System.Windows.Forms.MenuItem();
            this.NI_menuItem_about = new System.Windows.Forms.MenuItem();
            this.NI_contextMenu = new System.Windows.Forms.ContextMenu();
            this.translator_notifyIcon = new System.Windows.Forms.NotifyIcon(this.components);
            this.contextMS_richTB.SuspendLayout();
            this.contextMS_richTBres.SuspendLayout();
            this.contextMenu.SuspendLayout();
            this.SuspendLayout();
            // 
            // button_url
            // 
            this.button_url.AutoSize = true;
            this.button_url.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.button_url.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.button_url.Enabled = false;
            this.button_url.Font = new System.Drawing.Font("Palatino Linotype", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button_url.Location = new System.Drawing.Point(0, 317);
            this.button_url.Name = "button_url";
            this.button_url.Size = new System.Drawing.Size(704, 29);
            this.button_url.TabIndex = 2;
            this.button_url.Text = "Перевести";
            this.button_url.UseVisualStyleBackColor = true;
            this.button_url.Click += new System.EventHandler(this.button_url_Click);
            // 
            // richTB
            // 
            this.richTB.AcceptsTab = true;
            this.richTB.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.richTB.BackColor = System.Drawing.SystemColors.Window;
            this.richTB.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.richTB.ContextMenuStrip = this.contextMS_richTB;
            this.richTB.Font = new System.Drawing.Font("Times New Roman", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.richTB.Location = new System.Drawing.Point(12, 50);
            this.richTB.Name = "richTB";
            this.richTB.Size = new System.Drawing.Size(317, 261);
            this.richTB.TabIndex = 3;
            this.richTB.Text = "";
            this.richTB.TextChanged += new System.EventHandler(this.richTB_TextChanged);
            // 
            // contextMS_richTB
            // 
            this.contextMS_richTB.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cut_ToolStripMenuItem,
            this.copy_ToolStripMenuItem,
            this.paste_ToolStripMenuItem,
            this.jToolStripMenuItem,
            this.Hotkey_richTB_ToolStripMenuItem,
            this.about_ToolStripMenuItem});
            this.contextMS_richTB.Name = "contextMS_richTB";
            this.contextMS_richTB.Size = new System.Drawing.Size(174, 120);
            // 
            // cut_ToolStripMenuItem
            // 
            this.cut_ToolStripMenuItem.Name = "cut_ToolStripMenuItem";
            this.cut_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.cut_ToolStripMenuItem.Text = "Вырезать";
            this.cut_ToolStripMenuItem.Click += new System.EventHandler(this.cut_ToolStripMenuItem_Click);
            // 
            // copy_ToolStripMenuItem
            // 
            this.copy_ToolStripMenuItem.Name = "copy_ToolStripMenuItem";
            this.copy_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.copy_ToolStripMenuItem.Text = "Копировать";
            this.copy_ToolStripMenuItem.Click += new System.EventHandler(this.copy_ToolStripMenuItem_Click);
            // 
            // paste_ToolStripMenuItem
            // 
            this.paste_ToolStripMenuItem.Name = "paste_ToolStripMenuItem";
            this.paste_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.paste_ToolStripMenuItem.Text = "Вставить";
            this.paste_ToolStripMenuItem.Click += new System.EventHandler(this.paste_ToolStripMenuItem_Click);
            // 
            // jToolStripMenuItem
            // 
            this.jToolStripMenuItem.Name = "jToolStripMenuItem";
            this.jToolStripMenuItem.Size = new System.Drawing.Size(170, 6);
            // 
            // Hotkey_richTB_ToolStripMenuItem
            // 
            this.Hotkey_richTB_ToolStripMenuItem.Name = "Hotkey_richTB_ToolStripMenuItem";
            this.Hotkey_richTB_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.Hotkey_richTB_ToolStripMenuItem.Text = "Горячие клавиши";
            this.Hotkey_richTB_ToolStripMenuItem.Click += new System.EventHandler(this.Hotkey_richTB_ToolStripMenuItem_Click_1);
            // 
            // about_ToolStripMenuItem
            // 
            this.about_ToolStripMenuItem.Name = "about_ToolStripMenuItem";
            this.about_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.about_ToolStripMenuItem.Text = "О программе";
            this.about_ToolStripMenuItem.Click += new System.EventHandler(this.about_ToolStripMenuItem_Click);
            // 
            // richTBres
            // 
            this.richTBres.AcceptsTab = true;
            this.richTBres.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.richTBres.BackColor = System.Drawing.SystemColors.Window;
            this.richTBres.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.richTBres.ContextMenuStrip = this.contextMS_richTBres;
            this.richTBres.Font = new System.Drawing.Font("Times New Roman", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.richTBres.Location = new System.Drawing.Point(375, 50);
            this.richTBres.Name = "richTBres";
            this.richTBres.ReadOnly = true;
            this.richTBres.Size = new System.Drawing.Size(317, 261);
            this.richTBres.TabIndex = 4;
            this.richTBres.Text = "";
            this.richTBres.TextChanged += new System.EventHandler(this.richTBres_TextChanged);
            // 
            // contextMS_richTBres
            // 
            this.contextMS_richTBres.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.copy_RichTBres_ToolStripMenuItem,
            this.gToolStripMenuItem,
            this.Hotkey_richTBres_ToolStripMenuItem,
            this.about_RichTBres_ToolStripMenuItem});
            this.contextMS_richTBres.Name = "contextMS_richTBres";
            this.contextMS_richTBres.Size = new System.Drawing.Size(174, 76);
            // 
            // copy_RichTBres_ToolStripMenuItem
            // 
            this.copy_RichTBres_ToolStripMenuItem.Name = "copy_RichTBres_ToolStripMenuItem";
            this.copy_RichTBres_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.copy_RichTBres_ToolStripMenuItem.Text = "Копировать";
            this.copy_RichTBres_ToolStripMenuItem.Click += new System.EventHandler(this.copy_RichTBres_ToolStripMenuItem_Click);
            // 
            // gToolStripMenuItem
            // 
            this.gToolStripMenuItem.Name = "gToolStripMenuItem";
            this.gToolStripMenuItem.Size = new System.Drawing.Size(170, 6);
            // 
            // Hotkey_richTBres_ToolStripMenuItem
            // 
            this.Hotkey_richTBres_ToolStripMenuItem.Name = "Hotkey_richTBres_ToolStripMenuItem";
            this.Hotkey_richTBres_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.Hotkey_richTBres_ToolStripMenuItem.Text = "Горячие клавиши";
            this.Hotkey_richTBres_ToolStripMenuItem.Click += new System.EventHandler(this.Hotkey_richTBres_ToolStripMenuItem_Click);
            // 
            // about_RichTBres_ToolStripMenuItem
            // 
            this.about_RichTBres_ToolStripMenuItem.Name = "about_RichTBres_ToolStripMenuItem";
            this.about_RichTBres_ToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.about_RichTBres_ToolStripMenuItem.Text = "О программе";
            this.about_RichTBres_ToolStripMenuItem.Click += new System.EventHandler(this.about_RichTBres_ToolStripMenuItem_Click);
            // 
            // Lang_CB_1
            // 
            this.Lang_CB_1.Cursor = System.Windows.Forms.Cursors.Hand;
            this.Lang_CB_1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.Lang_CB_1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Lang_CB_1.FormattingEnabled = true;
            this.Lang_CB_1.Location = new System.Drawing.Point(208, 22);
            this.Lang_CB_1.Name = "Lang_CB_1";
            this.Lang_CB_1.Size = new System.Drawing.Size(121, 21);
            this.Lang_CB_1.TabIndex = 5;
            this.Lang_CB_1.Tag = "";
            this.Lang_CB_1.SelectedIndexChanged += new System.EventHandler(this.Lang_CB_1_SelectedIndexChanged);
            // 
            // Lang_CB_2
            // 
            this.Lang_CB_2.Cursor = System.Windows.Forms.Cursors.Hand;
            this.Lang_CB_2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.Lang_CB_2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.Lang_CB_2.FormattingEnabled = true;
            this.Lang_CB_2.Location = new System.Drawing.Point(375, 23);
            this.Lang_CB_2.Name = "Lang_CB_2";
            this.Lang_CB_2.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.Lang_CB_2.Size = new System.Drawing.Size(121, 21);
            this.Lang_CB_2.TabIndex = 6;
            // 
            // button_reverse
            // 
            this.button_reverse.Location = new System.Drawing.Point(335, 22);
            this.button_reverse.Name = "button_reverse";
            this.button_reverse.Size = new System.Drawing.Size(34, 24);
            this.button_reverse.TabIndex = 7;
            this.button_reverse.Text = "<->";
            this.button_reverse.UseVisualStyleBackColor = true;
            this.button_reverse.Click += new System.EventHandler(this.button_reverse_Click);
            // 
            // button_clear
            // 
            this.button_clear.Enabled = false;
            this.button_clear.Font = new System.Drawing.Font("Palatino Linotype", 8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button_clear.ForeColor = System.Drawing.Color.Red;
            this.button_clear.Location = new System.Drawing.Point(12, 21);
            this.button_clear.Name = "button_clear";
            this.button_clear.Size = new System.Drawing.Size(22, 25);
            this.button_clear.TabIndex = 8;
            this.button_clear.Text = "x";
            this.button_clear.TextAlign = System.Drawing.ContentAlignment.TopRight;
            this.button_clear.UseVisualStyleBackColor = true;
            this.button_clear.Click += new System.EventHandler(this.button_clear_richTB_Click);
            // 
            // contextMenu
            // 
            this.contextMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.Hotkey_toolStripMenuItem,
            this.aboutTranslator});
            this.contextMenu.Name = "contextMenuStrip1";
            this.contextMenu.Size = new System.Drawing.Size(174, 48);
            // 
            // Hotkey_toolStripMenuItem
            // 
            this.Hotkey_toolStripMenuItem.Name = "Hotkey_toolStripMenuItem";
            this.Hotkey_toolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.Hotkey_toolStripMenuItem.Text = "Горячие клавиши";
            this.Hotkey_toolStripMenuItem.Click += new System.EventHandler(this.Hotkey_toolStripMenuItem_Click);
            // 
            // aboutTranslator
            // 
            this.aboutTranslator.Name = "aboutTranslator";
            this.aboutTranslator.Size = new System.Drawing.Size(173, 22);
            this.aboutTranslator.Text = "О программе";
            this.aboutTranslator.Click += new System.EventHandler(this.fdToolStripMenuItem1_Click);
            // 
            // Detect_label
            // 
            this.Detect_label.AutoSize = true;
            this.Detect_label.BackColor = System.Drawing.Color.Transparent;
            this.Detect_label.Font = new System.Drawing.Font("Palatino Linotype", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.Detect_label.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.Detect_label.Location = new System.Drawing.Point(143, 3);
            this.Detect_label.Name = "Detect_label";
            this.Detect_label.Size = new System.Drawing.Size(186, 16);
            this.Detect_label.TabIndex = 10;
            this.Detect_label.Text = "Язык определен автоматически:";
            // 
            // openFileD
            // 
            this.openFileD.Filter = "Текстовые файлы (*.txt; *.log; *.cfg )|*.txt;*.log;*.cfg";
            this.openFileD.FileOk += new System.ComponentModel.CancelEventHandler(this.openFileDialog1_FileOk);
            // 
            // read_file_button
            // 
            this.read_file_button.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.read_file_button.Location = new System.Drawing.Point(40, 21);
            this.read_file_button.Name = "read_file_button";
            this.read_file_button.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.read_file_button.Size = new System.Drawing.Size(75, 25);
            this.read_file_button.TabIndex = 11;
            this.read_file_button.Text = "Открыть";
            this.read_file_button.UseVisualStyleBackColor = true;
            this.read_file_button.Click += new System.EventHandler(this.read_file_button_Click);
            // 
            // saveFileD
            // 
            this.saveFileD.DefaultExt = "txt";
            this.saveFileD.Filter = "Текстовые файлы (*.txt; *.log; *.cfg )|*.txt;*.log;*.cfg";
            this.saveFileD.RestoreDirectory = true;
            this.saveFileD.Title = "Сохранить";
            this.saveFileD.FileOk += new System.ComponentModel.CancelEventHandler(this.saveFileD_FileOk);
            // 
            // button_safe
            // 
            this.button_safe.Enabled = false;
            this.button_safe.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button_safe.Location = new System.Drawing.Point(617, 20);
            this.button_safe.Name = "button_safe";
            this.button_safe.Size = new System.Drawing.Size(75, 26);
            this.button_safe.TabIndex = 12;
            this.button_safe.Text = "Сохранить";
            this.button_safe.UseVisualStyleBackColor = true;
            this.button_safe.Click += new System.EventHandler(this.button_safe_Click);
            // 
            // button_clipboard_cpy
            // 
            this.button_clipboard_cpy.Enabled = false;
            this.button_clipboard_cpy.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.button_clipboard_cpy.Location = new System.Drawing.Point(514, 20);
            this.button_clipboard_cpy.Name = "button_clipboard_cpy";
            this.button_clipboard_cpy.Size = new System.Drawing.Size(97, 26);
            this.button_clipboard_cpy.TabIndex = 13;
            this.button_clipboard_cpy.Text = "Копировать всё";
            this.button_clipboard_cpy.UseVisualStyleBackColor = true;
            this.button_clipboard_cpy.Click += new System.EventHandler(this.button_clipboard_cpy_Click);
            // 
            // NI_menuItem_close
            // 
            this.NI_menuItem_close.Index = 2;
            this.NI_menuItem_close.Text = "Закрыть";
            this.NI_menuItem_close.Click += new System.EventHandler(this.NI_menuItem_Click);
            // 
            // NI_menuItem_hotkey
            // 
            this.NI_menuItem_hotkey.Index = 0;
            this.NI_menuItem_hotkey.Text = "Горячие клавиши";
            this.NI_menuItem_hotkey.Click += new System.EventHandler(this.Hotkey_toolStripMenuItem_Click);
            // 
            // NI_menuItem_about
            // 
            this.NI_menuItem_about.Index = 1;
            this.NI_menuItem_about.Text = "О программе";
            this.NI_menuItem_about.Click += new System.EventHandler(this.fdToolStripMenuItem1_Click);
            // 
            // NI_contextMenu
            // 
            this.NI_contextMenu.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.NI_menuItem_hotkey,
            this.NI_menuItem_about,
            this.NI_menuItem_close});
            // 
            // translator_notifyIcon
            // 
            this.translator_notifyIcon.ContextMenu = this.NI_contextMenu;
            this.translator_notifyIcon.Icon = ((System.Drawing.Icon)(resources.GetObject("translator_notifyIcon.Icon")));
            this.translator_notifyIcon.Text = "Translate v1.5.1";
            this.translator_notifyIcon.Visible = true;
            this.translator_notifyIcon.DoubleClick += new System.EventHandler(this.notifyIcon_DoubleClick);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(704, 346);
            this.ContextMenuStrip = this.contextMenu;
            this.Controls.Add(this.button_clipboard_cpy);
            this.Controls.Add(this.button_safe);
            this.Controls.Add(this.read_file_button);
            this.Controls.Add(this.Detect_label);
            this.Controls.Add(this.button_clear);
            this.Controls.Add(this.button_reverse);
            this.Controls.Add(this.Lang_CB_2);
            this.Controls.Add(this.Lang_CB_1);
            this.Controls.Add(this.richTBres);
            this.Controls.Add(this.richTB);
            this.Controls.Add(this.button_url);
            this.DoubleBuffered = true;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Text = "Translator v1.5.1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.mainform_Closing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.contextMS_richTB.ResumeLayout(false);
            this.contextMS_richTBres.ResumeLayout(false);
            this.contextMenu.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button_url;
        private System.Windows.Forms.RichTextBox richTB;
        private System.Windows.Forms.RichTextBox richTBres;
        private System.Windows.Forms.ComboBox Lang_CB_1;
        private System.Windows.Forms.ComboBox Lang_CB_2;
        private System.Windows.Forms.Button button_reverse;
        private System.Windows.Forms.Button button_clear;
        private System.Windows.Forms.ContextMenuStrip contextMenu;
        private System.Windows.Forms.Label Detect_label;
        private System.Windows.Forms.ToolStripMenuItem aboutTranslator;
        private System.Windows.Forms.OpenFileDialog openFileD;
        private System.Windows.Forms.Button read_file_button;
        private System.Windows.Forms.SaveFileDialog saveFileD;
        private System.Windows.Forms.Button button_safe;
        private System.Windows.Forms.Button button_clipboard_cpy;
        private System.Windows.Forms.ContextMenuStrip contextMS_richTB;
        private System.Windows.Forms.ToolStripMenuItem copy_ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem paste_ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem about_ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cut_ToolStripMenuItem;
        private System.Windows.Forms.ContextMenuStrip contextMS_richTBres;
        private System.Windows.Forms.ToolStripMenuItem copy_RichTBres_ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem about_RichTBres_ToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator jToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator gToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem Hotkey_toolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem Hotkey_richTBres_ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem Hotkey_richTB_ToolStripMenuItem;
        private System.Windows.Forms.NotifyIcon translator_notifyIcon;
        private System.Windows.Forms.ContextMenu NI_contextMenu;
        private System.Windows.Forms.MenuItem NI_menuItem_close;
        private System.Windows.Forms.MenuItem NI_menuItem_about;
        private System.Windows.Forms.MenuItem NI_menuItem_hotkey;
    }
}

