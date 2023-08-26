import scratchattach as scratch3
import time
from random import randint

'''print(session.session_id)'''

targ = "HarrisonGamez"
session = scratch3.login("qseft1", "qsefts")
user = session.connect_user(targ)
user.follow()
session = scratch3.login("qseft2", "qsefts")
user = session.connect_user(targ)
user.follow()
session = scratch3.login("qseft3", "qsefts")
user = session.connect_user(targ)
user.follow()
session = scratch3.login("qseft4", "qsefts")
user = session.connect_user(targ)
user.follow()
session = scratch3.login("qseft5", "qsefts")
user = session.connect_user(targ)
user.follow()
