<div align="center">
<a href="https://xiaoqiangclub.51vip.biz/" alt="logo" ><img src="https://gitee.com/xiaoqiangclub/xiaoqiangapps/raw/master/logo/message_push_mini.jpeg"/></a>


🚀 多平台消息推送工具 🚀

[![GitHub license](https://img.shields.io/github/license/xiaoqiangclub/MessagePush?style=flat-square)](LICENSE)
[![PyPI v](https://img.shields.io/pypi/v/MessagePush?style=flat-square&color=%23a8e6cf)](https://pypi.org/project/MessagePush/)
[![PyPI wheel](https://img.shields.io/pypi/wheel/MessagePush?style=flat-square&color=%23dcedc1)](https://pypi.org/project/MessagePush/#files)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/MessagePush?color=%23ffaaa5&style=flat-square)](https://pypi.org/project/MessagePush/)
<br>
</div>


> MessagePush 是一个用于通过多个平台异步和同步推送消息的 Python 模块。它支持通过配置文件或直接调用接口发送消息。

## 支持的平台

✅ [邮件](https://support.google.com/mail/answer/7126229?hl=zh-Hans)

✅ [微信](https://work.weixin.qq.com/api/doc/90000/90135/91039)

✅ [钉钉](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)

✅ [Bark](https://github.com/Finb/Bark)

✅ [Telegram](https://core.telegram.org/bots/api)

✅ [IGot](https://push.hellyw.com/)

✅ [PushPlus](https://www.pushplus.plus/doc/guide/api.html)

✅ [Anpush](https://anpush.com/doc)

✅ [飞书](https://open.feishu.cn/document/server-docs/im-v1/message/create?appId=cli_a6e3f9e3b95a100b)

✅ [Discord](https://discord.com/developers/docs/intro)

✅ [WhatsApp](https://developers.facebook.com/docs/whatsapp)

## 安装

```bash
pip install MessagePush
```

## 使用方法

MessagePush 支持同步和异步的调用方式。您可以根据需要选择适合的方式进行消息发送。

### 1. 同步发送消息

您可以通过 `Sender` 类的同步方法发送消息到多个平台。

#### 发送邮件

```python
from message_push import Sender


def send_email():
    Sender.email(
        subject="测试邮件",
        body="这是一封测试邮件",
        to_email="example@example.com",
        from_email="your_email@example.com",
        smtp_server="smtp.example.com",
        smtp_port=587,
        smtp_user="your_email@example.com",
        smtp_password="your_password"
    )


send_email()
```

#### 发送微信消息

```python
from message_push import Sender


def send_wechat_message():
    Sender.wechat(
        wechat_corp_id="your_corp_id",
        wechat_corp_secret="your_corp_secret",
        wechat_agent_id=1000002,
        message="这是一条测试微信消息"
    )


send_wechat_message()
```

#### 发送钉钉消息

```python
from message_push import Sender


def send_dingtalk_message():
    Sender.dingtalk(
        webhook_url="https://oapi.dingtalk.com/robot/send?access_token=your_access_token",
        message="这是一条测试钉钉消息",
        secret="your_secret"  # 可选
    )


send_dingtalk_message()
```

### 2. 异步发送消息

您可以通过 `Sender` 类的异步方法发送消息到多个平台。

#### 发送邮件

```python
import asyncio
from message_push import Sender


async def send_email():
    await Sender.email_async(
        subject="测试邮件",
        body="这是一封测试邮件",
        to_email="example@example.com",
        from_email="your_email@example.com",
        smtp_server="smtp.example.com",
        smtp_port=587,
        smtp_user="your_email@example.com",
        smtp_password="your_password"
    )


asyncio.run(send_email())
```

#### 发送微信消息

```python
import asyncio
from message_push import Sender


async def send_wechat_message():
    await Sender.wechat_async(
        wechat_corp_id="your_corp_id",
        wechat_corp_secret="your_corp_secret",
        wechat_agent_id=1000002,
        message="这是一条测试微信消息"
    )


asyncio.run(send_wechat_message())
```

#### 发送钉钉消息

```python
import asyncio
from message_push import Sender


async def send_dingtalk_message():
    await Sender.dingtalk_async(
        webhook_url="https://oapi.dingtalk.com/robot/send?access_token=your_access_token",
        message="这是一条测试钉钉消息",
        secret="your_secret"  # 可选
    )


asyncio.run(send_dingtalk_message())
```

### 3. 使用配置文件发送消息

您可以通过 `Sender` 类的同步或异步方法使用配置文件发送消息到多个平台。

#### 同步方式

```python
from message_push import Sender


def send_messages_with_config():
    Sender.send_messages_with_config_sync(
        config_path="config.yaml",  # 或者 "config.json"
        message="这是一条测试消息",
        title="测试标题",
        url="https://example.com"
    )


send_messages_with_config()
```

#### 异步方式

```python
import asyncio
from message_push import Sender


async def send_messages_with_config():
    await Sender.send_messages_with_config_async(
        config_path="config.yaml",  # 或者 "config.json"
        message="这是一条测试消息",
        title="测试标题",
        url="https://example.com"
    )


asyncio.run(send_messages_with_config())
```

## 示例配置文件

### YAML 格式

```yaml
email:
  to_email: "example@example.com"
  from_email: "your_email@example.com"
  smtp_server: "smtp.example.com"
  smtp_port: 587
  smtp_user: "your_email@example.com"
  smtp_password: "your_password"

wechat:
  corp_id: "your_corp_id"
  corp_secret: "your_corp_secret"
  agent_id: 1000002
  to_user: "UserID"

dingtalk:
  webhook_url: "https://oapi.dingtalk.com/robot/send?access_token=your_access_token"
  secret: "your_secret"  # 可选

bark:
  bark_url: "https://api.day.app/your_bark_key"

telegram:
  bot_token: "your_bot_token"
  chat_id: "your_chat_id"

igot:
  igot_key: "your_igot_key"

pushplus:
  token: "your_pushplus_token"

anpush:
  token: "your_anpush_token"

feishu:
  webhook_url: "https://open.feishu.cn/open-apis/bot/v2/hook/your_feishu_webhook"

discord:
  webhook_url: "https://discord.com/api/webhooks/your_discord_webhook"

whatsapp:
  api_url: "https://graph.facebook.com/v13.0/your_phone_number_id/messages"
  phone_number: "your_phone_number"
  api_token: "your_api_token"
```

### JSON 格式

```json
{
  "email": {
    "to_email": "example@example.com",
    "from_email": "your_email@example.com",
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_user": "your_email@example.com",
    "smtp_password": "your_password"
  },
  "wechat": {
    "corp_id": "your_corp_id",
    "corp_secret": "your_corp_secret",
    "agent_id": 1000002,
    "to_user": "UserID"
  },
  "dingtalk": {
    "webhook_url": "https://oapi.dingtalk.com/robot/send?access_token=your_access_token",
    "secret": "your_secret"
    #
    可选
  },
  "bark": {
    "bark_url": "https://api.day.app/your_bark_key"
  },
  "telegram": {
    "bot_token": "your_bot_token",
    "chat_id": "your_chat_id"
  },
  "igot": {
    "igot_key": "your_igot_key"
  },
  "pushplus": {
    "token": "your_pushplus_token"
  },
  "anpush": {
    "token": "your_anpush_token"
  },
  "feishu": {
    "webhook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/your_feishu_webhook"
  },
  "discord": {
    "webhook_url": "https://discord.com/api/webhooks/your_discord_webhook"
  },
  "whatsapp": {
    "api_url": "https://graph.facebook.com/v13.0/your_phone_number_id/messages",
    "phone_number": "your_phone_number",
    "api_token": "your_api_token"
  }
}
```

### 捐赠

![支持我](https://gitee.com/xiaoqiangclub/xiaoqiangapps/raw/master/images/xiaoqiangclub_ad.png)