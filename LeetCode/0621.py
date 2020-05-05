import heapq
#from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        
        temp = {} #temporary dictionary for counting how many of each task are needed
        for task in tasks:
            if task not in temp:
                temp[task] = 1
            else:
                temp[task] += 1
                
        active_heap = [] #This heap keeps track of tasks not on cooldown
        #Create a max heap by pushing tuples of (inverted) count and task name
        for task in temp: 
            heapq.heappush(active_heap, (-temp[task], task))
        
        cooldowns = {} #Dictionary of all tasks on cooldown and their cooldown values and counters.
        #Iterate until there are no tasks left to do. Pick active tasks with largest count.
        while active_heap or cooldowns:
            #For any tasks on cooldown, update their timers and/or transfer them to active heap.
            for task in cooldowns:
                cooldown, counter = cooldowns[task]
                cooldown -= 1
                if cooldown == 0:
                    del cooldowns[task]
                    heapq.heappush(active_heap, (-counter, task))
            
            #Check for any tasks off cooldown, otherwise idle.
            if active_heap:
                neg_count, task = heapq.heappop(active_heap)
                count = -neg_count
                count -= 1
                #If count is still positive after decrement, move task to cooldown
                if count > 0: 
                    cooldowns[task] = (n, count)
                    
            result += 1 #Update number of tasks/idles
        
        return result
            