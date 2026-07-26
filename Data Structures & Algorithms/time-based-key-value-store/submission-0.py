class TimeMap:

    def __init__(self):
        """
        {
          "alice": [(1, "hello"), (2,"bye"), (10, "zzz")]
        }
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        kvs = self.store[key]
        # kvs are in increasing order of timestamp
        # find timestamp or next biggest timestamp
        res = ""
        l, r = 0, len(kvs)-1
        while l <= r:
            mid = l + (r-l) // 2
            if kvs[mid][0] <= timestamp:
                res = kvs[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
