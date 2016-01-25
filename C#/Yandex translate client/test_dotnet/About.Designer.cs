namespace Translator
{
    partial class About
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(About));
            this.label_about = new System.Windows.Forms.Label();
            this.linkLabel_vk = new System.Windows.Forms.LinkLabel();
            this.pictureB_yatrans = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureB_yatrans)).BeginInit();
            this.SuspendLayout();
            // 
            // label_about
            // 
            this.label_about.AutoSize = true;
            this.label_about.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label_about.Location = new System.Drawing.Point(12, 9);
            this.label_about.Name = "label_about";
            this.label_about.Size = new System.Drawing.Size(481, 169);
            this.label_about.TabIndex = 0;
            this.label_about.Text = resources.GetString("label_about.Text");
            // 
            // linkLabel_vk
            // 
            this.linkLabel_vk.AutoSize = true;
            this.linkLabel_vk.Location = new System.Drawing.Point(12, 178);
            this.linkLabel_vk.Name = "linkLabel_vk";
            this.linkLabel_vk.Size = new System.Drawing.Size(134, 13);
            this.linkLabel_vk.TabIndex = 1;
            this.linkLabel_vk.TabStop = true;
            this.linkLabel_vk.Tag = "http://vk.com/write96996256";
            this.linkLabel_vk.Text = "http://vk.com/id96996256";
            this.linkLabel_vk.LinkClicked += new System.Windows.Forms.LinkLabelLinkClickedEventHandler(this.linkLabel1_LinkClicked);
            // 
            // pictureB_yatrans
            // 
            this.pictureB_yatrans.Image = global::Translator.Properties.Resources.yandex_translate;
            this.pictureB_yatrans.Location = new System.Drawing.Point(374, 81);
            this.pictureB_yatrans.Name = "pictureB_yatrans";
            this.pictureB_yatrans.Size = new System.Drawing.Size(119, 110);
            this.pictureB_yatrans.TabIndex = 2;
            this.pictureB_yatrans.TabStop = false;
            // 
            // About
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(504, 200);
            this.Controls.Add(this.pictureB_yatrans);
            this.Controls.Add(this.linkLabel_vk);
            this.Controls.Add(this.label_about);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "About";
            this.Text = "About";
            this.TopMost = true;
            ((System.ComponentModel.ISupportInitialize)(this.pictureB_yatrans)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        #endregion

        private System.Windows.Forms.Label label_about;
        private System.Windows.Forms.LinkLabel linkLabel_vk;
        private System.Windows.Forms.PictureBox pictureB_yatrans;
    }
}