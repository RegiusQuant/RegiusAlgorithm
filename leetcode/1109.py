from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        delta = [0] * (n + 2)
        for first, last, seats in bookings:
            delta[first] += seats
            delta[last + 1] -= seats

        prefix = [0]
        for x in delta[1:]:
            prefix.append(prefix[-1] + x)

        return prefix[1: -1]
