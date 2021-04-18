# This problem reminded me of a breadth-first search, modified with time dependency heap sorts. However you view it is not really important. Enjoy!

# The following problem is from LeetCode: https://leetcode.com/contest/weekly-contest-237/problems/single-threaded-cpu/
"""
tasks[i] = [enqueueTime, processingTime] 

If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.

Once a task is started, the CPU will process the entire task without stopping.
"""

class SingleThreadedCPU:    
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        original = tasks[:]
        tasks = sorted(tasks, key = lambda x: x[0])
        order = []
        processQueue = []
        time = tasks[0][0]
        
        while len(tasks) != 0 or len(processQueue) != 0:
            if len(processQueue) != 0:
                processQueue = sorted(processQueue, key = lambda x: [x[1], x[2]])
                tmp = processQueue[0]
                del processQueue[0]
                time += tmp[1]
                order.append(tmp[2])
            
            deleteIdx = []
            
            for i in range(len(tasks)):
                if time >= tasks[i][0]:
                    item = tasks[i]
                    item.append(original.index(item))
                    processQueue.append(item)
                    deleteIdx.append(i)
                else:
                    break
            
            for delete in deleteIdx[::-1]:
                del tasks[delete]
            
        return order
