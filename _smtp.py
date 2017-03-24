#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
here is the doc
'''

from smtplib import *


class proxy(object):

    def __init__(username, password):

    def connect(self):
        # 'this method will try to connet the SMTP server according the current user'
        # HOST = 'smtp.' + self.smtp + '.com'
        # try:
        #     self.mySMTP = SMTP(HOST)
        #     self.mySMTP.login(self.username, self.passwd)
        #     return True
        # #except SMTPConnectError:
        # except Exception as e:
        #     tkMessageBox.showerror('连接错误', '%s' % e)
        #     return
        # self.mySendMail = sendMail(self.master, self.mySMTP, self.username)

    def getSmtpHost(username,):
        #     'this method try to obtian the SMTP HOST according the user account'
        #     firstSplit = self.username.split('@')[1]
        #     self.smtp = firstSplit.split('.')[0]
        # 'my sendemail class'

    def sendMail(self):
        # self.getMailInfo()
        # body = string.join(("From: %s" % self.sender, "To: %s" % self.sendToAdd,
        #                     "Subject: %s" % self.subjectInfo, "", self.sendTextInfo), "\r\n")
        # try:
        #     self.smtp.sendmail(self.sender, [self.sendToAdd], body)
        # except Exception as e:
        #     tkMessageBox.showerr('发送失败', "%s" % e)
        #     return
        # tkMessageBox.showinfo('提示', '邮件已发送成功！')
