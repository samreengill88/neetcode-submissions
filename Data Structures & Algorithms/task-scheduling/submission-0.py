class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    
        # get freq map of all tasks
        freqMap = [0] * 26
        for t in tasks:
            # index of task
            freqMap[ord(t) - ord('A')] += 1
        
        # by default we have min heap, to make maxHeap negate all in freqMap
        maxHeap = [-cnt for cnt in freqMap if cnt > 0]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        # pop for maxhea(the most freq task) 
        # process task (subtract 1) -> opposite add 1 since maxHeap
        # inc time (time += 1) 
        # add remaining task to q with ready time (task, time)
        # when time = t pop task from q with time = t
        # continue until tasks in maxHeap or q

        while maxHeap or q:
            time += 1
            # if maxHeap is not empty -> pop from it -> process task(add 1)
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1

                # if count is not 0 -> still have tasks to process -> add it to q with readyTime i.e, current time + n
                if cnt != 0:
                    q.append([cnt, time + n])

            # if q is not empty and first task in the queue is ready to process i.e. q[0][1] == time
            # pop first task ->  q[0][0] and it to heap
            if q and q[0][1] == time:
                first_task = q.popleft()[0]
                heapq.heappush(maxHeap, first_task)

        return time