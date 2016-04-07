<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="index.aspx.cs" Inherits="WebApp_DB_Client.index" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
    <style type="text/css">
        #Text1 {
            width: 30px;
        }
        #form1 {
            width: 1252px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        User id:<asp:TextBox ID="userid_textBox" runat="server"></asp:TextBox>
    </div>
        <br />
        <asp:Button ID="get_buton" runat="server" OnClick="get_buton_Click" Text="Get info" />
        <br />
        <asp:Panel ID="Panel1" runat="server" Height="112px" Width="197px">
            Name:
            <asp:TextBox ID="userName_textBox" runat="server" ReadOnly="True"></asp:TextBox>
            <br />
            Surname:
            <asp:TextBox ID="userSurname_textBox" runat="server" ReadOnly="True"></asp:TextBox>
            <br />
            Age:
            <asp:TextBox ID="userAge_textBox" runat="server" ReadOnly="True"></asp:TextBox>
            <br />
            City:
            <asp:TextBox ID="userCity_textBox" runat="server" ReadOnly="True"></asp:TextBox>
        </asp:Panel>

        <br />
        <br />

        Friend list:<br />
        <asp:ListBox ID="userFriends_listBox" runat="server" AutoPostBack="True" Height="82px" OnSelectedIndexChanged="userFriends_listBox_SelectedIndexChanged" Width="197px"></asp:ListBox>

        <br />
        <br />
        <br />

        About user:<br />
&nbsp;<asp:TextBox ID="userAbout_richTextBox" runat="server" Height="160px" Width="358px"></asp:TextBox>

        <br />
        <br />

        <asp:Label ID="time_label" runat="server" Text="Runtime: "></asp:Label>
    </form>
</body>
</html>
