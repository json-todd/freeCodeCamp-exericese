class Hat:
   
    def __init__(self, **kwarg):
        self.contents = []
        for ball,number in kwarg.items():
            for i in range(number):
                self.contents.append(ball)
        
    def draw():
        pass
    
hat1 = Hat(yellow=3, blue=2, green=6)
print( hat1.contents )
