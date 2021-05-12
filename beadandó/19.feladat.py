import numpy as np

def atlo1(m):
    if (m[0,0]+m[1,1]+m[2,2]+m[3,3])==12:
        return True
    else:
        return False

def atlo2(m):
    if (m[0,3]+m[1,2]+m[2,1]+m[3,0])==12:
        return True
    else:
        return False

x = np.zeros((1,4))
ls = []
for i in range(10):
    x[0,0] = i
    for i1 in range(10):
        x[0,1] = i1
        for i2 in range(10):
            x[0,2] = i2
            for i3 in range(10):
                x[0,3] = i3
                if x[0,0] + x[0,1] + x[0,2] + x[0,3] == 12 :
                    y = [int(x[0,0]), int(x[0,1]), int(x[0,2]), int(x[0,3])]
                    ls.append(y)


print(ls)
matrix=np.zeros((4,4))
db=0
db2=0
for i in ls:
    matrix[0,:] = i
    for j in ls:
        matrix[1,:] = j

        if matrix[0,0]+matrix[1,0] <13 and matrix[0,1]+matrix[1,1] <13 and  matrix[0,2]+matrix[1,2] <13 and matrix[0,3]+matrix[1,3] <13:

            for k in ls:
                matrix[2,:] = k

                muvelet = 12-(matrix[0,0]+matrix[1,0]+matrix[2,0])
                if -1<(muvelet) and (muvelet)<10:
                    matrix[3,0] = muvelet
                else:
                    break

                muvelet2 = 12 - (matrix[0, 1] + matrix[1, 1] + matrix[2, 1] )
                if -1<(muvelet2) and (muvelet2)<10 :
                    matrix[3,1] = muvelet2
                else:
                    break

                muvelet3 = 12 - (matrix[0, 2] + matrix[1, 2] + matrix[2, 2] )
                if -1<(muvelet3)and (muvelet3)<10:
                    matrix[3, 2] = muvelet3
                else:
                    break

                muvelet4 = 12- (matrix[0, 3] + matrix[1, 3] + matrix[2, 3] )
                if -1<(muvelet4) and (muvelet4)<10:
                    matrix[3, 3] = muvelet4
                else:
                    break

                print(matrix)
                db2+=1

                if matrix[0,0]+matrix[1,0]+matrix[2,0]+matrix[3,0]==12 and matrix[0,1]+matrix[1,1]+matrix[2,1]+matrix[3,1]==12 and matrix[0,2]+matrix[1,2]+matrix[2,2]+matrix[3,2]==12 and matrix[0,3]+matrix[1,3]+matrix[2,3]+matrix[3,3]==12 and matrix[3,0]+matrix[3,1]+matrix[3,2]+matrix[3,3]==12 and atlo1(matrix) is True and atlo2(matrix) is True:
                    db+=1
print(db2)
print(db)



