import ActiveCircle


class Goalpost(ActiveCircle.ActiveCircle):

    def __init__( self, pos, delta, mass, path):
        ActiveCircle.ActiveCircle.__init__( self, pos, 0, 0, mass, path, 0)
        self.__delta = delta

        self.set_pos_xy((pos[0]+delta[0]*self.get_width()*0.5,pos[1]+delta[1]*self.get_height()*0.5))
        
    def get_delta(self):
        return self.__delta
        
    def set_delta(self,delta):
        self.__delta = delta
        
    def collision(self, B, dt):
        posA = self.get_pos_xy()
        delta = self.get_delta()
        posB = B.get_pos_xy()

        if (delta[1]==-1 and posB[1]<=posA[1]) or (delta[1]==1 and posB[1]>=posA[1]):
            return False;
            
        ActiveCircle.ActiveCircle.collision(self, B, dt)