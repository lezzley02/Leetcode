def canShip(weights,days,capacity):
    day_used = 1
    current_weight =0
    
    for weight in weights:
        if  current_weight + weight > capacity:
             day_used += 1
             current_weight = weight
        else :
             current_weight += weight 
    return day_used <= days


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)  

        while low < high :
            mid =(low +high)//2
            if canShip(weights,days,mid):
                high = mid
            else :
                low = mid +1
        return low