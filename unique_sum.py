n=int(input())
lst=list(map(int,input().split()))
c=0
for i in set(lst):
   c+=i
print(c)