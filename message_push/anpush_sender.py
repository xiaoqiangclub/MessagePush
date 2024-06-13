# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： anpush_sender.py
# 项目描述： 发送Anpush消息的模块

import httpx


class AnpushSender:
    @staticmethod
    async def send_anpush_message(token: str, title: str, message: str, url: str = None):
        """
        发送Anpush消息

        :param token: Anpush Token
        :param title: 消息标题
        :param message: 消息内容
        :param url: 消息链接（可选）
        获取Anpush参数：https://www.anpush.com/
        """
        async with httpx.AsyncClient() as client:
            try:
                send_url = "https://api.anpush.com/send"
                data = {
                    "token": token,
                    "title": title,
                    "content": message,
                    "url": url
                }
                response = await client.post(send_url, json=data)
                if response.status_code == 200:
                    print("Anpush消息发送成功")
                else:
                    print(f"Anpush消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"Anpush消息发送失败: {e}")

    @staticmethod
    async def send_anpush_message_with_config(config: dict, title: str, message: str, url: str = None):
        """
        使用配置文件发送Anpush消息

        :param config: 配置字典
        :param title: 消息标题
        :param message: 消息内容
        :param url: 消息链接（可选）
        """
        anpush_config = config['anpush']
        await AnpushSender.send_anpush_message(
            token=anpush_config['token'],
            title=title,
            message=message,
            url=url
        )
