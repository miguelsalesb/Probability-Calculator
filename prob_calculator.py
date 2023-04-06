import copy
import random

class Hat:
    # **kwargs to access the keyword arguments
    def __init__(self, **kwargs):  
        self.contents = list()

        for key, value in kwargs.items():
            count = 0
            while count < value:
                self.contents.append(key)
                count = count + 1

    def draw(self, number):
        if number <= len(self.contents):
            rand = random.sample(self.contents, number)
            for r in rand:
                self.contents.remove(r)
        else:
            rand = self.contents

        return rand


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
 
    c = 0
    match = 0

    while c < num_experiments:
        contents_dict = dict()
         
        hat_copy = copy.deepcopy(hat)
        
        contents = Hat.draw(hat_copy, num_balls_drawn)
        
        # get a dictionary with the number of balls of each color
        for b in contents:
            if b not in contents_dict:
                contents_dict[b] = 1
            else:
                contents_dict[b] = contents_dict[b] + 1

        cnt = 0  
        for k, v in contents_dict.items():
               for key, value in expected_balls.items(): 
                if k == key and v >= value:
                    cnt = cnt + 1
                    if cnt == len(expected_balls.keys()):
                        match = match + 1
                        
        c = c + 1
  
    probability = round(match/num_experiments, 3)
    
    return probability
