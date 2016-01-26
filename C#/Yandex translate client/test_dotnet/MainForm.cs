using System;
using System.Net;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;



namespace Translator
{
    public partial class MainForm : Form
    {
        public MainForm() { InitializeComponent(); this.KeyPreview = true; }

        #region Constant, Structure and Exception-class
        /// <summary>
        /// Basic constants, parameters
        /// </summary>
        // ===================================================================================================================
        private const int MAX_AMOUNT_NEXTLINES = 9;
        private const int MAX_LENGTH_TEXT = 258;
        private const int LARGE_FONT_SIZE = 14;
        private const int SMALL_FONT_SIZE = 8;
        private const int RESULT_TEXT_POS = 36;
        private const string PAGE_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=";
        private const string API_KEY = "trnsl.1.1.20160121T075113Z.c7a52a569a61fc9e.dbcafd73421e8d61bd4badc95f778c9a8a3d71e3";
        private const string TEXT_BLOCK = "&text=";
        private const string LANG_BLOCK = "&lang=";
        private string[] Lang_name = { "русский", "английский", "немецкий", "французский", "украинский" };
        private string[] Lang_code = { "ru", "en", "de", "fr", "uk" };
        private const string ENCODE_NAME = "windows-1251";
        // ===================================================================================================================
        private String GetQuery; // GET query from PAGE_URL
        private HotkeyInfo HotkeyInfo_form;
        private bool auto_detec_lang;
        private Font Small_font_richTB;
        private Font Large_font_richTB;
        private bool not_changed_detect_label;
        // ===================================================================================================================
        // Basic Exeption from PAGE_URL
        public class API_Exception : System.Exception
        {
            public string code;
            public API_Exception(string c) { code = c; }
        };
        private void check_API_exception()
        {
            string cur_code = GetQuery.Substring(8, 3);
            if (!(cur_code.Equals("200")))
                throw new API_Exception(cur_code);
        }
        // ===================================================================================================================
        #endregion

        #region Translator code
        /// <summary>
        /// Basic functions for translate any text
        /// </summary>
        // ===================================================================================================================
        private String get_result()
        {
            return GetQuery.Substring(RESULT_TEXT_POS, GetQuery.Length - RESULT_TEXT_POS - 3); // 3 - удаляем 3 последних ненужных символа с результата
        }

        private String get_translate_dir()
        {
            if (Lang_CB_1.SelectedIndex == 5)
            {
                auto_detec_lang = true;
                return Lang_code[Lang_CB_2.SelectedIndex];
            }
            else
                return Lang_code[Lang_CB_1.SelectedIndex] + "-" + Lang_code[Lang_CB_2.SelectedIndex];
        }
        
        private int get_id_lang_code()
        {
            string cur_lcode = GetQuery.Substring(20, 2);
            for (int i = 0; i < Lang_code.Length; i++)
                if (cur_lcode.Equals(Lang_code[i])) return i;
            throw new API_Exception("100");
        }
        // ===================================================================================================================
        public String set_url()
        {
            return PAGE_URL + API_KEY + TEXT_BLOCK + WebUtility.UrlEncode(richTB.Text.Replace("\\n", "\n").Replace("\t", " @1101 ")) + LANG_BLOCK + get_translate_dir();
        }

        public StreamReader get_connect(String Url)
        {
            WebClient Connect = new WebClient();
            Connect.Proxy = new WebProxy();

            Stream UrlStream = Connect.OpenRead(Url);
            return new StreamReader(UrlStream);
        }
        
        public String get_translate()
        {
            auto_detec_lang = false;
            String test = set_url();
            GetQuery = get_connect(set_url()).ReadToEnd();

            check_API_exception();

            if (auto_detec_lang)
            {
                Detect_label.Visible = true;
                not_changed_detect_label = true;
                Lang_CB_1.SelectedIndex = get_id_lang_code();
            }
            return get_result().Replace("\\n", "\n").Replace("@1101", "\t");
        }

        private String translate_text_from_richTB()
        {
            if (richTB.Text.Trim().Length >= 1)
            {
                try
                {
                    return richTBres.Text = get_translate();
                }
                catch (WebException error)
                {
                    MessageBox.Show(error.Message);
                }
                catch (API_Exception except)
                {
                    switch (except.code)
                    {
                        case "100":
                            MessageBox.Show("[API Exception: 100]\nОпределен неинициализированый язык.");
                            break;
                        case "200":
                            MessageBox.Show("[API Exception: 200]\nНеправильный ключ API.");
                            break;
                        case "401":
                            MessageBox.Show("[API Exception: 401]\nКлюч API заблокирован.");
                            break;
                        case "402":
                            MessageBox.Show("[API Exception: 402]\nПревышено суточное ограничение на количество запросов.");
                            break;
                        case "403":
                            MessageBox.Show("[API Exception: 403]\nНеправильный ключ API.");
                            break;
                        case "404":
                            MessageBox.Show("[API Exception: 404]\nПревышено суточное ограничение на объем переведенного текста.");
                            break;
                        case "413":
                            MessageBox.Show("[API Exception: 413]\nПревышен максимально допустимый размер текста.");
                            break;
                        case "422":
                            MessageBox.Show("[API Exception: 422]\nТекст не может быть переведен.");
                            break;
                        case "501":
                            MessageBox.Show("[API Exception: 501]\nЗаданное направление перевода не поддерживается.");
                            break;
                        default:
                            throw;
                    }
                }
                catch
                {
                    MessageBox.Show("Неизвестная ошибка.\nОбратитесь к разработчику.\nhttp://vk.com/id96996256");
                }
            }
            else
            {
                MessageBox.Show("Может введете текст в левую половину? :)");
            }
            return "";
        }
        // ===================================================================================================================                            
        #endregion

        #region HotKey register code
        /// <summary>
        /// WinAPI functions and const
        /// </summary>
        // ===================================================================================================================
        [System.Runtime.InteropServices.DllImport("user32")] 
        public static extern int RegisterHotKey(IntPtr hwnd, int id, int fsModifiers, int vk);
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        static extern bool UnregisterHotKey(IntPtr hWnd, int id);
        //private const int MOD_ALT = 0x1;
        private const int MOD_CONTROL = 0x2;
        //private const int MOD_SHIFT = 0x4;
        //private const int MOD_WIN = 0x8;
        private const int WM_HOTKEY = 0x312;

        protected override void WndProc(ref Message m)
        {
            base.WndProc(ref m);
            if (m.Msg == WM_HOTKEY)
            {
                switch (m.WParam.ToInt32())
                {
                    case 1:
                        if ((richTB.Text = Clipboard.GetText()).Length > 0)
                        {
                            System.Media.SystemSounds.Exclamation.Play();
                            Clipboard.SetText(translate_text_from_richTB());
                        }
                        break;
                    case 2:
                        System.Media.SystemSounds.Asterisk.Play();
                        reverse_lang();
                        break;
                }
            }
        }

        protected override void OnKeyDown(KeyEventArgs e)
        {
            base.OnKeyDown(e);
            if (e.KeyCode == Keys.F1 && e.Control && richTB.Text.Length > 0)
            {
                //System.Media.SystemSounds.Exclamation.Play(); //tuuu dum!
                //System.Media.SystemSounds.Asterisk.Play(); //fruuum!
                //System.Media.SystemSounds.Hand.Play(); //hong!
                System.Media.SystemSounds.Beep.Play(); //teng!
                //System.Media.SystemSounds.Question.Play(); //nothing :(
                translate_text_from_richTB();
                //e.Handled = true;
            }
            else
            {
                if (!HotkeyInfo_form.hotkey_checkBox.Checked)
                {
                    if (e.KeyCode == Keys.F2 && e.Control && (richTB.Text = Clipboard.GetText()).Length > 0)
                    {
                        System.Media.SystemSounds.Exclamation.Play();
                        Clipboard.SetText(translate_text_from_richTB());
                    }
                    else
                    {
                        if (e.KeyCode == Keys.F3 && e.Control && richTB.Text.Length > 0)
                        {
                            System.Media.SystemSounds.Asterisk.Play();
                            reverse_lang();
                        }
                    }
                }
            }
        }
        // ===================================================================================================================                            
        #endregion

        #region FormLoader and FormClosing
        /// <summary>
        /// Basic function of mainform
        /// </summary>
        // ===================================================================================================================
        private void Form1_Load(object sender, EventArgs e)
        {
            Lang_CB_1.Items.AddRange(Lang_name); Lang_CB_1.Items.Add("Определить язык");
            Lang_CB_1.SelectedIndex = Lang_name.Length;

            Lang_CB_2.Items.AddRange(Lang_name);
            Lang_CB_2.SelectedIndex = 1;

            Detect_label.Visible = false;

            HotkeyInfo_form = new HotkeyInfo();
            HotkeyInfo_form.hotkey_checkBox.CheckedChanged += new System.EventHandler(hotkey_CB_CheckedChanged);

            richTB.Font = richTBres.Font = Large_font_richTB = new Font(richTB.Font.FontFamily, LARGE_FONT_SIZE);
            Small_font_richTB = new Font(richTB.Font.FontFamily, SMALL_FONT_SIZE);

            translator_notifyIcon.ShowBalloonTip(5, translator_notifyIcon.Text, "Хэй, я тут! :)", ToolTipIcon.Info);
        }
         
        private void mainform_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            if (HotkeyInfo_form.hotkey_checkBox.Checked)
            {
                UnregisterHotKey(this.Handle, 1);
                UnregisterHotKey(this.Handle, 2);
            }
        }
        // ===================================================================================================================                            
        #endregion

        #region Basic buttons and their funtions
        /// <summary>
        /// Basic buttons on mainform
        /// </summary>
        // ===================================================================================================================
        private void button_url_Click(object sender, EventArgs e)
        {
            translate_text_from_richTB();
        }

        private void reverse_lang()
        {
            if (Lang_CB_1.SelectedIndex == Lang_CB_2.SelectedIndex)
            {
                switch (Lang_CB_1.SelectedIndex)
                {
                    case 0:
                        Lang_CB_2.SelectedIndex++;
                        break;
                    case 1:
                        Lang_CB_2.SelectedIndex--;
                        break;
                    default:
                        break;
                }

            }
            else
            {
                if (Lang_CB_1.SelectedIndex == 5) Lang_CB_1.SelectedIndex = 0;
                int temp = Lang_CB_1.SelectedIndex;
                Lang_CB_1.SelectedIndex = Lang_CB_2.SelectedIndex;
                Lang_CB_2.SelectedIndex = temp;
            }
        }

        private void button_reverse_Click(object sender, EventArgs e)
        {
            reverse_lang();
        }

        private void button_clear_richTB_Click(object sender, EventArgs e)
        {
            richTBres.Text = richTB.Text = "";
        }

        private void button_clipboard_cpy_Click(object sender, EventArgs e)
        {
            Clipboard.SetText(richTBres.Text);
            MessageBox.Show("Перевод скопирован в буфер обмена.");
        }

        private void button_safe_Click(object sender, EventArgs e)
        {
            saveFileD.ShowDialog();
        }

        private void read_file_button_Click(object sender, EventArgs e)
        {
            openFileD.ShowDialog();
        }
        // ===================================================================================================================
        #endregion

        #region KeyBoard emitation of Ctrl+C, Ctrl+V, Ctrl+X
        /// <summary>
        /// WinAPI functions
        /// </summary>
        // ===================================================================================================================
        [System.Runtime.InteropServices.DllImport("user32.dll", SetLastError = true)]
        private static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, int dwExtraInfo);

        private static void SendCtrlhotKey(char key)
        {
            keybd_event(0x11, 0, 0, 0);
            keybd_event((byte)key, 0, 0, 0);
            keybd_event((byte)key, 0, 0x2, 0);
            keybd_event(0x11, 0, 0x2, 0);
        }

        private void copy_ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SendCtrlhotKey('C');
        }

        private void paste_ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SendCtrlhotKey('V');
        }

        private void about_ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            fdToolStripMenuItem1_Click(sender, e);
        }

        private void cut_ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SendCtrlhotKey('X');
        }

        private void copy_RichTBres_ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SendCtrlhotKey('C');
        }

        private void about_RichTBres_ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            fdToolStripMenuItem1_Click(sender, e);
        }
        // ===================================================================================================================
        #endregion

        private void Lang_CB_1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (!not_changed_detect_label)
                Detect_label.Visible = false;
            else
                not_changed_detect_label = !not_changed_detect_label;
        }

        private void fdToolStripMenuItem1_Click(object sender, EventArgs e) // About
        {
            About F = new About();
            F.Show();
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            try
            {
                StreamReader read_file = new StreamReader(openFileD.OpenFile(), Encoding.GetEncoding(ENCODE_NAME));
                richTB.Text = read_file.ReadToEnd();

                read_file.Close();
            }
            catch
            {
                MessageBox.Show("Ошибка открытия файла!");
            }
        }

        private void saveFileD_FileOk(object sender, CancelEventArgs e)
        {
            try
            {
                StreamWriter write_file = new StreamWriter(saveFileD.FileName, false, Encoding.GetEncoding(ENCODE_NAME));
                write_file.Write(richTBres.Text.ToString());

                write_file.Close();
            }
            catch
            {
                MessageBox.Show("Ошибка записи файла!");
            }
        }

        private void richTBres_TextChanged(object sender, EventArgs e)
        {
            if (richTBres.Text.Length > 0)
                button_clipboard_cpy.Enabled = button_safe.Enabled = true;
            else
                button_clipboard_cpy.Enabled = button_safe.Enabled = false;
        }

        private int get_amount_nextlines()
        {
            return (int)(new System.Text.RegularExpressions.Regex("\n").Matches(richTB.Text).Count);
        }

        private void richTB_TextChanged(object sender, EventArgs e)
        {
            if (get_amount_nextlines() > MAX_AMOUNT_NEXTLINES || richTB.Text.Length > MAX_LENGTH_TEXT)
                richTBres.Font = richTB.Font = Small_font_richTB;
            else
                richTBres.Font = richTB.Font = Large_font_richTB;

            if (richTB.Text.Length > 0)
                button_url.Enabled = button_clear.Enabled = true;
            else
                button_url.Enabled = button_clear.Enabled = false;
        }

        private void Hotkey_toolStripMenuItem_Click(object sender, EventArgs e)
        {
            HotkeyInfo_form.Show();
        }

        private void Hotkey_richTBres_ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Hotkey_toolStripMenuItem_Click(sender, e);
        }

        private void Hotkey_richTB_ToolStripMenuItem_Click_1(object sender, EventArgs e)
        {
            Hotkey_toolStripMenuItem_Click(sender, e);
        }

        public void hotkey_CB_CheckedChanged(object sender, EventArgs e)
        {
            if (HotkeyInfo_form.hotkey_checkBox.Checked)
            {
                RegisterHotKey(Handle, 1, MOD_CONTROL, (int)Keys.F2);
                RegisterHotKey(Handle, 2, MOD_CONTROL, (int)Keys.F3);
            }
            else
            {
                UnregisterHotKey(Handle, 1);
                UnregisterHotKey(Handle, 2);
            }
        }
        // ===================================================================================================================
        bool to_minimum = false;

        public void MainForm_MinimumSizeChanged(object sender, EventArgs e)
        {
            if (to_minimum)
            {
                to_minimum = Visible = false;
                translator_notifyIcon.ShowBalloonTip(5, translator_notifyIcon.Text, "Хэй, я тут! :)", ToolTipIcon.Info);
            }
            else
            {
                to_minimum = true;
            }
        }

        private void NI_menuItem_Click(object Sender, EventArgs e)
        {
            Close();
        }

        private void notifyIcon_DoubleClick(object Sender, EventArgs e)
        {
            Show();
            WindowState = FormWindowState.Normal;

            Activate();
        }
    }
}