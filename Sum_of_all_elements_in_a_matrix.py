r,c=map(int,input().split())
mat=[]
sum=0
for i in range(r):
    lst=list(map(int ,input().split()))
    mat.append(lst)
for i in range (r):
    for j in range(c):
        sum=sum+mat[i][j]
print(sum)