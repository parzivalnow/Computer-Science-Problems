# Normally I do not put Leetcode metrics on here, but this was a great question to learn from. 
# Today, writing green code (energy-conserving code) is becoming more and more important for IoT applications
# and datacenters. At the time of this writing, there were 30,934 accepted submissions out of 64,905 submissions. 
# The best memory allocation was 16.5 MB, with 0.18% of the accepted submissions meeting this. 
# The algorithm below is simple and requires only 16.2 MB of memory.

# *************** Please modify to make the runtime better if you see any shortcuts ******************** #

def advantageCount(A, B):
        if len(A) != len(B):
            return -1
        
        maxB = sorted(B, reverse = True)
        maxA = sorted(A, reverse = True)
        length = len(maxA)
        newArr = [0 for _ in range(len(A))]
        
        while length > 0:
            idx = B.index(maxB[0])
            if maxB[0] >= maxA[0]:
                newArr[idx] = maxA[-1]
                del maxB[0]
                del maxA[-1]
            
            else:
                newArr[idx] = maxA[0]
                del maxB[0]
                del maxA[0]
                
            # Poison
            B[idx] = None
            length -= 1
        
        return newArr
