import random
import sys
import base_bot

slack_token = sys.argv[1]

channelName = "오늘-뭐먹지"
RANDOM_TAIL = ["원할머니이모 닭한마리", "이차돌", "뱅뱅막국수", "샐러디", "와곱", "짱깨", "할머니순두부", "떡볶이 배달", "봉구스밥버거", "명동할머니국수", "가츠동", "푸팟퐁커리", "맘스터치", "국대치킨", "김밥천국", "글쎄요.. 저도 잘 모르겠네요^^"]
message = "[오늘모먹지? 봇] 오늘 추천드리는 음식은 다음과 같습니다 :D " + random.choice(RANDOM_TAIL)

channelName, channel_id = base_bot.channelId(channelName, slack_token)
base_bot.sendMessage(channel_id, message, slack_token)
