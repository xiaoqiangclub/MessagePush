# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： igot_sender.py
# 项目描述： 发送IGot消息的模块

import httpx


class IGotSender:
    @staticmethod
    async def send_igot_message(igot_key: str, message: str):
        """
        发送IGot消息

        :param igot_key: IGot密钥
        :param message: 消息内容
        获取IGot参数：https://push.hellyw.com/
        """
        async with httpx.AsyncClient() as client:
            try:
                send_url = f"https://push.hellyw.com/{igot_key}"
                data = {
                    "title": "Message",
                    "content": message
                }
                response = await client.post(send_url, json=data)
                if response.status_code == 200:
                    print("IGot消息发送成功")
                else:
                    print(f"IGot消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"IGot消息发送失败: {e}")

    @staticmethod
    async def send_igot_message_with_config(config: dict, message: str):
        """
        使用配置文件发送IGot消息

        :param config: 配置字典
        :param message: 消息内容
        """
        igot_config = config['igot']
        await IGotSender.send_igot_message(
            igot_key=igot_config['igot_key'],
            message=message
        )
