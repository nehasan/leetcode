from collections import deque

class RecentCounter:
    def __init__(self):
      self.requests = deque()

    def ping(self, t: int) -> int:
      self.requests.append(t)
      if len(self.requests) == 1:
        return 1
      else:
        while True:
          first = self.requests[0]
          last = self.requests[-1]
          
          if (last - first) > 3000:
            self.requests.popleft()
          else:
            return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(200))
print(obj.ping(3000))
print(obj.ping(3010))
print(obj.ping(3020))

