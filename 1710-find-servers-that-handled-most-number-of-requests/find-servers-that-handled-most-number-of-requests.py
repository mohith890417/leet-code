import heapq
import bisect

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []  # Min-heap storing (end_time, server_id)
        available_servers = list(range(k))  # Sorted list of currently available servers
        
        counts = [0] * k
        
        for i in range(len(arrival)):
            arr = arrival[i]
            dur = load[i]
            
            # 1. Free up servers whose tasks have finished by the current arrival time
            while busy and busy[0][0] <= arr:
                _, s_id = heapq.heappop(busy)
                idx = bisect.bisect_left(available_servers, s_id)
                if idx == len(available_servers) or available_servers[idx] != s_id:
                    available_servers.insert(idx, s_id)
            
            # If no servers are available, drop the request
            if not available_servers:
                continue
                
            # 2. Find the preferred server index (i % k) using binary search
            preferred = i % k
            idx = bisect.bisect_left(available_servers, preferred)
            
            # If no available server >= preferred, wrap around to the first available server
            if idx == len(available_servers):
                server_id = available_servers.pop(0)
            else:
                server_id = available_servers.pop(idx)
                
            # 3. Assign the request to the chosen server
            counts[server_id] += 1
            heapq.heappush(busy, (arr + dur, server_id))
            
        # 4. Find all servers that handled the maximum number of requests
        max_handled = max(counts)
        return [i for i, c in enumerate(counts) if c == max_handled]