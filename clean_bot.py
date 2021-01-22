import random
import sys
import base_bot

slack_token = sys.argv[1]

channelName = "공지"
RANDOM_TAIL = ["있답니다.", "있어요 ㅎㅎ.", "있으니, 도망가지마세요.", "... 이쯤 되면 다들 아시죠?", "있습니다."]
message = "[공지봇] 금일 18:30에 청소가 " + random.choice(RANDOM_TAIL)

channelName, channel_id = base_bot.channelId(channelName, slack_token)
base_bot.sendMessage(channel_id, message, slack_token)
