import smtplib
import sys
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def smtp_email(sender, receivers, password, smtp_server, port, attachment=None,
               subject="***来自Python接口自动化***"):
    message = MIMEMultipart()
    mail_msg = "<h1>接口测试报告</h1><p>您提交的接口测试已经测试完毕，附件中存放您的测试报告和测试日志.</p><p>"
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    if attachment:
        if isinstance(attachment, list) or isinstance(attachment, tuple):
            for fp in attachment:
                with open(fp, 'r', encoding='utf-8') as f:
                    att = MIMEText(f.read(), 'base64', 'utf-8')
                    att["Content-Type"] = 'application/octet-stream'
                    att["Content-Disposition"] = 'attachment; filename={}'.format(fp.split('/')[-1])
                    message.attach(att)
        else:
            with open(attachment, 'r', encoding='utf-8') as f:
                att = MIMEText(f.read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename={}'.format(attachment.split('/')[-1])
                message.attach(att)
    try:
        smtp_obj = smtplib.SMTP_SSL(smtp_server, port)
        smtp_obj.login(sender, password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    log_fp = '../logs/czb.log'
    path = '/Users/shiyan/Code/Appium_CZB/'
    sys.path.append(path)

    test_dir = '../test_case'
    report_dir = '../reports'

    report_name = report_dir + '/2020-03-13 14_57_13' + ' czb_report.html'
    smtp_email(sender='1002450926@qq.com',
               receivers=['shiyan@czb365.com', 'peiyang@czb365.com', 'wangxueshi@czb365.com'],
               password='insedbpcrkekbefd',
               smtp_server='smtp.qq.com', port=465,
               attachment=[report_name, log_fp])
