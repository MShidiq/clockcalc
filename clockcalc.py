#!/usr/bin/env python
# 
# Clockalc - counting the clock
# ========_=_========_===_=====
# 
#   author = Maulana Shidiq
#   email  = mshidiq98@gmail.com
#   github = MShidiq
# 

def minutes(*clock):
    """
    :clock: array : (hour, minute)
    :rtype: int : minute

    convert clock to minutes
    minutes(1, 30) -> 90 minutes
    """
    if isinstance(clock[0], tuple) or isinstance(clock[0], list):
        clock = clock[0]
    if len(clock) < 2:
        raise IndexError('Too little data to unpack: <minutes(hour, minute)>') 
    if clock[1] > 59:
        raise ValueError('Minute too large')
        
    return 60 * clock[0] + clock[1]

def hours(minute):
    """
    :minute: int : minute
    :rtype: tuple : (hour, minute)

    convert minute to clocks/hours
    hours(90) -> (1, 30) o'clock/hours
    """
    return divmod(minute, 60)

def days(*hours):
    """
    :hours: array : days(hour, minute)
    :rtype: list : return day leaps [days, hours, minutes]
    """
    if isinstance(hours[0], tuple) or isinstance(hours[0], list):
        hours = hours[0]
    if len(hours) < 2:
        hours = (hours[0], 0)
        
    day = divmod(hours[0], 24)
    return [day[0], day[1], hours[1]]

class Clock:
    def __init__(self, *time):
        """
        <class "Clock"> -> Clock object
        """
        if isinstance(time[0], list) or isinstance(time[0], tuple):
            time = time[0]
        if len(time) < 2:
            raise ValueError('Wrong parameter: <Clock(hour, minute)>')

        self.time = time
        self.ltime = list(time)
        self.minute = minutes(*time)
        

    def __repr__(self):
        return 'Clock{}'.format(self.time)


    def __add__(self, t):
        return hours(self.minute + t.minute)

    def __sub__(self, t):
        return hours(self.minute - t.minute)

    def __floordiv__(self, t):
        return hours(self.minute // t.minute)

    def __mul__(self, t):
        return hours(self.minute * t.minute)


    def __iadd__(self, other):
        self.minute += other.minute
        self.time = hours(self.minute)
        self.ltime = list(self.time)
        return self.time

    def __isub__(self, other):
        self.minute -= other.minute
        self.time = hours(self.minute)
        self.ltime = list(self.time)
        return self.time

    def __imul__(self, other):
        self.minute *= other.minute
        self.time = hours(self.minute)
        self.ltime = list(self.time)
        return self.time

    def __ifloordiv__(self, other):
        self.minute //= other.minute
        self.time = hours(self.minute)
        self.ltime = list(self.time)
        return self.time


    def __eq__(self, t):
        return self.minute == t.minute

    def __ne__(self, t):
        return self.minute != t.minute

    def __lt__(self, t):
        return self.minute < t.minute

    def __gt__(self, t):
        return self.minute > t.minute
        
    def __le__(self, t):
        return self.minute <= t.minute

    def __ge__(self, t):
        return self.minute >= t.minute
        

    def __index__(self):
        return self.time

    def __getitem__(self, index):
        return self.time[index]
        
    def __setitem__(self, index, v):
        self.ltime[index] = v
        self.time = tuple(self.ltime)
        self.minute = minutes(*self.time)
        
    def __len__(self):
        return len(self.time)

    def __containts__(self, i):
        return i in self.time


    def increase(self, minute):
        """
        :minute: int : increase time value
        """
        self.minute += minute
        self.time = hours(self.minute)
        self.ltime = list(self.time)
        return hours(self.minute)

    def decrease(self, minute):
        """
        :minute: int : decerease time value
        """
        self.minute -= minute
        self.time = hours(self.minute)
        self.ltime = list(self.time)
        return hours(self.minute)

    def center(self, Clock_obj):
        """
        :Clock_obj: object : Clock object
        :rtype: tuple : center of the clock
        """
        if isinstance(Clock_obj, list) or isinstance(Clock_obj, tuple):
            raise ValueError('Not <Clock> object')
            
        interval = self.minute - Clock_obj.minute
        return hours(interval // 2)

    def quarter(self, Clock_obj=None):
        """
        :rtype: tuple : times sliced into 4 quarter line
        """
        quartal = minutes(self.quartal())
        Q1 = 0 + quartal
        Q2 = Q1+ quartal
        Q3 = Q2+ quartal
        Q4 = Q3+ quartal
        return [hours(Q1), hours(Q2), hours(Q3), hours(Q4)]

    def quartal(self, Clock_obj=None):
        """
        :rtype: list : quartal of the times
        """
        return hours(round(self.minute / 4))

    def days(self):
        '''
        :rtype: list : return days, hour, and minute leaps
        '''
        day = divmod(self.time[0], 24)
        return [day[0], day[1], self.time[1]]

    def string(self):
        """
        :rtype: str : string format
        """
        return '{}:{}'.format(
            '0'+str(self.time[0]) if len(str(self.time[0])) == 1 else self.time[0],
            '0'+str(self.time[1]) if len(str(self.time[1])) == 1 else self.time[1],
        )        


if __name__ == '__main__':
    # TEST
    # ==========    
    from time import strftime
    now = strftime('%H %M').split()
    now = int(now[0]), int(now[1])
    a = Clock(24,30)
    b = Clock(1,30)
    c = b*b
    a[0] = 14
    
    print(a, now)
    a.increase(60)
    
    print(a.string())
    print(a+b, a-b, a//b, c, Clock(c).days())
    print(a==a, a!=b, a>b, b<=a)
    print(a-b, a.center(b))
    print(a.quarter())
    print(Clock(300,0).days())
    print(days(500))
    
    print(minutes(a+b))
