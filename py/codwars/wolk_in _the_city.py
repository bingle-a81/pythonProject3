wlk=['w','e','w','e','w','e','w','e','w','e','w','e']

def is_valid_walk(walk):    
    if len(walk)!=10:
        print('should return False')
    else:
        north=walk.count('n')
        south=walk.count('s')
        east=walk.count('e')
        west=walk.count('w')
        if north==south and east==west:
            print('should return True')
        else:
            print('should return False')
    
    #determine if walk is valid
    # pass


is_valid_walk(wlk)