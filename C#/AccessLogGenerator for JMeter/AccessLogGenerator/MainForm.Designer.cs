namespace AccessLogGenerator
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
            this.url_textBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.getParam_textBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.countVar_textBox = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.gen_progressBar = new System.Windows.Forms.ProgressBar();
            this.SuspendLayout();
            // 
            // url_textBox
            // 
            this.url_textBox.Location = new System.Drawing.Point(130, 6);
            this.url_textBox.Name = "url_textBox";
            this.url_textBox.Size = new System.Drawing.Size(100, 20);
            this.url_textBox.TabIndex = 0;
            this.url_textBox.Text = "index.aspx";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(22, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(102, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "http://somedomain/";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(22, 35);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(82, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "GET parameter:";
            // 
            // getParam_textBox
            // 
            this.getParam_textBox.Location = new System.Drawing.Point(130, 32);
            this.getParam_textBox.Name = "getParam_textBox";
            this.getParam_textBox.Size = new System.Drawing.Size(100, 20);
            this.getParam_textBox.TabIndex = 2;
            this.getParam_textBox.Text = "user_id";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(22, 61);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(83, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Variable counts:";
            // 
            // countVar_textBox
            // 
            this.countVar_textBox.Location = new System.Drawing.Point(130, 58);
            this.countVar_textBox.Name = "countVar_textBox";
            this.countVar_textBox.Size = new System.Drawing.Size(100, 20);
            this.countVar_textBox.TabIndex = 4;
            // 
            // button1
            // 
            this.button1.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.button1.Location = new System.Drawing.Point(0, 121);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(256, 23);
            this.button1.TabIndex = 6;
            this.button1.Text = "Let\'s go!";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(58, 81);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(172, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "* output file name is AccessLog.log";
            // 
            // gen_progressBar
            // 
            this.gen_progressBar.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.gen_progressBar.Location = new System.Drawing.Point(0, 98);
            this.gen_progressBar.Name = "gen_progressBar";
            this.gen_progressBar.Size = new System.Drawing.Size(256, 23);
            this.gen_progressBar.TabIndex = 8;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(256, 144);
            this.Controls.Add(this.gen_progressBar);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.countVar_textBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.getParam_textBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.url_textBox);
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Text = "Access Log Generator";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox url_textBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox getParam_textBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox countVar_textBox;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ProgressBar gen_progressBar;
    }
}

