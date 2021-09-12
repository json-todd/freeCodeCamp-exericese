# Ver 3: Complete version

import copy
import random

class Hat:
    def __init__(self, **kwarg):
        self.contents = []
        for ball,number in kwarg.items():
            for i in range(number):
                self.contents.append(ball)
        
    def draw(self, num_balls_drawn):
        """ accept argument indicating number of balls to draw from hat.
        remove balls at random from `contents`
        return those balls as a list of strings.
        """        
        self.remove = []

        if num_balls_drawn >= len(self.contents):
            self.remove = self.contents
        else: 
            for i in range(num_balls_drawn):
                rndm = random.randint(0, len(self.contents) - 1 )
                ball_removed = self.contents.pop(rndm)
                self.remove.append(ball_removed)
        return self.remove

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    satisfy_experiments = 0
    
    for i in range(num_experiments):
        
        # creating a deep copy of Hat object. 
        # function use afterward affects the object; hence it must be deep copied
        hat_copy = copy.deepcopy(hat)
        ball_removed = hat_copy.draw(num_balls_drawn)
        ball_removed_dict = {}
        for b in ball_removed:
            ball_removed_dict[b] = ball_removed_dict.get(b,0) + 1
        
        def compareWithExpected(expt,real):
            satisfy = 0
            for ball in expt:
                if real.get(ball,0) >= expt[ball]:
                    satisfy += 1
            return satisfy == len(expt)
        
        satisfy = compareWithExpected(expected_balls, ball_removed_dict)
        if satisfy:
            satisfy_experiments += 1

    prob = satisfy_experiments / num_experiments
    return prob    
        
    
hat1 = Hat(blue = 3,red=2,green=6)
exp = experiment(hat = hat1,
                expected_balls={"blue":2,"green":1},
                num_balls_drawn=4,
                num_experiments=1000)
print(exp)
