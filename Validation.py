
class Validation:
    """
    Conatains all puzzle rules:
    - Which states are valid.
    - Who can drive the boat.
    - Who can stay together in the boat.

    """

    def __init__(self, *args):
        super(Validation, self).__init__(*args)
        
    def is_valid_left(state):
        """Check if left side is valid according to rules."""
        left = state.left_side
        if 'mother' in left and 'father' not in left and 'son' in left:
            return False
        elif 'father' in left and 'mother' not in left and 'daughter' in left:
            return False
        elif 'thief' in left and len(left) > 1 and 'police' not in left:
            return False
        else:
            return True
        
    def is_valid_right(state):
        """Check if right side is valid according to rules."""
        right = state.right_side
        if 'mother' in right and 'father' not in right and 'son' in right:
            return False
        elif 'father' in right and 'mother' not in right and 'daughter' in right:
            return False
        elif 'thief' in right and len(right) > 1 and 'police' not in right:
            return False
        else:
            return True
    
    def is_valid(state):
        """A state valid if both sides are valid."""
        if Validation.is_valid_left(state) and Validation.is_valid_right(state):
            return True
    def can_drive(person):
        """Check if person can drive the boat."""
        if person == 'son' or person == 'daughter' or person == 'thief':
            return False
        return True 
    
    def can_stay_on_boat(person1, person2):
        """Check if two person can share the boat."""
        chosen_persons = [person1, person2]
        if 'daughter' in chosen_persons and 'father' in chosen_persons:
            return False
        elif 'son' in chosen_persons and 'mother' in chosen_persons:
            return False
        elif 'thief' in chosen_persons and 'police' not in chosen_persons:
            return False
        else:
            return True