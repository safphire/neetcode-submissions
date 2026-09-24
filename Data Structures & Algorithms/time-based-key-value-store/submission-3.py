class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            #add the value with the timestamp to the list
            self.store[key].append((value, timestamp))
        else:
            #create new array
            self.store[key] = [(value, timestamp)]


    def get(self, key: str, timestamp: int) -> str:
        #return the value after array.
        searchlist = self.store.get(key, None)
        if not searchlist:
            return ""
        # print(searchlist)
        start = 0
        end = len(searchlist) - 1
        ans = ""
        while start <= end: 
            mid = (start + end) // 2
            val, ts = searchlist[mid]
            if timestamp == ts:
                return val
            elif timestamp < ts:
                end = mid - 1
            else:
                ans = val
                start = mid + 1
        return ans