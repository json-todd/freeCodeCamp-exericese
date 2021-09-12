# Ver 2: Define ```draw``` function for ```Hat``` class

class Hat:
    def __init__(self, **kwarg):
        self.contents = []
        for ball,number in kwarg.items():
            for i in range(number):
                self.contents.append(ball)
        
    def draw(self, num_balls_drawn):
        self.remove = []
        for i in range(num_balls_drawn):
            rndm = random.randint(0, len(self.contents) - 1 )
            ball_removed = self.contents.pop(rndm)
            self.remove.append(ball_removed)
        return self.remove
