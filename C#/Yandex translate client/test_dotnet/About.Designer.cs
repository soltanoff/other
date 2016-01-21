namespace test_dotnet
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
            this.pictureB = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureB)).BeginInit();
            this.SuspendLayout();
            // 
            // label_about
            // 
            this.label_about.AutoSize = true;
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
            // pictureB
            // 
            this.pictureB.Image = global::test_dotnet.Properties.Resources.unnamed1;
            this.pictureB.Location = new System.Drawing.Point(374, 82);
            this.pictureB.Name = "pictureB";
            this.pictureB.Size = new System.Drawing.Size(119, 114);
            this.pictureB.TabIndex = 2;
            this.pictureB.TabStop = false;
            // 
            // About
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(504, 208);
            this.Controls.Add(this.pictureB);
            this.Controls.Add(this.linkLabel_vk);
            this.Controls.Add(this.label_about);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "About";
            this.Text = "About";
            this.TopMost = true;
            this.Load += new System.EventHandler(this.About_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureB)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label_about;
        private System.Windows.Forms.LinkLabel linkLabel_vk;
        private System.Windows.Forms.PictureBox pictureB;
    }
}