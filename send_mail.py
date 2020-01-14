import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'test5.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.cirno.vip的测试', '1485500330@qq.com', 'cirno_ninth@icloud.com'
    text_content = '欢迎访问www.cirno.vip'
    html_content = '<p>欢迎访问<a href="http://www.cirno.vip">www.cirno.vip</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
