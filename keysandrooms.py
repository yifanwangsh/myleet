#for every key in a new room
#if that key we've never seen before, then we goto that room


def canVisitAllRooms(rooms):
    '''
    List[List[int]]
    '''
    def collectKeys(klist):
        for k in klist:
            if k not in pool:
                pool.append(k)
                collectKeys(rooms[k])


    pool = [0]

    collectKeys(rooms[0])

    if len(pool) < len(rooms):
        return False
    else:
        return True
        


    
input = [[1],[2],[3],[]]
print (canVisitAllRooms(input))

input1 = [[1,3],[3,0,1],[2],[0]]
print (canVisitAllRooms(input1))

input2 = [[2,3],[],[2],[1,3,1]]
print (canVisitAllRooms(input2))