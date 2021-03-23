def ArimeticProgression(self, arr: List[int]) -> int:
        larger = -1000000
        idx = None
        for i in range(0, len(arr)-1):
            if abs(arr[i+1]-arr[i]) > larger:
                idx = i+1
                larger = abs(arr[i+1]-arr[i])
       # in-place modification
       arr.insert(idx, (arr[idx]+arr[idx-1])//2)
