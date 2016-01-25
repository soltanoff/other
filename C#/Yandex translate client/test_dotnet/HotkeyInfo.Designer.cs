namespace Translator
{
    partial class HotkeyInfo
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(HotkeyInfo));
            this.Hotkey_info_label = new System.Windows.Forms.Label();
            this.label_starinfo = new System.Windows.Forms.Label();
            this.pictureBox_yatranslate_mini = new System.Windows.Forms.PictureBox();
            this.hotkey_checkBox = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_yatranslate_mini)).BeginInit();
            this.SuspendLayout();
            // 
            // Hotkey_info_label
            // 
            this.Hotkey_info_label.AutoSize = true;
            this.Hotkey_info_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.Hotkey_info_label.Location = new System.Drawing.Point(12, 9);
            this.Hotkey_info_label.Name = "Hotkey_info_label";
            this.Hotkey_info_label.Size = new System.Drawing.Size(474, 65);
            this.Hotkey_info_label.TabIndex = 0;
            this.Hotkey_info_label.Text = resources.GetString("Hotkey_info_label.Text");
            // 
            // label_starinfo
            // 
            this.label_starinfo.AutoSize = true;
            this.label_starinfo.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label_starinfo.Location = new System.Drawing.Point(12, 105);
            this.label_starinfo.Name = "label_starinfo";
            this.label_starinfo.Size = new System.Drawing.Size(346, 13);
            this.label_starinfo.TabIndex = 1;
            this.label_starinfo.Text = "* - могут исполняться при неактивном окне приложения";
            // 
            // pictureBox_yatranslate_mini
            // 
            this.pictureBox_yatranslate_mini.BackgroundImage = global::Translator.Properties.Resources.yandex_translate_mini;
            this.pictureBox_yatranslate_mini.InitialImage = null;
            this.pictureBox_yatranslate_mini.Location = new System.Drawing.Point(442, 68);
            this.pictureBox_yatranslate_mini.Name = "pictureBox_yatranslate_mini";
            this.pictureBox_yatranslate_mini.Size = new System.Drawing.Size(50, 50);
            this.pictureBox_yatranslate_mini.TabIndex = 2;
            this.pictureBox_yatranslate_mini.TabStop = false;
            // 
            // hotkey_checkBox
            // 
            this.hotkey_checkBox.AutoSize = true;
            this.hotkey_checkBox.Location = new System.Drawing.Point(12, 85);
            this.hotkey_checkBox.Name = "hotkey_checkBox";
            this.hotkey_checkBox.Size = new System.Drawing.Size(238, 17);
            this.hotkey_checkBox.TabIndex = 3;
            this.hotkey_checkBox.Text = "Активировать глобальный отлов клавиш*";
            this.hotkey_checkBox.UseVisualStyleBackColor = true;
            // 
            // HotkeyInfo
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(504, 127);
            this.Controls.Add(this.hotkey_checkBox);
            this.Controls.Add(this.pictureBox_yatranslate_mini);
            this.Controls.Add(this.label_starinfo);
            this.Controls.Add(this.Hotkey_info_label);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "HotkeyInfo";
            this.Text = "Hotkey info";
            this.TopMost = true;
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.HotkeyInfo_FormClosing);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_yatranslate_mini)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Hotkey_info_label;
        private System.Windows.Forms.Label label_starinfo;
        private System.Windows.Forms.PictureBox pictureBox_yatranslate_mini;
        public System.Windows.Forms.CheckBox hotkey_checkBox;
    }
}