from threading import Timer
from Core.DB import update_db

SEC_PER_DAY = 86400
INTERVAL = SEC_PER_DAY
def updater():
    update_db()
    print("*Finished Update - Next update in {t}*".format(t=str(INTERVAL)))
    Timer(INTERVAL, updater).start()
updater()
