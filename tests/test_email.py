from email.mime.text import MIMEText

msg = MIMEText('断，如果说生命的旅程从头到尾都是一场决断，你需要判断的仅仅在于，决断是否美好。这次，百度空间忍痛做出决断，将空间内容迁入百度云', 'plain', 'utf-8')

# 输入Email地址和密码
from_addr = '1143123897@qq.com'
password = 'han15903067415'

# 输入收件人地址
to_addr = '1161745215@qq.com'
smtp_server = 'smtp.qq.com'

import smtplib

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
