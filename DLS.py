from Validation import Validation
from State import State
from Update import Update
import time
from Animate import AnimateRiver
import matplotlib.pyplot as plt

class Dls:

    """
    Implements Depth-Limited Search (DLS) for solving the river crossing puzzle.
    - Keep track of expanded and unexpanded states.
    - Limits the search depth by `max-depth`
    """
    __unexpanded_states = []   # Stack of states yet to be expanded
    __expanded_states = []     # Stack already expanded (to avoid repetition)
    __head = -1                # Always points to the last element (DFS stack behavior)
    def __init__(self, starting_point, max_depth) -> None:
        """Initialize with the starting state and maximum depth."""
        self.__unexpanded_states.append(starting_point) 
        self.max_depth = max_depth
        
    def serach(self):
        """
        Main loop of depth-limited search
        Expand states until goal is found or depth limit is reached.
        """
        while True:
            try:
                n = self.__unexpanded_states[self.__head] # Take the last unexpanded node
                
                # Check validity of current state
                if Validation.is_valid(n):
                    # If this the goal, print the path and stop
                    if self.__is_goal(n):
                        self.__pathshow(n,0.5) 
                        print('Transferring is done successfully')
                        return
                    
                    # Expand if not already expanded
                    if not self.__is_expanded(n):
                        self.__expanded_states.append(n) 
                        self.__unexpanded_states.pop(self.__head)
                        
                        # Generate children if depth limit not exceeded
                        if n.depth < self.max_depth:
                            ch_list = []
                            update = Update(ch_list)
                            ch_list = update.generate_children(n)
                            self.__add_to_list(self.__unexpanded_states, ch_list[::-1])
                            
                    else:
                        # Already expanded, discard node
                        self.__unexpanded_states.pop(self.__head)
                else:
                    # Invalid state, discard node
                    self.__unexpanded_states.pop(self.__head)
            
            except IndexError:
                # No more nodes left to expand
                print('Up to a depth of {0} is not the goal state'.format(self.max_depth))
                return
                
                
    def __is_goal(self,state):
        """Goal is when the left side is empty (everyone trasferred)."""
        if len(state.left_side) == 0:
            return True
        return False
    
    def __is_expanded(self, state):
        """Check if state is already expanded"""
        for node in self.__expanded_states:
            if self.__is_dentical(node, state):
                return True
        return False
           
        
    def __add_to_list(self, un, ch_list):
        """Add child states to unexpanded list (DFS stack)"""
        for state in ch_list:
            un.append(state)  
            
    def __pathshow(self, state, delay):
        """
        Prints the solution path from goal to start by following parents
        Uses delay for step by step printing.
        """
        path = []
        while state is not None:
            path.append(state)
            state = state.parent
        path.reverse()

        # Launch interactive animation
        animator = AnimateRiver(path)
        plt.show()
    def __is_dentical(self,state1, state2):
        """Check if two states are identical (same left, right, boat position)."""
        if (sorted(state1.left_side) ==sorted(state2.left_side) and
            sorted(state1.right_side) == sorted(state2.right_side) and 
            state1.is_boat_on_left == state2.is_boat_on_left):
                return True
        else: return False
        