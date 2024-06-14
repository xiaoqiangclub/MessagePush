# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： feishu_sender.py
# 项目描述： 发送飞书消息的模块

import httpx


class FeishuSender:
    @staticmethod
    async def send_feishu_message(webhook_url: str, message: str):
        """
        发送飞书消息

        :param webhook_url: 飞书机器人Webhook地址
        :param message: 消息内容
        添加机器人文档：https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot
        获取飞书机器人参数：https://open.feishu.cn/document/server-docs/im-v1/message/create
        """
        async with httpx.AsyncClient() as client:
            try:
                headers = {
                    "Content-Type": "application/json"
                }
                data = {
                    "msg_type": "text",
                    "content": {
                        "text": message
                    }
                }
                response = await client.post(webhook_url, headers=headers, json=data)
                if response.status_code == 200:
                    print("飞书消息发送成功")
                else:
                    print(f"飞书消息发送失败: {response.status_code}")
            except Exception as e:
                print(f"飞书消息发送失败: {e}")

    @staticmethod
    async def send_feishu_message_with_config(config: dict, message: str):
        """
        使用配置文件发送飞书消息

        :param config: 配置字典
        :param message: 消息内容
        """
        feishu_config = config['feishu']
        await FeishuSender.send_feishu_message(
            webhook_url=feishu_config['webhook_url'],
            message=message
        )
