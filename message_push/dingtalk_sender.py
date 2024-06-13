# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： dingtalk_sender.py
# 项目描述： 发送钉钉消息的模块

import httpx


class DingTalkSender:
    @staticmethod
    async def send_dingtalk_message(webhook_url: str, message: str):
        """
        发送钉钉消息

        :param webhook_url: 钉钉机器人Webhook地址
        :param message: 消息内容
        获取钉钉机器人参数：https://developers.dingtalk.com/document/app/custom-robot-access
        """
        async with httpx.AsyncClient() as client:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                data = {
                    "msgtype": "text",
                    "text": {
                        "content": message
                    }
                }
                response = await client.post(webhook_url, headers=headers, json=data)
                result = response.json()
                if result.get('errcode') == 0:
                    print("钉钉消息发送成功")
                else:
                    print(f"钉钉消息发送失败: {result.get('errmsg')}")
            except Exception as e:
                print(f"钉钉消息发送失败: {e}")

    @staticmethod
    async def send_dingtalk_message_with_config(config: dict, message: str):
        """
        使用配置文件发送钉钉消息

        :param config: 配置字典
        :param message: 消息内容
        """
        dingtalk_config = config['dingtalk']
        await DingTalkSender.send_dingtalk_message(
            webhook_url=dingtalk_config['webhook_url'],
            message=message
        )
