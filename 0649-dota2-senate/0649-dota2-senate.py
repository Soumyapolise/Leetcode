class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQueue, dQueue = deque(), deque()
        
        for i in range(len(senate)):
            if senate[i] == "R":
                rQueue.append(i)
            else:
                dQueue.append(i)
            
        
        while rQueue and dQueue:
            r_turn = rQueue.popleft()
            d_turn = dQueue.popleft()
            
            if d_turn < r_turn:
                dQueue.append(d_turn + len(senate))
            else:
                rQueue.append(r_turn + len(senate))
        
        if rQueue: #there are just R's left
            return "Radiant"
        else: #there are just D's left - dominating!!!!!
            return "Dire"