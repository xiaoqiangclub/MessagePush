# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： telegram_sender.py
# 项目描述： 发送Telegram消息的模块

import httpx


class TelegramSender:
    @staticmethod
    async def send_telegram_message(bot_token: str, chat_id: str, message: str):
        """
        发送Telegram消息

        :param bot_token: Telegram机器人Token
        :param chat_id: Telegram聊天ID
        :param message: 消息内容
        获取Telegram参数：https://core.telegram.org/bots/api
        """
        async with httpx.AsyncClient() as client:
            try:
                send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                data = {
                    "chat_id": chat_id,
                    "text": message
                }
                response = await client.post(send_url, json=data)
                if response.status_code == 200:
                    print("Telegram消息发送成功")
                else:
                    print(f"Telegram消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"Telegram消息发送失败: {e}")

    @staticmethod
    async def send_telegram_message_with_config(config: dict, message: str):
        """
        使用配置文件发送Telegram消息

        :param config: 配置字典
        :param message: 消息内容
        """
        telegram_config = config['telegram']
        await TelegramSender.send_telegram_message(
            bot_token=telegram_config['bot_token'],
            chat_id=telegram_config['chat_id'],
            message=message
        )
