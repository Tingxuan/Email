#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
here is the doc
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def mailFormer(body):
    msg = MIMEText(body["Text"], 'plain', 'utf-8')
    msg["From"] = body["From"]
    msg["To"] = body["To"]
    msg["Subject"] = body["Subject"]
    return msg

