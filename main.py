import zulip
import os
import random

def chunks(l):
  n = 2
  for i in range(0, len(l), n):
    if i == len(l)-(2+1):
      yield l[i:i+n+1]
      return
    else:
      yield l[i:i+n]

subscriber_stream = os.getenv("SUBSCRIBER_STREAM")

client = zulip.Client(email="enthusiasticon-bot@zulipchat.com", client="CoffeConBot/0.1")

subscriptions = client.list_subscriptions({'include_subscribers':True})

stream = [s for s in subscriptions["subscriptions"] if s["name"] == subscriber_stream][0]
subscribers = [s for s in stream["subscribers"] if s != os.getenv("ZULIP_EMAIL")]
random.shuffle(subscribers)
groups = list(chunks(subscribers))
print(groups)

for group in groups:
  content = """
Hey, you've been matched! :robot:

Feel free to chat a bit, or have a video call! (You can insert a link to a new Jitsi room by clicking "Reply" and then clicking on the camera icon.)
"""
  client.send_message({'type': 'private', 'content': content, 'to': group})
