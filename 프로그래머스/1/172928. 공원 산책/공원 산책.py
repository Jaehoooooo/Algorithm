def solution(park, routes):
    answer = []

    
    for i in range(len(park)):
        a = list(map(str, park[i]))
        park[i] = a
    
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x = int(i)
                y = int(j)
                # pass
    
    for i in range(len(routes)):
        b = list(map(str, routes[i]))
        routes[i] = b
    
    H = len(park)-1
    W = len(park[0])-1
    
    for j in range(len(routes)):
        x_init = x
        y_init = y
        for i in range(1, int(routes[j][2])+1):
            if routes[j][0] == 'E':
                if y_init + int(routes[j][2]) <= W:
                    if park[x][y+1] == 'X':
                        y = y_init
                        break
                    else:
                        y = y+1
            elif routes[j][0] == 'W':
                if y_init - int(routes[j][2]) >= 0:
                    if park[x][y-1] == 'X':
                        y = y_init
                        break
                    else:
                        y = y-1
            elif routes[j][0] == 'S':
                if x_init + int(routes[j][2]) <= H:
                    if park[x+1][y] == 'X':
                        x = x_init
                        break
                    else:
                        x = x+1
            else:
                if x_init - int(routes[j][2]) >= 0:
                    if park[x-1][y] == 'X':
                        x = x_init
                        break
                    else:
                        x = x-1

    return [x,y]