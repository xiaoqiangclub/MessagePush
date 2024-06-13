# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： email_sender.py
# 项目描述： 发送邮件的模块

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    @staticmethod
    async def send_email(subject: str, body: str, to_email: str, from_email: str, smtp_server: str, smtp_port: int,
                         smtp_user: str, smtp_password: str):
        """
        发送邮件

        :param subject: 邮件主题
        :param body: 邮件内容
        :param to_email: 收件人邮箱
        :param from_email: 发件人邮箱
        :param smtp_server: SMTP服务器地址
        :param smtp_port: SMTP服务器端口
        :param smtp_user: SMTP用户名
        :param smtp_password: SMTP密码
        """
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.close()
            print("邮件发送成功")
        except Exception as e:
            print(f"邮件发送失败: {e}")

    @staticmethod
    async def send_email_with_config(config: dict, subject: str, body: str):
        """
        使用配置文件发送邮件

        :param config: 配置字典
        :param subject: 邮件主题
        :param body: 邮件内容
        """
        email_config = config['email']
        await EmailSender.send_email(
            subject=subject,
            body=body,
            to_email=email_config['to_email'],
            from_email=email_config['from_email'],
            smtp_server=email_config['smtp_server'],
            smtp_port=email_config['smtp_port'],
            smtp_user=email_config['smtp_user'],
            smtp_password=email_config['smtp_password']
        )
