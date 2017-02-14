class Sphere():
    
    
    def __init__(self, r=1.0,x=0.0,y=0.0,z=0.0):
        self.r=r
        self.x=x
        self.y=y
        self.z=z
        
    def get_volume(self):
        import math
        vol= (4*math.pi*self.r*self.r*self.r)/3
        return vol
    
    def get_square(self):
        import math
        sq=math.pi*4*self.r*self.r
        return sq
    
    def get_radius(self):
        return self.r
    
    def get_center(self):
        return self.x, self.y, self.z
        
    def set_radius(self, r): 
        self.r=r
        
    def set_center(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def is_point_inside(self,x,y,z):
        if self.x-self.r<x<self.x+self.r and self.y-self.r<y<self.y+self.r and self.z-self.r<z<self.z+self.r:
            return True
        else:
            return False
