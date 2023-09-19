class State:
    
    def __init__(self, left_side, right_side, is_boat_on_left, depth, parent) :
        self.left_side = left_side
        self.right_side = right_side
        self.is_boat_on_left = is_boat_on_left
        self.depth = depth
        self.parent = parent
        
    
   
    def show(self):
        print('left_side: ',self.left_side)
        print('Right_side: ',self.right_side)
        
        if self.is_boat_on_left:
            print('boat on left')
        else:
            print('boat on right')
        