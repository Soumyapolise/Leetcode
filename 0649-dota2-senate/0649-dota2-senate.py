class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_Queue, d_Queue = deque(), deque()
        
        for i in range(len(senate)):
            if senate[i] == "R":
                r_Queue.append(i)
            else:
                d_Queue.append(i)
        
        while r_Queue and d_Queue:
            r_turn = r_Queue.popleft()
            d_turn = d_Queue.popleft()
            
            if r_turn < d_turn:
                r_Queue.append(r_turn + len(senate))
            else:
                d_Queue.append(d_turn + len(senate))
            
        
        if r_Queue:
            return "Radiant"
        
        if d_Queue:
            return "Dire"