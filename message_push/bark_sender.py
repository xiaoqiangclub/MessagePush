# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： bark_sender.py
# 项目描述： 发送Bark消息的模块

import httpx


class BarkSender:
    @staticmethod
    async def send_bark_message(bark_url: str, message: str):
        """
        发送Bark消息

        :param bark_url: Bark推送地址
        :param message: 消息内容
        获取Bark参数：https://github.com/Finb/Bark
        """
        async with httpx.AsyncClient() as client:
            try:
                send_url = f"{bark_url}/{message}"
                response = await client.get(send_url)
                if response.status_code == 200:
                    print("Bark消息发送成功")
                else:
                    print(f"Bark消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"Bark消息发送失败: {e}")

    @staticmethod
    async def send_bark_message_with_config(config: dict, message: str):
        """
        使用配置文件发送Bark消息

        :param config: 配置字典
        :param message: 消息内容
        """
        bark_config = config['bark']
        await BarkSender.send_bark_message(
            bark_url=bark_config['bark_url'],
            message=message
        )
