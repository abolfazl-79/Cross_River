
class Validation:
    def __init__(self, *args):
        super(Validation, self).__init__(*args)
        
    def is_valid_left(state):
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
        if Validation.is_valid_left(state) and Validation.is_valid_right(state):
            return True
    def can_drive(person):
        if person == 'son' or person == 'daughter' or person == 'thief':
            return False
        return True 
    
    def can_stay_on_boat(person1, person2):
        chosen_persons = [person1, person2]
        if 'daughter' in chosen_persons and 'father' in chosen_persons:
            return False
        elif 'son' in chosen_persons and 'mother' in chosen_persons:
            return False
        elif 'thief' in chosen_persons and 'police' not in chosen_persons:
            return False
        else:
            return True