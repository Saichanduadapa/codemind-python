n,m=map(int,input().split())
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
print(len(s1.symmetric_difference(s2)))