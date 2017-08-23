#!/usr/local/anaconda/bin/python2.7
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib


class EmailInfo(object):
    def __init__(self, from_addr, to_addr, smtp_server, passwd):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.plaintext = ""
        self.html = ""
        self.smtp_server = smtp_server
        self.passwd = passwd

    def send(self):
        msg = MIMEMultipart()
        msg['From'] = _format_addr(u'Chaway <%s>' % self.from_addr)
        msg['To'] = _format_addr(u'我 <%s>' % self.to_addr)
        msg['Subject'] = Header(u'最新豆瓣首页', 'utf-8').encode()
        msg.attach(MIMEText(self.plaintext, 'plain', 'utf-8'))
        smtp_port = 465
        server = smtplib.SMTP_SSL(self.smtp_server, smtp_port)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.passwd)
        server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
        server.quit()



def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))
