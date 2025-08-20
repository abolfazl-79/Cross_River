class State:
    """
    Represent a single state in the river crossing puzzle.

    Contains:
    - left side: people on the left side
    - right side: people on the right side
    - is boat on left: True if boat is on left side
    - depth: depth of this state in search tree
    - parent: reference to parent state (for path reconstruction)
    """
    def __init__(self, left_side, right_side, is_boat_on_left, depth, parent) :
        self.left_side = left_side
        self.right_side = right_side
        self.is_boat_on_left = is_boat_on_left
        self.depth = depth
        self.parent = parent
        
    
   
    def show(self):
        """Print a readable representation of the state."""
        side_info = f"Left: {self.left_side}, Right: {self.right_side}, "
        side_info += "Boat: Left" if self.is_boat_on_left else "Boat: Right"
        return side_info
        