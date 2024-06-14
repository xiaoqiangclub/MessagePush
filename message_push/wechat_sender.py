# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： wechat_sender.py
# 项目描述： 发送微信消息的模块

import httpx

class WeChatSender:
    @staticmethod
    async def send_wechat_message(wechat_corp_id: str, wechat_corp_secret: str, wechat_agent_id: int, message: str, touser: str = "@all", toparty: str = "", totag: str = ""):
        """
        发送微信消息

        :param wechat_corp_id: 企业微信ID
        :param wechat_corp_secret: 企业微信密钥
        :param wechat_agent_id: 企业微信应用ID
        :param message: 消息内容
        :param touser: 接收消息的用户ID列表，多个用户用 '|' 分隔，默认为 '@all'
        :param toparty: 接收消息的部门ID列表，多个部门用 '|' 分隔
        :param totag: 接收消息的标签ID列表，多个标签用 '|' 分隔
        获取企业微信参数：https://work.weixin.qq.com/api/doc/90000/90135/91039
        """
        async with httpx.AsyncClient() as client:
            try:
                # 获取AccessToken
                token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wechat_corp_id}&corpsecret={wechat_corp_secret}"
                token_response = await client.get(token_url)
                token_data = token_response.json()
                access_token = token_data.get('access_token')

                # 发送消息
                send_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
                headers = {
                    "Content-Type": "application/json"
                }
                data = {
                    "touser": touser,
                    "toparty": toparty,
                    "totag": totag,
                    "msgtype": "text",
                    "agentid": wechat_agent_id,
                    "text": {
                        "content": message
                    },
                    "safe": 0
                }
                response = await client.post(send_url, headers=headers, json=data)
                result = response.json()
                if result.get('errcode') == 0:
                    print("微信消息发送成功")
                else:
                    print(f"微信消息发送失败: {result.get('errmsg')}")
            except Exception as e:
                print(f"微信消息发送失败: {e}")

    @staticmethod
    async def send_wechat_message_with_config(config: dict, message: str):
        """
        使用配置文件发送微信消息

        :param config: 配置字典
        :param message: 消息内容
        """
        wechat_config = config['wechat']
        await WeChatSender.send_wechat_message(
            wechat_corp_id=wechat_config['corp_id'],
            wechat_corp_secret=wechat_config['corp_secret'],
            wechat_agent_id=wechat_config['agent_id'],
            message=message,
            touser=wechat_config.get('to_user', "@all"),
            toparty=wechat_config.get('to_party', ""),
            totag=wechat_config.get('to_tag', "")
        )