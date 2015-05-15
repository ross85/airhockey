from const import *


class Chrono:

    def __init__( self, m, s, ms):
        self.__minute = m
        self.__second = s
        self.__millisecond = ms    
        
    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def get_millisecond(self):
        return self.__millisecond
        
    def set_minute(self,m):
        self.__minute = m
    def set_second(self,s):
        self.__second = s
    def set_millisecond(self,ms):
        self.__millisecond = ms

    def add_minute(self,m):
        self.set_minute(self.get_minute()+m)

    def add_second(self,s):
        self.set_second(self.get_second()+s)
        if self.get_second()>=60:
            self.add_minute(int(self.get_second()/60))
            self.set_second(self.get_second()%60)

    def add_millisecond(self,ms):
        self.set_millisecond(self.get_millisecond()+ms)
        if self.get_millisecond()>=1000:
            self.add_second(int(self.get_millisecond()/1000))
            self.set_millisecond(self.get_millisecond()%1000)

    def reset(self):
        self.set_minute(0)
        self.set_second(0)
        self.set_millisecond(0)

    def __str__(self):
        return '%(minute)02d:%(second)02d' % {'minute': self.get_minute(), 'second': self.get_second()}

    def blit( self, screen, font):
        screen.blit( font.render( self.__str__(), 1, CHRONO_LABEL_COLOR), CHRONO_LABEL_POS)