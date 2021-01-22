import random
import sys
import base_bot

slack_token = sys.argv[1]

channelName = "오늘-뭐먹지"
RANDOM_TAIL = ["원할머니이모 닭한마리", "이차돌", "뱅뱅막국수", "샐러디", "와곱", "짱깨", "갈비집", "할머니순두부", "굼터치킨", "떡볶이 배달"]
message = "[오늘모먹지? 봇] 오늘 추천드리는 음식음 다음과 같습니다 :D" + random.choice(RANDOM_TAIL)

channelName, channel_id = base_bot.channelId(channelName, slack_token)
base_bot.sendMessage(channel_id, message, slack_token)
