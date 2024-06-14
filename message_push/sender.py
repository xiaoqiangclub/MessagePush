# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： sender.py
# 项目描述： 同步和异步发送消息的模块

from .async_sender import AsyncSender
from .email_sender import EmailSender
from .wechat_sender import WeChatSender
from .dingtalk_sender import DingTalkSender
from .bark_sender import BarkSender
from .telegram_sender import TelegramSender
from .igot_sender import IGotSender
from .pushplus_sender import PushPlusSender
from .anpush_sender import AnpushSender
from .feishu_sender import FeishuSender
from .discord_sender import DiscordSender
from .whatsapp_sender import WhatsAppSender
import asyncio
from typing import Optional, Dict, Any


class Sender(AsyncSender):
    @staticmethod
    def send_messages_sync(
            email_args: Optional[Dict[str, Any]] = None,
            wechat_args: Optional[Dict[str, Any]] = None,
            dingtalk_args: Optional[Dict[str, Any]] = None,
            bark_args: Optional[Dict[str, Any]] = None,
            telegram_args: Optional[Dict[str, Any]] = None,
            igot_args: Optional[Dict[str, Any]] = None,
            pushplus_args: Optional[Dict[str, Any]] = None,
            anpush_args: Optional[Dict[str, Any]] = None,
            feishu_args: Optional[Dict[str, Any]] = None,
            discord_args: Optional[Dict[str, Any]] = None,
            whatsapp_args: Optional[Dict[str, Any]] = None
    ):
        """
        同步方式发送消息到多个平台

        :param email_args: 邮件参数
        :param wechat_args: 微信参数
        :param dingtalk_args: 钉钉参数
        :param bark_args: Bark参数
        :param telegram_args: Telegram参数
        :param igot_args: IGot参数
        :param pushplus_args: PushPlus参数
        :param anpush_args: Anpush参数
        :param feishu_args: 飞书参数
        :param discord_args: Discord参数
        :param whatsapp_args: WhatsApp参数
        """
        asyncio.run(AsyncSender.send_messages(
            email_args=email_args,
            wechat_args=wechat_args,
            dingtalk_args=dingtalk_args,
            bark_args=bark_args,
            telegram_args=telegram_args,
            igot_args=igot_args,
            pushplus_args=pushplus_args,
            anpush_args=anpush_args,
            feishu_args=feishu_args,
            discord_args=discord_args,
            whatsapp_args=whatsapp_args
        ))

    @staticmethod
    def send_messages_with_config_sync(config_path: str, message: str, title: Optional[str] = None,
                                       url: Optional[str] = None):
        """
        使用配置文件同步方式发送消息到多个平台

        :param config_path: 配置文件路径
        :param message: 消息内容
        :param title: 消息标题（可选）
        :param url: 消息链接（可选）
        """
        asyncio.run(AsyncSender.send_messages_with_config(config_path, message, title, url))

    @staticmethod
    async def email_async(subject: str, body: str, to_email: str, from_email: str, smtp_server: str, smtp_port: int,
                          smtp_user: str, smtp_password: str):
        """
        异步方式发送邮件

        :param subject: 邮件主题
        :param body: 邮件内容
        :param to_email: 收件人邮箱
        :param from_email: 发件人邮箱
        :param smtp_server: SMTP服务器地址
        :param smtp_port: SMTP服务器端口
        :param smtp_user: SMTP用户名
        :param smtp_password: SMTP密码
        """
        await EmailSender.send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user,
                                     smtp_password)

    @staticmethod
    def email(subject: str, body: str, to_email: str, from_email: str, smtp_server: str, smtp_port: int, smtp_user: str,
              smtp_password: str):
        """
        同步方式发送邮件

        :param subject: 邮件主题
        :param body: 邮件内容
        :param to_email: 收件人邮箱
        :param from_email: 发件人邮箱
        :param smtp_server: SMTP服务器地址
        :param smtp_port: SMTP服务器端口
        :param smtp_user: SMTP用户名
        :param smtp_password: SMTP密码
        """
        asyncio.run(
            Sender.email_async(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password))

    @staticmethod
    async def wechat_async(wechat_corp_id: str, wechat_corp_secret: str, wechat_agent_id: int, message: str,
                           touser: str = "@all", toparty: str = "", totag: str = ""):
        """
        异步方式发送微信消息

        :param wechat_corp_id: 企业微信ID
        :param wechat_corp_secret: 企业微信密钥
        :param wechat_agent_id: 企业微信应用ID
        :param message: 消息内容
        :param touser: 接收消息的用户ID列表，多个用户用 '|' 分隔，默认为 '@all'
        :param toparty: 接收消息的部门ID列表，多个部门用 '|' 分隔
        :param totag: 接收消息的标签ID列表，多个标签用 '|' 分隔
        """
        await WeChatSender.send_wechat_message(wechat_corp_id, wechat_corp_secret, wechat_agent_id, message, touser,
                                               toparty, totag)

    @staticmethod
    def wechat(wechat_corp_id: str, wechat_corp_secret: str, wechat_agent_id: int, message: str, touser: str = "@all",
               toparty: str = "", totag: str = ""):
        """
        同步方式发送微信消息

        :param wechat_corp_id: 企业微信ID
        :param wechat_corp_secret: 企业微信密钥
        :param wechat_agent_id: 企业微信应用ID
        :param message: 消息内容
        :param touser: 接收消息的用户ID列表，多个用户用 '|' 分隔，默认为 '@all'
            :param toparty: 接收消息的部门ID列表，多个部门用 '|' 分隔
            :param totag: 接收消息的标签ID列表，多个标签用 '|' 分隔
            """
        asyncio.run(
            Sender.wechat_async(wechat_corp_id, wechat_corp_secret, wechat_agent_id, message, touser, toparty, totag))

    @staticmethod
    async def dingtalk_async(webhook_url: str, message: str, secret: str = None):
        """
        异步方式发送钉钉消息

        :param webhook_url: 钉钉机器人Webhook地址
        :param message: 消息内容
        :param secret: 加签密钥（可选）
        """
        await DingTalkSender.send_dingtalk_message(webhook_url, message, secret)

    @staticmethod
    def dingtalk(webhook_url: str, message: str, secret: str = None):
        """
        同步方式发送钉钉消息

        :param webhook_url: 钉钉机器人Webhook地址
        :param message: 消息内容
        :param secret: 加签密钥（可选）
        """
        asyncio.run(Sender.dingtalk_async(webhook_url, message, secret))

    @staticmethod
    async def bark_async(bark_url: str, message: str):
        """
        异步方式发送Bark消息

        :param bark_url: Bark推送地址
        :param message: 消息内容
        """
        await BarkSender.send_bark_message(bark_url, message)

    @staticmethod
    def bark(bark_url: str, message: str):
        """
        同步方式发送Bark消息

        :param bark_url: Bark推送地址
        :param message: 消息内容
        """
        asyncio.run(Sender.bark_async(bark_url, message))

    @staticmethod
    async def telegram_async(bot_token: str, chat_id: str, message: str):
        """
        异步方式发送Telegram消息

        :param bot_token: Telegram机器人Token
        :param chat_id: Telegram聊天ID
        :param message: 消息内容
        """
        await TelegramSender.send_telegram_message(bot_token, chat_id, message)

    @staticmethod
    def telegram(bot_token: str, chat_id: str, message: str):
        """
        同步方式发送Telegram消息

        :param bot_token: Telegram机器人Token
        :param chat_id: Telegram聊天ID
        :param message: 消息内容
        """
        asyncio.run(Sender.telegram_async(bot_token, chat_id, message))

    @staticmethod
    async def igot_async(igot_key: str, message: str):
        """
        异步方式发送IGot消息

        :param igot_key: IGot密钥
        :param message: 消息内容
        """
        await IGotSender.send_igot_message(igot_key, message)

    @staticmethod
    def igot(igot_key: str, message: str):
        """
        同步方式发送IGot消息

        :param igot_key: IGot密钥
        :param message: 消息内容
        """
        asyncio.run(Sender.igot_async(igot_key, message))

    @staticmethod
    async def pushplus_async(token: str, message: str):
        """
        异步方式发送PushPlus消息

        :param token: PushPlus Token
        :param message: 消息内容
        """
        await PushPlusSender.send_pushplus_message(token, message)

    @staticmethod
    def pushplus(token: str, message: str):
        """
        同步方式发送PushPlus消息

        :param token: PushPlus Token
        :param message: 消息内容
        """
        asyncio.run(Sender.pushplus_async(token, message))

    @staticmethod
    async def anpush_async(token: str, title: str, message: str, url: str = None):
        """
        异步方式发送Anpush消息

        :param token: Anpush Token
        :param title: 消息标题
        :param message: 消息内容
        :param url: 消息链接（可选）
        """
        await AnpushSender.send_anpush_message(token, title, message, url)

    @staticmethod
    def anpush(token: str, title: str, message: str, url: str = None):
        """
        同步方式发送Anpush消息

        :param token: Anpush Token
        :param title: 消息标题
        :param message: 消息内容
        :param url: 消息链接（可选）
        """
        asyncio.run(Sender.anpush_async(token, title, message, url))

    @staticmethod
    async def feishu_async(webhook_url: str, message: str):
        """
        异步方式发送飞书消息

        :param webhook_url: 飞书机器人Webhook地址
        :param message: 消息内容
        """
        await FeishuSender.send_feishu_message(webhook_url, message)

    @staticmethod
    def feishu(webhook_url: str, message: str):
        """
        同步方式发送飞书消息

        :param webhook_url: 飞书机器人Webhook地址
        :param message: 消息内容
        """
        asyncio.run(Sender.feishu_async(webhook_url, message))

    @staticmethod
    async def discord_async(webhook_url: str, message: str):
        """
        异步方式发送Discord消息

        :param webhook_url: Discord Webhook地址
        :param message: 消息内容
        """
        await DiscordSender.send_discord_message(webhook_url, message)

    @staticmethod
    def discord(webhook_url: str, message: str):
        """
        同步方式发送Discord消息

        :param webhook_url: Discord Webhook地址
        :param message: 消息内容
        """
        asyncio.run(Sender.discord_async(webhook_url, message))

    @staticmethod
    async def whatsapp_async(api_url: str, phone_number: str, message: str, api_token: str):
        """
        异步方式发送WhatsApp消息

        :param api_url: WhatsApp API URL
        :param phone_number: 接收消息的电话号码
        :param message: 消息内容
        :param api_token: API Token
        """
        await WhatsAppSender.send_whatsapp_message(api_url, phone_number, message, api_token)

    @staticmethod
    def whatsapp(api_url: str, phone_number: str, message: str, api_token: str):
        """
        同步方式发送WhatsApp消息

        :param api_url: WhatsApp API URL
        :param phone_number: 接收消息的电话号码
        :param message: 消息内容
        :param api_token: API Token
        """
        asyncio.run(Sender.whatsapp_async(api_url, phone_number, message, api_token))

    @staticmethod
    async def send_messages_async(
            email_args: Optional[Dict[str, Any]] = None,
            wechat_args: Optional[Dict[str, Any]] = None,
            dingtalk_args: Optional[Dict[str, Any]] = None,
            bark_args: Optional[Dict[str, Any]] = None,
            telegram_args: Optional[Dict[str, Any]] = None,
            igot_args: Optional[Dict[str, Any]] = None,
            pushplus_args: Optional[Dict[str, Any]] = None,
            anpush_args: Optional[Dict[str, Any]] = None,
            feishu_args: Optional[Dict[str, Any]] = None,
            discord_args: Optional[Dict[str, Any]] = None,
            whatsapp_args: Optional[Dict[str, Any]] = None
    ):
        """
        异步方式发送消息到多个平台

        :param email_args: 邮件参数
        :param wechat_args: 微信参数
        :param dingtalk_args: 钉钉参数
        :param bark_args: Bark参数
        :param telegram_args: Telegram参数
        :param igot_args: IGot参数
        :param pushplus_args: PushPlus参数
        :param anpush_args: Anpush参数
        :param feishu_args: 飞书参数
        :param discord_args: Discord参数
        :param whatsapp_args: WhatsApp参数
        """
        await AsyncSender.send_messages(
            email_args=email_args,
            wechat_args=wechat_args,
            dingtalk_args=dingtalk_args,
            bark_args=bark_args,
            telegram_args=telegram_args,
            igot_args=igot_args,
            pushplus_args=pushplus_args,
            anpush_args=anpush_args,
            feishu_args=feishu_args,
            discord_args=discord_args,
            whatsapp_args=whatsapp_args
        )

    @staticmethod
    async def send_messages_with_config_async(config_path: str, message: str, title: Optional[str] = None,
                                              url: Optional[str] = None):
        """
        使用配置文件异步方式发送消息到多个平台

        :param config_path: 配置文件路径
        :param message: 消息内容
        :param title: 消息标题（可选）
        :param url: 消息链接（可选）
        """
        await AsyncSender.send_messages_with_config(config_path, message, title, url)
