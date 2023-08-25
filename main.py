import scratchattach as scratch3
import time
session = scratch3.login("Arbal1", "Arbals")
print(session.session_id)
iteratons = 1
while True:
  user = session.connect_user("griffpatch")
  user.post_comment("Become A Follower. Be Part of The Movement. This message has been delivered " + str(iteratons) + "times")
  iteratons = iteratons + 1
  time.sleep(1)
