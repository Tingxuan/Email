#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
The entry of the application
'''
import doctest
import _smtp
import string
from tkinter import *
import tkinter.messagebox as tkMessageBox
import smtplib


class loginPage(object):

    def __init__(self, master, info='Mail Send System'):
        self.master = master
        self.mainlabel = Label(master, text=info, justify=CENTER)
        self.mainlabel.grid(row=0, columnspan=3)

        self.user = Label(master, text='username', borderwidth=2)
        self.user.grid(row=1, sticky=W)

        self.pwd = Label(master, text='password', borderwidth=2)
        self.pwd.grid(row=2, sticky=W)

        self.userEntry = Entry(master)
        self.userEntry.grid(row=1, column=1, columnspan=2)
        self.userEntry.focus_set()

        self.pwdEntry = Entry(master, show='*')
        self.pwdEntry.grid(row=2, column=1, columnspan=2)

        self.loginButton = Button(
            master, text='Login', borderwidth=2, command=self.login)
        self.loginButton.grid(row=3, column=1)

        self.clearButton = Button(
            master, text='Clear', borderwidth=2, command=self.clear)
        self.clearButton.grid(row=3, column=2)

    def login(self):
        username = self.userEntry.get().strip()
        passwd = self.pwdEntry.get().strip()

        if len(username) == 0 or len(passwd) == 0 or '@' not in username:
            tkMessageBox.showwarning('Warning:', 'Invalid email format.')
            self.clear()
            self.userEntry.focus_set()
            return
        try:
            proxy = _smtp.proxy(username, passwd)
            self.mySendMail = mailBoxPage(self.master, proxy, username)

        except smtplib.SMTPConnectError:
            tkMessageBox.showerror(
                'Connection Error', "Can't connect to server!")
        except smtplib.SMTPAuthenticationError as auth:
            tkMessageBox.showerror(
                'Authentication error!', 'Invalid username or password!')
        except smtplib.SMTPHeloError as helo:
            tkMessageBox.showerror('Hello error!', helo)
        except smtplib.SMTPException as e:
            tkMessageBox.showerror('Connection error!', e)

    def clear(self):
        self.userEntry.delete(0, END)
        self.pwdEntry.delete(0, END)


class mailBoxPage(object):
    '''
    app = Tk()
    app.title("Test")
    host = _smtp.proxy('m13618311520@163.com', 'jkl7888927')
    boxPage = mailBoxPage(app, host, host.username)
    '''

    def __init__(self, master, server, sender=''):
        self.proxy = server
        self.sender = sender

        self.sendPage = Toplevel(master)

        self.sendToLabel = Label(self.sendPage, text='send to:')
        self.sendToLabel.grid()
        self.sendToEntry = Entry(self.sendPage)
        self.sendToEntry.grid(row=0, column=1)

        self.subjectLabel = Label(self.sendPage, text='subject:')
        self.subjectLabel.grid(row=1, column=0)
        self.subjectEntry = Entry(self.sendPage)
        self.subjectEntry.grid(row=1, column=1)

        self.fromToLabel = Label(self.sendPage, text='from to:')
        self.fromToLabel.grid(row=2, column=0)
        self.formToAdd = Label(self.sendPage, text=self.sender)
        self.formToAdd.grid(row=2, column=1)

        self.sendText = Text(self.sendPage)
        self.sendText.grid(row=3, column=0, columnspan=2)

        self.sendButton = Button(
            self.sendPage, text='send', command=self.sendMail)
        self.sendButton.grid(row=4, column=0)

        self.newButton = Button(
            self.sendPage, text='new mail', command=self.newMail)
        self.newButton.grid(row=4, column=1)

    def sendMail(self):

        def wraper():
            sendToAdd = self.sendToEntry.get().strip()
            subjectInfo = self.subjectEntry.get().strip()
            sendTextInfo = self.sendText.get(1.0, END)
            body = {"From": self.sender, "To": sendToAdd,
                    "Subject": subjectInfo, "Text": sendTextInfo}
            return body

        tkMessageBox.showinfo('Test', wraper())

        try:
            self.proxy.sendMail(wraper())

        except smtplib.SMTPSenderRefused as e:
            tkMessageBox.showerror('Invalid sender!', e)
            return
        except smtplib.SMTPRecipientsRefused as e:
            tkMessageBox.showerror('Invalid Recipients!', e)
            return
        except Exception as e:
            tkMessageBox.showerror('Failed!', e)
            return
        tkMessageBox.showinfo('Success!', 'Mail has been sent!')

    def newMail(self):
        self.sendToEntry.delete(0, END)
        self.subjectEntry.delete(0, END)
        self.sendText.delete(1.0, END)
        return

    #def logout(self):

if __name__ == '__main__':
    # doctest.testmod(optionflags=1)
    root = Tk()
    root.title('Simple Email')

    myLogin = loginPage(root)

    #root.wait_window(myLogin.mySendMail.sendPage)
    mainloop()
