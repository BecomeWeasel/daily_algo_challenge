from sys import stdin

def sol():
    N,C=map(int,stdin.readline().split())

    houses=list()

    for _ in range(N):
        houses.append(int(stdin.readline()))
    
    min_dist,max_dist=1,max(houses)-min(houses)

    houses.sort()

    answer=-float('inf')
    while min_dist<=max_dist:
        prev=houses[0]

        count=1
        mid=(min_dist+max_dist)//2

        for i in range(1,N):
            if houses[i]-prev>=mid:
                count+=1
                prev=houses[i]


        # print(mid,count)
        if count>=C:
            answer=max(answer,mid)
            min_dist=mid+1
        else:
            max_dist=mid-1
    
    return answer

print(sol())