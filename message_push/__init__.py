# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： __init__.py
# 项目描述： MessagePush模块初始化文件

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
from .async_sender import AsyncSender
from .config_loader import ConfigLoader

__version__ = '0.0.1'

__all__ = [
    'EmailSender',
    'WeChatSender',
    'DingTalkSender',
    'BarkSender',
    'TelegramSender',
    'IGotSender',
    'PushPlusSender',
    'AnpushSender',
    'FeishuSender',
    'DiscordSender',
    'WhatsAppSender',
    'AsyncSender',
    'ConfigLoader'
]


def print_logo():
    """
    打印程序的logo。
    """
    logo_text = """
                /$$   /$$ /$$                               /$$                                /$$$$$$  /$$           /$$      
               | $$  / $$|__/                              |__/                               /$$__  $$| $$          | $$      
               |  $$/ $$/ /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$  /$$$$$$  /$$$$$$$   /$$$$$$ | $$  \__/| $$ /$$   /$$| $$$$$$$ 
                \  $$$$/ | $$ |____  $$ /$$__  $$ /$$__  $$| $$ |____  $$| $$__  $$ /$$__  $$| $$      | $$| $$  | $$| $$__  $$
                 >$$  $$ | $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$      | $$| $$  | $$| $$  \ $$
                /$$/\  $$| $$ /$$__  $$| $$  | $$| $$  | $$| $$ /$$__  $$| $$  | $$| $$  | $$| $$    $$| $$| $$  | $$| $$  | $$
               | $$  \ $$| $$|  $$$$$$$|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$/| $$$$$$$/
               |__/  |__/ \_______/ \______/  \____  $$|__/ \_______/|__/  |__/ \____  $$ \______/ |__/ \______/ |_______/ 
                                                       | $$                         /$$  \ $$                                  
                                                       | $$                        |  $$$$$$/                                  
                                                       |__/                         \______/                                   
               """
    print(logo_text)


print_logo()
