import requests
from pandas.io.json import json_normalize


def channelId(channel_name, slack_token):
    # 채널 조회 API 메소드: conversations.list
    URL = 'https://slack.com/api/conversations.list'

    # 파라미터
    params = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token
    }

    # API 호출
    res = requests.get(URL, params=params)

    channel_list = json_normalize(res.json()['channels'])
    channel_id = list(channel_list.loc[channel_list['name'] == channel_name, 'id'])[0]

    return (channel_name, channel_id)


def sendMessage(channel_id, message, slack_token):
    # 파라미터
    data = {'Content-Type': 'application/x-www-form-urlencoded',
            'token': slack_token,
            'channel': channel_id,
            'text': message,
            'reply_broadcast': 'True',
            }

    # 메시지 등록 API 메소드: chat.postMessage
    URL = "https://slack.com/api/chat.postMessage"
    res = requests.post(URL, data=data)
