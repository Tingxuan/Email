#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
here is the doc
'''

import smtplib
import _mailformer
import doctest


class proxy(object):
    '''
    a proxy that connect to a server and send email to service providor
    '''
    default_port = {
        "pop3": {False: 110, True: 995},
        "imap4": {False: 143, True: 993},
        "smtp": {False: 25, True: 465},
    }

    def __init__(self, username, password, ssl=False):
        '''
        Doctest successful~
        '''
        self.username = username
        self.password = password
        self.ssl = ssl
        self.smtpServer = None
        self.imapServer = None
        self.connect()

    def connect(self):
        '''
        this method will try to connet the SMTP server according the current user
        '''
        def getHost():
            '''this method try to obtian the SMTP HOST according the user account
            :exapmle:
            >>> getSmtpHost('neuromancer43@gmail.com')
            '''
            'gmail'
            return self.username.split('@')[1].split('.')[0]

        smtpHost = 'smtp.' + getHost() + '.com'
        imapHost = 'imap.' + getHost() + '.com'

        if self.ssl:
            self.smtpServer = smtplib.SMTP_SSL(smtpHost, proxy.default_port['smtp'][self.ssl])
        else:
            self.smtpServer = smtplib.SMTP(smtpHost, proxy.default_port['smtp'][self.ssl])
            self.smtpServer.set_debuglevel(True)
            self.smtpServer.ehlo()
            self.smtpServer.starttls()
        self.smtpServer.login(self.username, self.password)
        return True

    def sendMail(self, wraper):
        msg = _mailformer.mailFormer(wraper)
        self.smtpServer.sendmail(self.username, [wraper["To"]], msg.as_string())

if __name__ == '__main__':
    doctest.testmod(optionflags=1)
