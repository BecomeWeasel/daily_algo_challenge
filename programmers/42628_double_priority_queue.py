import heapq
def solution(operations):
    answer = []
    min_q,max_q=list(),list()
    init_q=list()
    
    def getMinHeapFromMaxHeap(l):
        ll=[-x for x in l]
        heapq.heapify(ll)
        return ll
    
    def getMinHeap(l):
        ll=l[:]
        heapq.heapify(ll)
        return ll
    
    def getMaxHeap(l):
        ll=[-x for x in l]
        heapq.heapify(ll)
        return ll
    
    for op in operations:
        if op.count('I')==1:
            min_q.append(int((op.split(' ')[1])))
            min_q=getMinHeap(min_q)
            max_q=getMaxHeap(min_q)
        elif op=='D -1':
            if min_q:
                heapq.heappop(min_q)
                max_q=getMaxHeap(min_q)

        else:
            if max_q:
                heapq.heappop(max_q)
                min_q=getMinHeapFromMaxHeap(max_q)

                    
    return [max(min_q),min(min_q)] if len(max_q)!=0 else [0,0]