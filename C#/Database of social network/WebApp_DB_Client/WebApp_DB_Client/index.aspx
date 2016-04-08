<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="index.aspx.cs" Inherits="WebApp_DB_Client.index" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>DB WebClient</title>
    <style type="text/css">
        #Text1 {
            width: 30px;
        }
        #form1 {
            width: 1252px;
        }

        .text-style {
            text-align: center;
        }

        .auto-style1 {
        }
        .auto-style3 {
            width: 245px;
        }
        .auto-style4 {
            width: 573px;
        }
        .auto-style5 {
        }
        .auto-style6 {
            width: 152px;
        }
        .auto-style8 {
            width: 502px;
        }
        .auto-style10 {
            width: 109px;
            height: 128px;
        }
        .auto-style11 {
            height: 128px;
            width: 14%;
        }
        .auto-style12 {
            width: 14%;
        }
        .auto-style14 {
            width: 59%;
        }
        .auto-style15 {
            width: 109px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    </div>
        <br />
        <table style="width: 14%;">
            <tr>
                <asp:Label ID="time_label" runat="server" Text="Runtime: "></asp:Label>
            </tr>
            <tr>
                <td>User id:</td>
                <td><asp:TextBox ID="userid_textBox" runat="server" Width="62px"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td colspan="2">
        <asp:Button ID="get_buton" runat="server" OnClick="get_buton_Click" Text="Get info" Width="141px" />
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <asp:CheckBox ID="search_checkBox" runat="server" AutoPostBack="True" OnCheckedChanged="search_checkBox_CheckedChanged" Text="Show search panel" />
                </td>
            </tr>
        </table>


        <table class="text-style">
            <td class="auto-style8">
                <h2>
                    User info
                </h2>
                <table style="width: 64%;">
                    <tr>
                        <td class="auto-style3">
                            <table style="">
                                <tr>
                                    <td>Name:
                    </td>
                                    <td>
                    <asp:TextBox ID="userName_textBox" runat="server" ReadOnly="True" CssClass="text-style"></asp:TextBox>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Surname:
                    </td>
                                    <td>
                    <asp:TextBox ID="userSurname_textBox" runat="server" ReadOnly="True" CssClass="text-style"></asp:TextBox>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Age:</td>
                                    <td>
                    <asp:TextBox ID="userAge_textBox" runat="server" ReadOnly="True" CssClass="text-style"></asp:TextBox>
                                    </td>
                                </tr>
                                <tr>
                                    <td>City:
                    </td>
                                    <td>
                    <asp:TextBox ID="userCity_textBox" runat="server" ReadOnly="True" CssClass="text-style"></asp:TextBox>
                                    </td>
                                </tr>
                            </table>
                        </td>
                        <td class="auto-style4">Friend list:<br />
                <asp:ListBox ID="userFriends_listBox" runat="server" AutoPostBack="True" Height="80px" OnSelectedIndexChanged="userFriends_listBox_SelectedIndexChanged" Width="222px"></asp:ListBox>

                        </td>
                    </tr>
                    <tr>
                        <td class="auto-style1" colspan="2">About user:<br />
        &nbsp;<asp:TextBox ID="userAbout_richTextBox" runat="server" Height="137px" Width="461px" ReadOnly="True" TextMode="MultiLine"></asp:TextBox>

                        </td>
                    </tr>
                </table>
            </td>
            <td>
                <asp:Panel ID="search_panel" runat="server" Height="318px" style="margin-bottom: 0px" Visible="False">
                    <h2>Search panel</h2>
                    <table style="width:42%;">
                        <tr>
                            <td class="auto-style12">Name: </td>
                            <td class="auto-style15">
                                <asp:TextBox ID="searchName_textBox" runat="server" CssClass="text-style"></asp:TextBox>
                            </td>
                            <td rowspan="5" class="auto-style14">
                                <asp:ListBox ID="user_listBox" runat="server" AutoPostBack="True" Height="223px" OnSelectedIndexChanged="user_listBox_SelectedIndexChanged" Width="197px"></asp:ListBox>
                            </td>
                        </tr>
                        <tr>
                            <td class="auto-style12">Surname: </td>
                            <td class="auto-style15">
                                <asp:TextBox ID="searchSurname_textBox" runat="server" CssClass="text-style"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <td class="auto-style12">City</td>
                            <td class="auto-style15">
                                <asp:TextBox ID="searchCity_textBox" runat="server" CssClass="text-style"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <td class="auto-style12">About:</td>
                            <td class="auto-style15">
                                <asp:TextBox ID="searchAbout_textBox" runat="server" CssClass="text-style"></asp:TextBox>
                            </td>
                        </tr>
                        <tr>
                            <td class="auto-style11">Age:</td>
                            <td class="auto-style10">
                                <asp:TextBox ID="searchAge_textBox" runat="server" CssClass="text-style"></asp:TextBox>
                                <br />
                                <asp:CheckBox ID="age_range_checkBox" runat="server" AutoPostBack="True" Font-Size="Small" OnCheckedChanged="age_range_checkBox_CheckedChanged" Text="Range of age" />
                                <asp:Panel ID="age_panel" runat="server" Enabled="False">
                                    <table style="margin-top: 0px">
                                        <tr>
                                            <td>from</td>
                                            <td>
                                                <asp:TextBox ID="from_age_textBox" runat="server" Width="63px" CssClass="text-style"></asp:TextBox>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>to</td>
                                            <td>
                                                <asp:TextBox ID="to_age_textBox" runat="server" Width="63px" CssClass="text-style"></asp:TextBox>
                                            </td>
                                        </tr>
                                    </table>
                                </asp:Panel>
                            </td>
                        </tr>
                        <tr>
                            <td class="auto-style5" colspan="3">
                                <asp:Button ID="search_button" runat="server" OnClick="search_button_Click" Text="Let's search" Width="450px" />
                            </td>
                        </tr>
                    </table>
                </asp:Panel>
            </td>
        </table>
    </form>
</body>
</html>
