import asyncio
from message_push import AsyncSender


async def test_senders():
    email_args = {
        "subject": "测试邮件",
        "body": "这是一封测试邮件",
        "to_email": "example@example.com",
        "from_email": "your_email@example.com",
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "smtp_user": "your_email@example.com",
        "smtp_password": "your_password"
    }

    wechat_args = {
        "wechat_corp_id": "ww04df62e2c859b771",
        "wechat_corp_secret": "y88b58_-eX7-1LXMW9vIV1L3DJbOQ3-XQC3c1CdQi1I",
        "wechat_agent_id": 1000004,
        # "to_user": "@XiaoqiangClub",
        "message": "这是一条测试微信消息11"
    }

    dd_args = {
        "webhook_url": "https://oapi.dingtalk.com/robot/send?access_token=b5142d02f0a5dee6937f049961cf47bf046a46b9ed4dcd193cf2a6ababfd71bd",
        "message": "你好"

    }
    feishu_args = {
        "webhook_url": "https://open.feishu.cn/open-apis/im/v1/messages",
        "message": "你好"

    }
    push_args = {
        "message": "这是一条测试消息",
        "token":"4a8cc3c64e72457d8a8562005f02f908"
    }

    # await AsyncSender.send_messages(feishu_args=feishu_args)
    await AsyncSender.send_messages(pushplus_args=push_args)


async def test_senders_with_config():
    config_path_yaml = "tests/config.yaml"
    config_path_json = "tests/config.json"
    message = "这是一条测试消息"
    title = "测试标题"
    url = "https://example.com"

    await AsyncSender.send_messages_with_config(config_path_yaml, message, title, url)
    await AsyncSender.send_messages_with_config(config_path_json, message, title, url)


if __name__ == '__main__':
    asyncio.run(test_senders())
    # asyncio.run(test_senders_with_config())