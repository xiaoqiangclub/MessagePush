import asyncio
from message_push import EmailSender, WeChatSender, DingTalkSender, BarkSender, TelegramSender, IGotSender, \
    PushPlusSender, AnpushSender, FeishuSender, DiscordSender, WhatsAppSender, AsyncSender


async def test_senders():
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

    await AsyncSender.send_messages(email_args, wechat_args, dingtalk_args, bark_args, telegram_args, igot_args,
                                    pushplus_args, anpush_args, feishu_args, discord_args, whatsapp_args)


async def test_senders_with_config():
    config_path = "config.yaml"  # 或者 "config.json"
    message = "这是一条测试消息"
    title = "测试标题"
    url = "https://example.com"

    await AsyncSender.send_messages_with_config(config_path, message, title, url)


if __name__ == '__main__':
    asyncio.run(test_senders())
    asyncio.run(test_senders_with_config())
