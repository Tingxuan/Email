#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
here is the doc
'''

import smtplib
import doctest
from email.mime.text import MIMEText
from email.utils import formataddr
#import tkMessageBox
#import Tkinter


class proxy(object):
    default_port = {
        "pop3": {False: 110, True: 995},
        "imap4": {False: 143, True: 993},
        "smtp": {False: 25, True: 465},
    }

    def __init__(self, username, password, ssl=True):

        self.username = username
        self.password = password
        self.ssl = ssl
        #self.port = port
        self.smtpServer = None
        self.imapServer = None

    def connect(self):
        ''' this method will try to connet the SMTP server according the current user

        '''

        def getHost(self):
            '''this method will try to obtian the SMTP HOST according the user account
            :exapmle:
            >>> getSmtpHost('neuromancer43@gmail.com')
            'gmail'
            '''

            return self.username.split('@')[1].split('.')[0]

        smtpHost = 'smtp.' + getHost(self) + '.com'
        imapHost = 'imap.' + getHost(self) + '.com'
        try:

            self.smtpServer = smtplib.SMTP(smtpHost, proxy.default_port['smtp']['self.ssl'])
            self.smtpServer.login(self.username, self.password)
            return True

        except Exception as e:
            print('Connecting error!')
            #tkMessageBox.showinfo('Connecting error!', '%s' % e)
            return
        

    def sendMail(self):
        '''this method will try to get the information, then send the mail

        '''
       

        def getUsername(self):
            #username = str(input("Please input the username:"))
            username = 'zhangtingxuan@163.com'
            return self.username

        def getPassword():
            #password = str(input("Please input the password:"))
            password = 'ztx123456'

        def getReceiverName():
            #receiverName = str(input("Please input the receiver's name:"))
            receiverName = '892339906@qq.com'

        def setSubject():
            #MessageSubject = str(input("Please input the subject:"))
            MessageSubject = 'send by python'

        
        def getHost(self):
            '''this method will try to obtian the SMTP HOST according the user account
            :exapmle:
            >>> getSmtpHost('neuromancer43@gmail.com')
            'gmail'
            '''

            return self.username.split('@')[1].split('.')[0]

        def prepare():
            getUsername()
            getPassword()
            getReceiverName()
            setSubject()
            getHost(self)
        
        try:
            Message = MIMEText('Test', 'plain', 'utf-8')
            getUsername(self)
            username = 'zhangtingxuan@163.com'
            print(username)
            smtpHost = 'smtp.' + getHost(self) + '.com'
            print(smtpHost)
            imapHost = 'imap.' + getHost(self) + '.com'
            Message['From'] = formataddr(self.username)
            Message['To'] = formataddr(self.receiverName)
            #Message['Subject'] = formataddr(self.MessageSubject)
            print(smtpHost)
            smtpServer = smtplib.SMTP(smtpHost, proxy.default_port['smtp']['self.ssl'])
            smtpServer.login(self.username, self.password)
            server.sendmail(self.username, [receiverName, ], Message.as_string())
            server.quit()
            
        except Exception as e:
            #print('Sending error!')
            #tkMessageBox.showerror('sendmail error!')
            Message = MIMEText('Test', 'plain', 'utf-8')
            getUsername(self)
            username = 'zhangtingxuan@163.com'
            smtpHost = 'smtp.' + getHost(self) + '.com'
            print(smtpHost)
            imapHost = 'imap.' + getHost(self) + '.com'
            Message['From'] = formataddr('zhangtingxuan@163.com')
            Message['To'] = formataddr('892339906@qq.com')
            #Message['Subject'] = formataddr(self.MessageSubject)
            print(smtpHost)
            server = smtplib.SMTP('smtp.163.com', 25#proxy.default_port['smtp']['self.ssl'])
            server.login('zhangtingxuan@163.com', 'ztx123456)
            server.sendmail('zhangtingxuan', [892339906@qq.com, ], Message.as_string())
            server.quit()
            return


Mail_demo = proxy('zhangtingxuan@163.com', 'ztx123456')
# Mail_demo.connect()
Mail_demo.sendMail()

# body = string.join(("From: %s" % self.sender, "To: %s" % self.sendToAdd,
#                     "Subject: %s" % self.subjectInfo, "", self.sendTextInfo), "\r\n")
# try:
#     self.smtp.sendmail(self.sender, [self.sendToAdd], body)
# except Exception as e:
#     tkMessageBox.showerr('发送失败', "%s" % e)
#     return
# tkMessageBox.showinfo('提示', '邮件已发送成功！')
# pass

# if __name__ == '__main__':
# doctest.testmod(optionflags=1)
