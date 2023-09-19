from Validation import Validation
from State import State
from Update import Update
import time

class Dls:
    __unexpanded_states = []
    __expanded_states = []
    __head = -1
    def __init__(self, starting_point, max_depth) -> None:
        self.__unexpanded_states.append(starting_point) 
        self.max_depth = max_depth
        
    def serach(self):
        while True:
            try:
                n = self.__unexpanded_states[self.__head]
                
                if Validation.is_valid(n):
                    
                    if self.__is_goal(n):
                        self.__pathshow(n,0.5) 
                        print('Transferring is done successfully')
                        return
                    
                    if not self.__is_expanded(n):
                        self.__expanded_states.append(n) 
                        self.__unexpanded_states.pop(self.__head)
                        
                        if n.depth < self.max_depth:
                            ch_list = []
                            update = Update(ch_list)
                            ch_list = update.generate_children(n)
                            self.__add_to_list(self.__unexpanded_states, ch_list[::-1])
                            
                    else:
                        self.__unexpanded_states.pop(self.__head)
                else:
                    self.__unexpanded_states.pop(self.__head)
            
            except IndexError:
                print('Up to a depth of {0} is not the goal state'.format(self.max_depth))
                return
                
                
    def __is_goal(self,state):
        if len(state.left_side) == 0:
            return True
        return False
    
    def __is_expanded(self, state):
        
        for node in self.__expanded_states:
            if self.__is_dentical(node, state):
                return True
        return False
           
        
    def __add_to_list(self, un, ch_list):
        for state in ch_list:
            un.append(state)  
            
    def __pathshow(self, state, delay):
        print(state.show(), '\n')
        while state.parent != None:
            time.sleep(delay)
            state = state.parent
            print(state.show(), '\n')
            
    def __is_dentical(self,state1, state2):
        if (sorted(state1.left_side) ==sorted(state2.left_side) and
            sorted(state1.right_side) == sorted(state2.right_side) and 
            state1.is_boat_on_left == state2.is_boat_on_left):
                return True
        else: return False
        