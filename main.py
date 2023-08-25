import scratchattach as scratch3
import time
session = scratch3.login("msgBOT", "Arbals")
print(session.session_id)
while True:
  user = session.connect_user("CraZCoder360")
  user.follow()
  time.sleep(1)
  user.unfollow()
  
