#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
here is the doc
'''

import smtplib
import doctest


class proxy(object):
    default_port = {
        "pop3": {False: 110, True: 995},
        "imap4": {False: 143, True: 993},
        "smtp": {False: 25, True: 465},
    }

    def __init__(username, password, ssl=True):

        self.username = username
        self.password = password
        self.ssl = ssl
        self.port = port
        self.smtpServer = None
        self.imapServer = None

    def connect(self):
        ''' this method will try to connet the SMTP server according the current user

        '''
        def getHost(self):
            '''this method try to obtian the SMTP HOST according the user account
            :exapmle:
            >>> getSmtpHost('neuromancer43@gmail.com')
            '''
            'gmail'
            return self.username.split('@')[1].split('.')[0]

        smtpHost = 'smtp.' + getHost() + '.com'
        imapHost = 'imap.' + getHost() + '.com'

        try:
            self.smtpServer = smtplib.SMTP(smtpHost, proxy.default_port['smtp']['self.ssl'])
            self.smtpServer.login(self.username, self.passwd)
            return True

        except Exception as e:
            tkMessageBox.showerror('Connecting error!', '%s' % e)
            return
        self.mySendMail = sendMail(self.master, self.mySMTP, self.username)

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
        pass

if __name__ == '__main__':
    doctest.testmod(optionflags=1)
