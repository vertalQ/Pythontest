import time
t = time
#---------------------------------

class DNTime:
    def __init__(self):
        self.clock = 1
        self.AM = True

clockStart = DNTime()

def clockwork():
    global clockStart
    while True:
        t.sleep(0.5)
        print(clockStart.clock)
        print(clockStart.AM)
        clockStart.clock += 1
        if clockStart.clock == 12:
            t.sleep(0.5)
            print(clockStart.clock)
            print(clockStart.AM)
            clockStart.clock = 1
            if clockStart.AM == True:
                clockStart.AM = False
            elif clockStart.AM == False:
                clockStart.AM = True

clockwork()

