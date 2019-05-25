# SMTP 发邮件
```python
# 纯文本邮件

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '7697****@qq.com'
#pwd为qq邮箱的授权码
pwd = '****kenbb***' ## xh**********bdc
#发件人的邮箱
sender_qq_mail = '7697****@qq.com'
#收件人邮箱
receiver = ['nj499521010@gmail.com','aaronj.9403@gmail.com']

#邮件的正文内容
mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'
#邮件标题
mail_title = 'Aaron的邮件'

#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

# 设置为纯文本邮件
msg = MIMEText(mail_content, "plain", 'utf-8')
# 设置为HTML邮件
msg = MIMEText(mail_content, "html", 'utf-8')

msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()

# =======================

# 带附件的邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '7697****@qq.com'
#pwd为qq邮箱的授权码
pwd = '*****mkenb****' ##
#发件人的邮箱
sender_qq_mail = '7697****@qq.com'
#收件人邮箱
receiver = 'yiibai.com@gmail.com'

#邮件的正文内容
mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"
#邮件标题
mail_title = 'Maxsu的邮件'

#邮件正文内容
msg = MIMEMultipart()
#msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

#邮件正文内容
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

 
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('attach.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="attach.txt"'
msg.attach(att1)
 
# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('yiibai.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="yiibai.txt"'
msg.attach(att2)


#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()

# =========================

# 带图片的邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = '7697****3@qq.com'
#pwd为qq邮箱的授权码
pwd = 'h******mk*****' #
#发件人的邮箱
sender_qq_mail = '7697****3@qq.com'
#收件人邮箱
receiver = ['yiibai.com@gmail.com','h****u@qq.com']

#邮件的正文内容
mail_content = ""
#邮件标题
mail_title = 'Maxsu的邮件'

#邮件正文内容
#msg = MIMEMultipart()
msg = MIMEMultipart('related')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = Header("接收者测试", 'utf-8') ## 接收者的别名

msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)


#邮件正文内容
mail_body = """
 <p>你好，Python 邮件发送测试...</p>
 <p>这是使用python登录qq邮箱发送HTML格式和图片的测试邮件：</p>
 <p><a href='http://www.yiibai.com'>易百教程</a></p>
 <p>图片演示：</p>
 <p>![](cid:send_image)</p>
"""

#msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
msgText = (MIMEText(mail_body, 'html', 'utf-8'))
msgAlternative.attach(msgText)

 
# 指定图片为当前目录
fp = open('my.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
 
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<send_image>')
msg.attach(msgImage)


#ssl登录
smtp = SMTP_SSL(host_server)
#set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
```