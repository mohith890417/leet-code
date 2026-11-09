from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        n = len(senate)
        
        # Populate queues with initial senator indices
        for i, char in enumerate(senate):
            if char == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
                
        # Simulate rounds
        while r_queue and d_queue:
            r_index = r_queue.popleft()
            d_index = d_queue.popleft()
            
            # The senator with the smaller index bans the other
            if r_index < d_index:
                # Radiant survives and gets to vote in the next round
                r_queue.append(r_index + n)
            else:
                # Dire survives and gets to vote in the next round
                d_queue.append(d_index + n)
                
        return "Radiant" if r_queue else "Dire"