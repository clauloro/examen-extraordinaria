def plants_and_zombies(lawn, zombies):
    lawn = [[int(cell) if cell.isdigit() else (0 if cell == ' ' else 2) for cell in row] for row in lawn]
    zombies = sorted([(x, y, z) for x, y, z in zombies])
    
    for move in range(1000):
        if len(zombies) == 0:
            return None
        for i in range(len(zombies)):
            zombies[i] = (zombies[i][0], zombies[i][1], zombies[i][2]-1)
            if zombies[i][2] < 0:
                del zombies[i]
        
        for y in range(len(lawn)):
            for x in range(len(lawn[0])):
                if lawn[y][x] == 0:
                    continue
                elif lawn[y][x] == 1:
                    if x+1 < len(lawn[0]) and any(zombie[1] == y and zombie[2] == x+1 for zombie in zombies):
                        for i in range(len(zombies)):
                            if zombies[i][1] == y and zombies[i][2] == x+1:
                                zombies[i] = (zombies[i][0], zombies[i][1], zombies[i][2]-1)
                                if zombies[i][2] < 0:
                                    del zombies[i]
                else: # shooter is an S-shooter
                    for i in range(len(zombies)):
                        if zombies[i][1] in {y-1, y, y+1} and zombies[i][2] == x+1:
                            zombies[i] = (zombies[i][0], zombies[i][1], zombies[i][2]-1)
                            if zombies[i][2] < 0:
                                del zombies[i]
        
        if any(zombie[2] == 0 for zombie in zombies):
            return move
    
    return None
