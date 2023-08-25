import scratchattach as scratch3
import time
session = scratch3.login("Arbal1", "Arbals")
print(session.session_id)
iteratons = 1
while True:
  user = session.connect_user("griffpatch")
  user.post_comment("This is an unofficial Scratch Test. This message has been delivered " + str(iteratons) + " times. ⏶ Please do not report this comment ⏶")
  iteratons = iteratons + 1
  time.sleep(1)
