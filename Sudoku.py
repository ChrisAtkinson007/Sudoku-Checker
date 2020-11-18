l1=[]
l2=[0]*9
blks=[]
cols=[]
boo=1
import numpy

for i in range(9):
    temp=input("Enter a 9 digit row of numbers 0-9")
    if len(temp)==9 and temp.isdecimal():
        print(temp)
        l1[:] = temp
        print(l1)
        l2[i]=l1[:]
        print(l2)
        print("********************")
    else:
        print("Not valid")
        break

print(l2)

#Check Sudoku Rows
for elem in l2:
    telem=elem[:]
    telem.sort()
    if telem!=['1','2','3','4','5','6','7','8','9']:
        print("NO rows")
        boo = 0
        break

#Check columns:
for i in range(9):
    cols.append(l2[0][i]+l2[1][i]+l2[2][i]+l2[3][i]+l2[4][i]+l2[5][i]+l2[6][i]+l2[7][i]+l2[8][i])

print(cols)
print("########COLUMNS PRE SORT")

tlst=[]
for elem in cols:
    telem=elem[:]
    tlst[:]=telem
    tlst.sort()
    print(tlst)
    print("####COLS######")
    if tlst!=['1','2','3','4','5','6','7','8','9']:
        print("NO cols")
        boo = 0
        break

#Check Sudoku Blocks
for i in range(0,9,3):
    for j in range(0,9,3):
        blks.append(l2[i][j:j+3]+l2[i+1][j:j+3]+l2[i+2][j:j+3])

print(blks)
print("########BLKS PRE SORT")


for elem in blks:
    telem=elem[:]
    telem.sort()
    print(telem)
    print("#######BLKS######")
    if telem!=['1','2','3','4','5','6','7','8','9']:
        print("NO blks")
        boo=0
        break



if boo==1:
    print("YES")