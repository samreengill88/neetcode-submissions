class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # 1. count freq of all tasks
        count_tasks = [0] * 26
        for task in tasks:
            index = ord(task) - ord('A')
            count_tasks[index] += 1
        
        # 2. make max_heap of count of tasks
        max_heap = [-val for val in count_tasks if val > 0]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # [-count, idle_time]

        # 3. both are not empty we've more tasks to process
        while max_heap or q: 
            time += 1
            if max_heap:
                # process a task -> add 1 since task is -ve in max_heap
                # if count_process -> add to q also add time when it will be available that is time + n
                count_process = heapq.heappop(max_heap) + 1
                if count_process != 0:
                    q.append([count_process, time + n])
                
                # idle time of first index of q is same as time that means the task is available to be processed now so add it to max_heap 
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0] )
                   
        return time 

# TC: t is no of tasks 
#   counting O(t)
#   heapify takes O(26) so O(1)
#   in wc: all tasks are same tasks = [A, A, A] and n = 3 gives A _ _ _ A _ _ _ A
#   n idle time between each copy so O(t.n)
#   total --> O(t * n)->  no of tasks  * idle time
# SC
#   O(1) always 26 slots atmost 