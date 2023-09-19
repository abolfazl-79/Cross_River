from Validation import Validation
from State import State

class Update:
    children = []
    def __init__(self, children) -> None:
        self.children = children
        
        
    def generate_children(self,state):
        if state.is_boat_on_left:
            self.__go_to_right(state, self.children)      
                    
        else:
            self.__go_to_left(state, self.children)
                    
        return self.children
    
    
    
    def __go_to_right(self,state, children):
        
    #In this case the transmission is dual
        self.__dual_transmission(state,children)
    
    #In this case the transmission is single
        self.__single_transmission(state, children)
        
        
    def __go_to_left(self,state, children):
        
    #In this case the transmission is dual
        self.__dual_transmission(state, children)
        
        #In this case the transmission is single
        self.__single_transmission(state, children)
        
    def __dual_transmission(self, state, children):
        boat_on_left = state.is_boat_on_left
        # Transmission from left to right
        if boat_on_left :
            origin_side = state.left_side
            destination_side = state.right_side
            origin_side_length = len(origin_side)
            new_depth = state.depth + 1
        
        #Transmission from right to left  
        else:
            origin_side = state.right_side
            destination_side = state.left_side
            origin_side_length = len(origin_side)
            new_depth = state.depth + 1
        
        for index_person1 in range(origin_side_length):
            for index_person2 in range(0 ,origin_side_length):
                
                persons_on_origin = origin_side.copy()
                persons_on_destination = destination_side.copy()
                
                person1 = persons_on_origin[index_person1]
                person2 = persons_on_origin[index_person2]
                
                if person1 == person2:
                    continue
                #Checking validation for person1 and person2 for transmission
                if not Validation.can_drive(person1) and not Validation.can_drive(person2):
                    continue
                if not Validation.can_stay_on_boat(person1, person2):
                    continue
                    
                
                #self origin_side
                persons_on_origin.remove(person1)
                persons_on_origin.remove(person2)
                new_origin_side = sorted(persons_on_origin)
                
                #self destination_side
                persons_on_destination.append(person1)
                persons_on_destination.append(person2)
                new_destination_side = sorted(persons_on_destination)
                
                if boat_on_left:
                    new_state = State(new_origin_side,new_destination_side, False,new_depth, state)
                    if not new_state in children:
                        children.append(new_state)
                else:
                    #Create new state and add to list
                    new_state = State(new_destination_side,new_origin_side, True,new_depth,state)
                    if not new_state in children:
                        children.append(new_state)
                        
                        
    def __single_transmission(self, state, children):
        
        boat_on_left = state.is_boat_on_left
        
        # Transmission from left to right
        if state.is_boat_on_left :
            origin_side = state.left_side
            destination_side = state.right_side
            new_depth = state.depth + 1
        
        #Transmission from right to left  
        else:
            origin_side = state.right_side
            destination_side = state.left_side
            new_depth = state.depth + 1
            
        
        for person in origin_side:
            
            persons_on_origin = origin_side.copy()
            persons_on_destination = destination_side.copy()
            
            if Validation.can_drive(person):
                
                #self origin_side
                persons_on_origin.remove(person)
                new_origin_side = persons_on_origin
                
                #self destination_side
                persons_on_destination.append(person)
                new_destination_side = persons_on_destination
                
                if boat_on_left:
                    
                    new_state = State(new_origin_side,new_destination_side, False,new_depth,state)
                    children.append(new_state)
                else:
                    #Create new state and add to list
                    new_state = State(new_destination_side,new_origin_side, True,new_depth, state )
                    children.append(new_state)
                            
            

    
        