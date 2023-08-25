import scratchattach as scratch3
import time
from random import randint
session = scratch3.login("msgBOT", "Arbals")
print(session.session_id)
while True:
  user = session.connect_user("CraZCoder360")
  user.post_comment(content=randint(0,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
  time.sleep(1)
