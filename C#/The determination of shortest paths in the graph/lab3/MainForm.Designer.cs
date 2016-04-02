namespace lab3
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
            this.label1 = new System.Windows.Forms.Label();
            this.variant_textBox = new System.Windows.Forms.TextBox();
            this.user_matrix_dataGridView = new System.Windows.Forms.DataGridView();
            this.prog_D_matrix_dataGridView = new System.Windows.Forms.DataGridView();
            this.ok_button = new System.Windows.Forms.Button();
            this.inc_button = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.prog_matrix_name_label = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.prog_matrix_label = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.other_variant_textBox = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.open_file_button = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.label6 = new System.Windows.Forms.Label();
            this.prog_delta_matrix_dataGridView = new System.Windows.Forms.DataGridView();
            this.label3 = new System.Windows.Forms.Label();
            this.prog_G_matrix_dataGridView = new System.Windows.Forms.DataGridView();
            this.clear_button = new System.Windows.Forms.Button();
            this.matrix_openFileDialog = new System.Windows.Forms.OpenFileDialog();
            ((System.ComponentModel.ISupportInitialize)(this.user_matrix_dataGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.prog_D_matrix_dataGridView)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.prog_delta_matrix_dataGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.prog_G_matrix_dataGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(9, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Вариант:";
            // 
            // variant_textBox
            // 
            this.variant_textBox.Location = new System.Drawing.Point(67, 17);
            this.variant_textBox.Name = "variant_textBox";
            this.variant_textBox.Size = new System.Drawing.Size(21, 20);
            this.variant_textBox.TabIndex = 1;
            this.variant_textBox.TextChanged += new System.EventHandler(this.variant_textBox_TextChanged);
            // 
            // user_matrix_dataGridView
            // 
            this.user_matrix_dataGridView.AllowUserToAddRows = false;
            this.user_matrix_dataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.user_matrix_dataGridView.Location = new System.Drawing.Point(8, 48);
            this.user_matrix_dataGridView.Name = "user_matrix_dataGridView";
            this.user_matrix_dataGridView.Size = new System.Drawing.Size(363, 179);
            this.user_matrix_dataGridView.TabIndex = 2;
            this.user_matrix_dataGridView.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.user_matrix_dataGridView_CellContentClick);
            // 
            // prog_D_matrix_dataGridView
            // 
            this.prog_D_matrix_dataGridView.AllowUserToAddRows = false;
            this.prog_D_matrix_dataGridView.AllowUserToDeleteRows = false;
            this.prog_D_matrix_dataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.prog_D_matrix_dataGridView.Location = new System.Drawing.Point(384, 48);
            this.prog_D_matrix_dataGridView.Name = "prog_D_matrix_dataGridView";
            this.prog_D_matrix_dataGridView.ReadOnly = true;
            this.prog_D_matrix_dataGridView.Size = new System.Drawing.Size(363, 179);
            this.prog_D_matrix_dataGridView.TabIndex = 3;
            // 
            // ok_button
            // 
            this.ok_button.Location = new System.Drawing.Point(215, 15);
            this.ok_button.Name = "ok_button";
            this.ok_button.Size = new System.Drawing.Size(75, 23);
            this.ok_button.TabIndex = 4;
            this.ok_button.Text = "OK";
            this.ok_button.UseVisualStyleBackColor = true;
            this.ok_button.Click += new System.EventHandler(this.ok_button_Click);
            // 
            // inc_button
            // 
            this.inc_button.Location = new System.Drawing.Point(384, 15);
            this.inc_button.Name = "inc_button";
            this.inc_button.Size = new System.Drawing.Size(121, 23);
            this.inc_button.TabIndex = 5;
            this.inc_button.Text = "Увеличить степень";
            this.inc_button.UseVisualStyleBackColor = true;
            this.inc_button.Click += new System.EventHandler(this.button1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.Location = new System.Drawing.Point(12, 230);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(80, 18);
            this.label2.TabIndex = 6;
            this.label2.Text = "Матрица L";
            // 
            // prog_matrix_name_label
            // 
            this.prog_matrix_name_label.AutoSize = true;
            this.prog_matrix_name_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.prog_matrix_name_label.Location = new System.Drawing.Point(393, 230);
            this.prog_matrix_name_label.Name = "prog_matrix_name_label";
            this.prog_matrix_name_label.Size = new System.Drawing.Size(80, 18);
            this.prog_matrix_name_label.TabIndex = 7;
            this.prog_matrix_name_label.Text = "Матрица L";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(88, 230);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(13, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "1";
            // 
            // prog_matrix_label
            // 
            this.prog_matrix_label.AutoSize = true;
            this.prog_matrix_label.Location = new System.Drawing.Point(470, 230);
            this.prog_matrix_label.Name = "prog_matrix_label";
            this.prog_matrix_label.Size = new System.Drawing.Size(13, 13);
            this.prog_matrix_label.TabIndex = 9;
            this.prog_matrix_label.Text = "1";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(94, 20);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(71, 13);
            this.label5.TabIndex = 10;
            this.label5.Text = "Подвариант:";
            // 
            // other_variant_textBox
            // 
            this.other_variant_textBox.Location = new System.Drawing.Point(171, 17);
            this.other_variant_textBox.Name = "other_variant_textBox";
            this.other_variant_textBox.ReadOnly = true;
            this.other_variant_textBox.Size = new System.Drawing.Size(21, 20);
            this.other_variant_textBox.TabIndex = 11;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.open_file_button);
            this.groupBox1.Controls.Add(this.prog_D_matrix_dataGridView);
            this.groupBox1.Controls.Add(this.other_variant_textBox);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.variant_textBox);
            this.groupBox1.Controls.Add(this.prog_matrix_label);
            this.groupBox1.Controls.Add(this.user_matrix_dataGridView);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.ok_button);
            this.groupBox1.Controls.Add(this.prog_matrix_name_label);
            this.groupBox1.Controls.Add(this.inc_button);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(755, 254);
            this.groupBox1.TabIndex = 12;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Матричный метод";
            // 
            // open_file_button
            // 
            this.open_file_button.Location = new System.Drawing.Point(296, 15);
            this.open_file_button.Name = "open_file_button";
            this.open_file_button.Size = new System.Drawing.Size(75, 23);
            this.open_file_button.TabIndex = 12;
            this.open_file_button.Text = "Открыть файл";
            this.open_file_button.UseVisualStyleBackColor = true;
            this.open_file_button.Click += new System.EventHandler(this.open_file_button_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.label6);
            this.groupBox2.Controls.Add(this.prog_delta_matrix_dataGridView);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.prog_G_matrix_dataGridView);
            this.groupBox2.Location = new System.Drawing.Point(12, 273);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(755, 225);
            this.groupBox2.TabIndex = 13;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Метод Флойда";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label6.Location = new System.Drawing.Point(393, 201);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(81, 18);
            this.label6.TabIndex = 9;
            this.label6.Text = "Матрица Δ";
            // 
            // prog_delta_matrix_dataGridView
            // 
            this.prog_delta_matrix_dataGridView.AllowUserToAddRows = false;
            this.prog_delta_matrix_dataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.prog_delta_matrix_dataGridView.Location = new System.Drawing.Point(384, 19);
            this.prog_delta_matrix_dataGridView.Name = "prog_delta_matrix_dataGridView";
            this.prog_delta_matrix_dataGridView.Size = new System.Drawing.Size(363, 179);
            this.prog_delta_matrix_dataGridView.TabIndex = 8;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label3.Location = new System.Drawing.Point(12, 201);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(81, 18);
            this.label3.TabIndex = 7;
            this.label3.Text = "Матрица Г";
            // 
            // prog_G_matrix_dataGridView
            // 
            this.prog_G_matrix_dataGridView.AllowUserToAddRows = false;
            this.prog_G_matrix_dataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.prog_G_matrix_dataGridView.Location = new System.Drawing.Point(6, 19);
            this.prog_G_matrix_dataGridView.Name = "prog_G_matrix_dataGridView";
            this.prog_G_matrix_dataGridView.Size = new System.Drawing.Size(363, 179);
            this.prog_G_matrix_dataGridView.TabIndex = 3;
            // 
            // clear_button
            // 
            this.clear_button.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.clear_button.Location = new System.Drawing.Point(0, 508);
            this.clear_button.Name = "clear_button";
            this.clear_button.Size = new System.Drawing.Size(778, 23);
            this.clear_button.TabIndex = 14;
            this.clear_button.Text = "Очистить все";
            this.clear_button.UseVisualStyleBackColor = true;
            this.clear_button.Click += new System.EventHandler(this.clear_button_Click);
            // 
            // matrix_openFileDialog
            // 
            this.matrix_openFileDialog.FileName = "matrix";
            this.matrix_openFileDialog.Filter = "Текстовый документ (*.txt) | *.txt";
            this.matrix_openFileDialog.FileOk += new System.ComponentModel.CancelEventHandler(this.matrix_openFileDialog_FileOk);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(778, 531);
            this.Controls.Add(this.clear_button);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Text = "Определение кротчайших путей графа";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.user_matrix_dataGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.prog_D_matrix_dataGridView)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.prog_delta_matrix_dataGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.prog_G_matrix_dataGridView)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox variant_textBox;
        private System.Windows.Forms.DataGridView user_matrix_dataGridView;
        private System.Windows.Forms.DataGridView prog_D_matrix_dataGridView;
        private System.Windows.Forms.Button ok_button;
        private System.Windows.Forms.Button inc_button;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label prog_matrix_name_label;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label prog_matrix_label;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox other_variant_textBox;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.DataGridView prog_delta_matrix_dataGridView;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.DataGridView prog_G_matrix_dataGridView;
        private System.Windows.Forms.Button clear_button;
        private System.Windows.Forms.Button open_file_button;
        private System.Windows.Forms.OpenFileDialog matrix_openFileDialog;
    }
}

