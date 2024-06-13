# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： discord_sender.py
# 项目描述： 发送Discord消息的模块

import httpx


class DiscordSender:
    @staticmethod
    async def send_discord_message(webhook_url: str, message: str):
        """
        发送Discord消息

        :param webhook_url: Discord Webhook地址
        :param message: 消息内容
        获取Discord Webhook参数：https://discord.com/developers/docs/resources/webhook
        """
        async with httpx.AsyncClient() as client:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                data = {
                    "content": message
                }
                response = await client.post(webhook_url, headers=headers, json=data)
                if response.status_code == 204:
                    print("Discord消息发送成功")
                else:
                    print(f"Discord消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"Discord消息发送失败: {e}")

    @staticmethod
    async def send_discord_message_with_config(config: dict, message: str):
        """
        使用配置文件发送Discord消息

        :param config: 配置字典
        :param message: 消息内容
        """
        discord_config = config['discord']
        await DiscordSender.send_discord_message(
            webhook_url=discord_config['webhook_url'],
            message=message
        )
