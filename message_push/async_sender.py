# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： async_sender.py
# 项目描述： 异步发送消息的模块

import asyncio
from typing import Optional, Dict, Any

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
from .config_loader import ConfigLoader


class AsyncSender:
    @staticmethod
    async def send_messages(
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
        tasks = []

        if email_args:
            tasks.append(EmailSender.send_email(**email_args))
        if wechat_args:
            tasks.append(WeChatSender.send_wechat_message(**wechat_args))
        if dingtalk_args:
            tasks.append(DingTalkSender.send_dingtalk_message(**dingtalk_args))
        if bark_args:
            tasks.append(BarkSender.send_bark_message(**bark_args))
        if telegram_args:
            tasks.append(TelegramSender.send_telegram_message(**telegram_args))
        if igot_args:
            tasks.append(IGotSender.send_igot_message(**igot_args))
        if pushplus_args:
            tasks.append(PushPlusSender.send_pushplus_message(**pushplus_args))
        if anpush_args:
            tasks.append(AnpushSender.send_anpush_message(**anpush_args))
        if feishu_args:
            tasks.append(FeishuSender.send_feishu_message(**feishu_args))
        if discord_args:
            tasks.append(DiscordSender.send_discord_message(**discord_args))
        if whatsapp_args:
            tasks.append(WhatsAppSender.send_whatsapp_message(**whatsapp_args))

        await asyncio.gather(*tasks)

    @staticmethod
    async def send_messages_with_config(config_path: str, message: str, title: Optional[str] = None,
                                        url: Optional[str] = None):
        """
        使用配置文件发送消息

        :param config_path: 配置文件路径
        :param message: 消息内容
        :param title: 消息标题（可选）
        :param url: 消息链接（可选）
        """
        config = ConfigLoader.load_config(config_path)
        tasks = []

        if 'email' in config:
            email_config = config['email']
            tasks.append(EmailSender.send_email_with_config(email_config, title or "Message", message))
        if 'wechat' in config:
            wechat_config = config['wechat']
            tasks.append(WeChatSender.send_wechat_message_with_config(wechat_config, message))
        if 'dingtalk' in config:
            dingtalk_config = config['dingtalk']
            tasks.append(DingTalkSender.send_dingtalk_message_with_config(dingtalk_config, message))
        if 'bark' in config:
            bark_config = config['bark']
            tasks.append(BarkSender.send_bark_message_with_config(bark_config, message))
        if 'telegram' in config:
            telegram_config = config['telegram']
            tasks.append(TelegramSender.send_telegram_message_with_config(telegram_config, message))
        if 'igot' in config:
            igot_config = config['igot']
            tasks.append(IGotSender.send_igot_message_with_config(igot_config, message))
        if 'pushplus' in config:
            pushplus_config = config['pushplus']
            tasks.append(PushPlusSender.send_pushplus_message_with_config(pushplus_config, message))
        if 'anpush' in config:
            anpush_config = config['anpush']
            tasks.append(AnpushSender.send_anpush_message_with_config(anpush_config, title or "Message", message, url))
        if 'feishu' in config:
            feishu_config = config['feishu']
            tasks.append(FeishuSender.send_feishu_message_with_config(feishu_config, message))
        if 'discord' in config:
            discord_config = config['discord']
            tasks.append(DiscordSender.send_discord_message_with_config(discord_config, message))
        if 'whatsapp' in config:
            whatsapp_config = config['whatsapp']
            tasks.append(WhatsAppSender.send_whatsapp_message_with_config(whatsapp_config, message))

        await asyncio.gather(*tasks)
