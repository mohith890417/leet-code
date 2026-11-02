class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest = 0
        
        for g in gain:
            current_altitude += g
            if current_altitude > highest:
                highest = current_altitude
                
        return highest