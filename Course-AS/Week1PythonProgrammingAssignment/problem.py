

def func(n, c, a):
    total=sum(a)
    if total<=c:
        return "Yes"
    return "No"



t = int(input())
ans=[]
a = []
for _ in range(0, t):
    n, c =input().split(" ")
    a = list(map(int, input().split(" ")))
    ans.append(func(int(n), int(c), a))

for a in ans:
    print(a)




