import time
import epics

def on_change(pvname=None, value=None, timestamp=None, **kwargs):
    print(pvname, value, timestamp)


pv = epics.PV("test01", callback=on_change)

while True:
    time.sleep(0.1)
