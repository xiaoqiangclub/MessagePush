# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： pushplus_sender.py
# 项目描述： 发送PushPlus消息的模块

import httpx


class PushPlusSender:
    @staticmethod
    async def send_pushplus_message(token: str, message: str):
        """
        发送PushPlus消息

        :param token: PushPlus Token
        :param message: 消息内容
        获取PushPlus参数：https://www.pushplus.plus/
        """
        async with httpx.AsyncClient() as client:
            try:
                send_url = "http://www.pushplus.plus/send"
                data = {
                    "token": token,
                    "content": message
                }
                response = await client.post(send_url, json=data)
                if response.status_code == 200:
                    print("PushPlus消息发送成功")
                else:
                    print(f"PushPlus消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"PushPlus消息发送失败: {e}")

    @staticmethod
    async def send_pushplus_message_with_config(config: dict, message: str):
        """
        使用配置文件发送PushPlus消息

        :param config: 配置字典
        :param message: 消息内容
        """
        pushplus_config = config['pushplus']
        await PushPlusSender.send_pushplus_message(
            token=pushplus_config['token'],
            message=message
        )
