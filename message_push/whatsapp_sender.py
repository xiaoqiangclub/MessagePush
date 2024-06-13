# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： whatsapp_sender.py
# 项目描述： 发送WhatsApp消息的模块

import httpx


class WhatsAppSender:
    @staticmethod
    async def send_whatsapp_message(api_url: str, phone_number: str, message: str, api_token: str):
        """
        发送WhatsApp消息

        :param api_url: WhatsApp API URL
        :param phone_number: 接收消息的电话号码
        :param message: 消息内容
        :param api_token: API Token
        获取WhatsApp API参数：https://developers.facebook.com/docs/whatsapp/cloud-api
        """
        async with httpx.AsyncClient() as client:
            try:
                headers = {
                    "Authorization": f"Bearer {api_token}",
                    "Content-Type": "application/json"
                }
                data = {
                    "messaging_product": "whatsapp",
                    "to": phone_number,
                    "type": "text",
                    "text": {
                        "body": message
                    }
                }
                response = await client.post(api_url, headers=headers, json=data)
                if response.status_code == 200:
                    print("WhatsApp消息发送成功")
                else:
                    print(f"WhatsApp消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"WhatsApp消息发送失败: {e}")

    @staticmethod
    async def send_whatsapp_message_with_config(config: dict, message: str):
        """
        使用配置文件发送WhatsApp消息

        :param config: 配置字典
        :param message: 消息内容
        """
        whatsapp_config = config['whatsapp']
        await WhatsAppSender.send_whatsapp_message(
            api_url=whatsapp_config['api_url'],
            phone_number=whatsapp_config['phone_number'],
            message=message,
            api_token=whatsapp_config['api_token']
        )
