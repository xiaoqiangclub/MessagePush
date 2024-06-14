# MessagePush

`MessagePush` 是一个Python模块，支持通过邮件、微信、钉钉、Bark、Telegram、IGot、PushPlus、Anpush、飞书、Discord和WhatsApp发送消息，并且支持异步方式。

## 安装

```sh
pip install MessagePush
```

## 使用方法

### 发送邮件

```python
import asyncio
from message_push import EmailSender


async def send_email_example():
    await EmailSender.send_email(
        subject="测试邮件",
        body="这是一封测试邮件",
        to_email="example@example.com",
        from_email="your_email@example.com",
        smtp_server="smtp.example.com",
        smtp_port=587,
        smtp_user="your_email@example.com",
        smtp_password="your_password"
    )


asyncio.run(send_email_example())
```

### 发送微信消息

```python
import asyncio
from message_push import WeChatSender


async def send_wechat_example():
    await WeChatSender.send_wechat_message(
        wechat_corp_id="your_corp_id",
        wechat_corp_secret="your_corp_secret",
        wechat_agent_id=1000002,
        to_user="UserID",
        message="这是一条测试微信消息"
    )


asyncio.run(send_wechat_example())
```

### 发送钉钉消息

```python
import asyncio
from message_push import DingTalkSender


async def send_dingtalk_example():
    await DingTalkSender.send_dingtalk_message(
        webhook_url="https://oapi.dingtalk.com/robot/send?access_token=your_access_token",
        message="这是一条测试钉钉消息"
    )


asyncio.run(send_dingtalk_example())
```

### 发送Bark消息

```python
import asyncio
from message_push import BarkSender


async def send_bark_example():
    await BarkSender.send_bark_message(
        bark_url="https://api.day.app/your_bark_key",
        message="这是一条测试Bark消息"
    )


asyncio.run(send_bark_example())
```

### 发送Telegram消息

```python
import asyncio
from message_push import TelegramSender


async def send_telegram_example():
    await TelegramSender.send_telegram_message(
        bot_token="your_bot_token",
        chat_id="your_chat_id",
        message="这是一条测试Telegram消息"
    )


asyncio.run(send_telegram_example())
```

### 发送IGot消息

```python
import asyncio
from message_push import IGotSender


async def send_igot_example():
    await IGotSender.send_igot_message(
        igot_key="your_igot_key",
        message="这是一条测试IGot消息"
    )


asyncio.run(send_igot_example())
```

### 发送PushPlus消息

```python
import asyncio
from message_push import PushPlusSender


async def send_pushplus_example():
    await PushPlusSender.send_pushplus_message(
        token="your_pushplus_token",
        message="这是一条测试PushPlus消息"
    )


asyncio.run(send_pushplus_example())
```

### 发送Anpush消息

```python
import asyncio
from message_push import AnpushSender


async def send_anpush_example():
    await AnpushSender.send_anpush_message(
        token="your_anpush_token",
        title="测试标题",
        message="这是一条测试Anpush消息",
        url="https://example.com"
    )


asyncio.run(send_anpush_example())
```

### 发送飞书消息

```python
import asyncio
from message_push import FeishuSender


async def send_feishu_example():
    await FeishuSender.send_feishu_message(
        webhook_url="https://open.feishu.cn/open-apis/bot/v2/hook/your_feishu_webhook",
        message="这是一条测试飞书消息"
    )


asyncio.run(send_feishu_example())
```

### 发送Discord消息

```python
import asyncio
from message_push import DiscordSender


async def send_discord_example():
    await DiscordSender.send_discord_message(
        webhook_url="https://discord.com/api/webhooks/your_discord_webhook",
        message="这是一条测试Discord消息"
    )


asyncio.run(send_discord_example())
```

### 发送WhatsApp消息

```python
import asyncio
from message_push import WhatsAppSender


async def send_whatsapp_example():
    await WhatsAppSender.send_whatsapp_message(
        api_url="https://graph.facebook.com/v13.0/your_phone_number_id/messages",
        phone_number="your_phone_number",
        message="这是一条测试WhatsApp消息",
        api_token="your_api_token"
    )


asyncio.run(send_whatsapp_example())
```

### 异步发送所有消息

```python
import asyncio
from message_push import AsyncSender


async def send_all_example():
    email_args = (
        "测试邮件", "这是一封测试邮件", "example@example.com", "your_email@example.com",
        "smtp.example.com", 587, "your_email@example.com", "your_password"
    )
    wechat_args = (
        "your_corp_id", "your_corp_secret", 1000002, "UserID", "这是一条测试微信消息"
    )
    dingtalk_args = (
        "https://oapi.dingtalk.com/robot/send?access_token=your_access_token", "这是一条测试钉钉消息"
    )
    bark_args = (
        "https://api.day.app/your_bark_key", "这是一条测试Bark消息"
    )
    telegram_args = (
        "your_bot_token", "your_chat_id", "这是一条测试Telegram消息"
    )
    igot_args = (
        "your_igot_key", "这是一条测试IGot消息"
    )
    pushplus_args = (
        "your_pushplus_token", "这是一条测试PushPlus消息"
    )
    anpush_args = (
        "your_anpush_token", "测试标题", "这是一条测试Anpush消息", "https://example.com"
    )
    feishu_args = (
        "https://open.feishu.cn/open-apis/bot/v2/hook/your_feishu_webhook", "这是一条测试飞书消息"
    )
    discord_args = (
        "https://discord.com/api/webhooks/your_discord_webhook", "这是一条测试Discord消息"
    )
    whatsapp_args = (
        "https://graph.facebook.com/v13.0/your_phone_number_id/messages", "your_phone_number",
        "这是一条测试WhatsApp消息", "your_api_token"
    )

    await AsyncSender.send_all_messages(email_args, wechat_args, dingtalk_args, bark_args, telegram_args, igot_args,
                                        pushplus_args, anpush_args, feishu_args, discord_args, whatsapp_args)


asyncio.run(send_all_example())
```

### 捐赠

![支持我](https://gitee.com/xiaoqiangclub/xiaoqiangapps/raw/master/images/xiaoqiangclub_ad.png)