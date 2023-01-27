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
    count_7 = 0
    AMVAL = 'AM'
    while True:
        t.sleep(0.5)
        clockStart.clock += 1
        count_7 += 1
        if clockStart.AM == True:
            AMVAL = 'AM'
        else:
            AMVAL = 'PM'
        if clockStart.clock == 12:
            clockStart.clock = 1
            if clockStart.AM == True:
                clockStart.AM = False
            elif clockStart.AM == False:
                clockStart.AM = True
        elif count_7 == 7:
            count_7 = 0
            timeReq = input('Would you lie to know the time? Y/N: ').lower()
            if timeReq == 'y':
                print('It is %s:00 %s!' % (clockStart.clock, AMVAL))
                
        
        

clockwork()

