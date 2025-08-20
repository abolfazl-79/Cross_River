from DLS import Dls
from State import State
from time import time

 

 
    

    
def main():
    """
    Entry point:
    - Defines the starting point of the puzzle.
    - Runs depth-limited search.
    """
    starting_point = State(['police', 'thief','daughter', 'daughter', 'father', 'son', 'son', 'mother'], [], True,0, None)
    dls_search = Dls(starting_point, 70)
    dls_search.serach()
    
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(end - start)
         
        
        
        
      
                

 

 