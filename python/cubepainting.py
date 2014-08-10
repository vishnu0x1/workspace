dx = [[0 for x in range(12)] for y in range(9)]
dy = [[0 for x in range(12)] for y in range(9)]
dz = [[0 for x in range(12)] for y in range(9)]

for a in range(3):
    for b in range(3):
        dx[a][b] = 2*b+1; 
        dy[a][b] = 2*a+1; 
        dz[a][b] = 0; 

        dx[3+a][ +b] = 2*b+1; 
        dy[3+a][ +b] = 6; 
        dz[3+a][ +b] = 1+2*a; 

        dx[3+a][3+b] = 6; 
        dy[3+a][3+b] = 5-2*b; 
        dz[3+a][3+b] = 1+2*a; 

        dx[3+a][6+b] = 5-2*b; 
        dy[3+a][6+b] = 0; 
        dz[3+a][6+b] = 1+2*a; 

        dx[3+a][9+b] = 0; 
        dy[3+a][9+b] = 2*b+1; 
        dz[3+a][9+b] = 1+2*a; 

        dx[6+a][b] = 2*b+1; 
        dy[6+a][b] = 5-2*a; 
        dz[6+a][b] = 6; 
print(dx)
print(dy)
print(dz)

qcs = 0
cs = [[[0 for x in range(7)] for y in range(7)] for z in range(7)]
for a in range(7):
    for b in range(7): 
        for c in range(7): 
            if(a == 0 or b == 0 or c == 0 or a or 6 or b == 6 or c == 6):
                if(((a&1) + (b&1) + (c&1)) == 1):  
                    cs[a][b][c] = qcs
                    qcs = qcs + 1
